import re
import asyncio
import aiohttp
import pandas as pd
from bs4 import BeautifulSoup
import docx
from PyPDF2 import PdfReader
import os
import tkinter as tk
from tkinter import filedialog

def read_file(file_path):
    if file_path.endswith('.txt'):
        with open(file_path, 'r') as file:
            return file.read()
    elif file_path.endswith('.docx'):
        doc = docx.Document(file_path)
        return ' '.join([paragraph.text for paragraph in doc.paragraphs])
    elif file_path.endswith('.pdf'):
        with open(file_path, 'rb') as file:
            pdf = PdfReader(file)
            return ' '.join([page.extract_text() for page in pdf.pages])
    else:
        input("不支持的文件格式！按任意键退出")
        exit()

# 异步获取单词信息的函数
async def request_word(session, word):
    url = f'https://www.youdao.com/w/eng/{word}'
    try:
        async with session.get(url) as response:
            data = await response.text()
            soup = BeautifulSoup(data, 'html.parser')
            # 获取英式发音
            British = soup.select_one('#phrsListTab > h2 > div > span:nth-child(1) > span').text
            # 获取美式发音
            American = soup.select_one('#phrsListTab > h2 > div > span:nth-child(2) > span').text
            # 获取单词释义
            paraphrase = ' '.join([li.text for li in soup.select('#phrsListTab > div > ul > li')])
            return word, British, American, paraphrase
    except Exception as e:
        return None

# 处理文本文件的函数
async def article_to_words(file_path):
    # 读取文本文件
    try:
        content = read_file(file_path)
    except:
        input("文件读取失败！请检查文件名是否正确！按任意键退出")
        exit()
    # 将内容分隔为单词列表
    words = re.split(r"\b[,.:?!()'\"\s\n\t\r]+?\b", content)
    sorted_words = sorted(list(set([word.lower() for word in words])))
    # 创建一个空列表用于存储过滤后的单词
    filtered_words = []

    # 定义一个正则表达式用于匹配非字母字符
    pattern = re.compile(r"[^a-zA-Z\s]")

    for word in sorted_words:
        # 排除包含撇号的单词
        if "'" in word:
            continue
        # 使用正则表达式排除包含非字母字符的单词
        if pattern.search(word):
            continue
        # 将过滤后的单词添加到列表中
        filtered_words.append(word)
    
    async with aiohttp.ClientSession() as session:
        tasks = [request_word(session, word) for word in filtered_words]
        word_info = await asyncio.gather(*tasks)

    # 过滤 word_info 中的 None 值
    word_info = [info for info in word_info if info is not None]

    # 将单词信息导出到Excel
    df = pd.DataFrame(word_info, columns=['单词', '英式发音', '美式发音', '释义'])
    output_file = os.path.splitext(file_path)[0] + '.xlsx'
    df.to_excel(output_file, index=False)
    input('文件保存成功！按任意键退出！')


def choose_file():
    # 使用filedialog.askopenfilename打开文件选择对话框
    # 只允许选择.docx，.pdf，.txt三种格式的文件
    filename = filedialog.askopenfilename(filetypes=(
        ('docx文件', '*.docx'),
        ('PDF文件', '*.pdf'),
        ('txt文件', '*.txt'),
        ('All Files', '*.*'),  # 允许选择所有类型的文件
    ))
    return filename

filename = choose_file()

# 运行主程序
asyncio.run(article_to_words(filename))