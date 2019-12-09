from gensim.models import Word2Vec
import logging
import sys
import io
#利用学习词向量表示 计算测试文件中单词的余弦相似度 结果存储在2019180151.txt

#设置输出编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
#日志设置
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
#加载词向量模型
model=Word2Vec.load('./wiki.zh.text.model')
#a用来存储每行输出内容
a=''

#读取测试文件内容 计算两词之间的余弦相似度
with open('./pku_sim_test.txt',encoding='UTF-8-sig') as f:
    while True:
        array = f.readline().strip().split()
        if (array.__len__() == 0):#读到文件末尾
            break
        else:#未到文件末尾
            try:
                sim=model.similarity(array[0],array[1])#计算两词之间的余弦相似度
                #print(array[0]+'    '+array[1]+'    '+str(sim))
                a+='\n'+array[0]+'    '+array[1]+'    '+str(sim)
            except KeyError:
                #print(array[0]+'    '+array[1]+'    '+'OOV')
                a+='\n'+array[0]+'    '+array[1]+'    '+'OOV'
print(a)

#将计算的结果存储到2019180151.txt中
with open('./2019180151.txt','w',encoding='utf8') as f:
    f.write(a)

