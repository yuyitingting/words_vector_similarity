import jieba
import jieba.analyse
import codecs
#将转换为简体中文的训练语料分词 结果存储在wiki.zh.simple.seg.txt

#jieba分词
def cut_words(sentence):
    return " ".join(jieba.cut(sentence)).encode('utf-8')

#将分词后结果存储在wiki.zh.simple.seg.txt中
f=codecs.open('./wiki.zh.simple.txt','r',encoding="utf8")
target = codecs.open("wiki.zh.simple.seg.txt", 'w',encoding="utf8")
print('open files')
line_num=1
line = f.readline()
while line:
	if(line_num % 1000 == 0):
		print('---- processing', line_num, 'article----------------')
	line_seg = " ".join(jieba.cut(line))
	target.writelines(line_seg)
	line_num = line_num + 1
	line = f.readline()
f.close()
target.close()
exit()