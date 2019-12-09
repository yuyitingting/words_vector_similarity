import logging
import sys
from gensim.corpora import WikiCorpus
#将下载的训练语料压缩包转换为txt格式存储在wiki.zh.txt中

#设置日志格式
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', level=logging.INFO)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit(1)
    logging.info("running %s" % ' '.join(sys.argv))
    inp, outp = sys.argv[1:3]
    i = 0
    output = open(outp, 'w', encoding='utf8')
    wiki = WikiCorpus(inp, lemmatize=False, dictionary={})
    for text in wiki.get_texts():
        output.write(" ".join(text) + "\n")
        i = i + 1
        if (i % 10000 == 0):
            logging.info("Save " + str(i) + " articles")
    output.close()
    logging.info("Finished saved " + str(i) + "articles")

