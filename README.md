# 📚 英文文章单词切割工具🔪🔍
本项目来源于[《腾讯云 Cloud Studio 实战训练营》](https://marketing.csdn.net/p/06a21ca7f4a1843512fa8f8c40a16635)的参赛作品，该作品在腾讯云 [Cloud Studio](https://www.cloudstudio.net/?utm=csdn) 中运行无误。

一个简单的Python工具，它可以把英文文章（.docx，.txt，.pdf三种格式）切割为单词，然后添加发音和释义，最后以表格的形式输出，此为学习python的练手作，有不足之处恳请大佬指正！🎉🎉

## 🚀 功能

1. 将英文文章切割为单词
2. 自动爬取有道词典网页，获取单词的发音和释义
3. 以表格的形式输出结果

## 📦 安装

你可以在 [release ↗](https://github.com/haorwen/EnglishArticleProcessor/releases) 下载到py文件，用法见如何使用

## 🎯 如何使用

### EXE

exe文件打包后过大，暂不提供

### Python源码

使用前请先安装依赖：

```bash
pip install -r requirements.txt
```

如果你使用源码-弹窗版，使用以下命令：

```bash
python article_to_words_gui.py
```

如果你选择了源码-命令行版，使用以下命令：

```bash
python article_to_words.py {文件名}
```

## 🔨 开发

这个工具是用Python编写的。如果有大佬能给出优化或改进，欢迎提出Pull Request。

## 📜 许可

这个项目采用MIT许可。

## 📬 联系

如果你有任何问题或者建议，欢迎通过issue或者电子邮件联系我。

---

💻 haorwen@qq.com

---
