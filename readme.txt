实验：利用训练语料学习的词向量计算输入的两个词的余弦相似度
步骤：
1.下载训练语料：https://dumps.wikimedia.org/backup-index.html  汉语数据
2.训练语料xml转换为txt格式（训练语料不用解压）
    对应的代码文件：xml2txt.py
    项目文件下运行： python3 homework.py zhwiki-20191120-pages-articles-multistream.xml.bz2 wiki.zh.txt
    转换后的文件：wiki.zh.txt
3.训练语料由繁体转换为简体中文
    项目文件下运行：python3.7 -m opencc -c t2s -i 项目路径/wiki.zh.txt -o 项目路径/wiki.zh.simple.txt
    转换后的文件：wiki.zh.simple.txt
4.切分简体中文语料（jieba）
    对应的代码：cut.py
    项目文件下运行：Python3.7 cut.py
    切分后的文件:wiki.zh.simple.seg.txt
5.词向量学习
    对应代码：train_.py
    项目文件下运行：python3.7 train_.py wiki.zh.simple.seg.txt wiki.zh.text.model
wiki.zh.text.vector
    学习到的向量表示模型：wiki.zh.text.model
6.计算测试文件的余弦相似度
    对应代码：similarity.py
    测试文件：pku_sim_test.txt
    测试结果：2019180151.txt

