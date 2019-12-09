import logging
import os
import sys
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
#根据切分后的简体中文语料学习词向量 训练后模型为：wiki.zh.text.model

#日志设置
if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # check and process input arguments
    if len(sys.argv) < 4:
        sys.exit(1)
    inp, outp1, outp2 = sys.argv[1:4]

    #词向量学习 CBOW
    #model = Word2Vec(LineSentence(inp), size=100, window=2)
    #skip-gram
    model = Word2Vec(LineSentence(inp), size=100, window=2,sg=1)
    model.save(outp1)
    model.wv.save_word2vec_format(outp2, binary=False)