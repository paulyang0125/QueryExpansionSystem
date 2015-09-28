#encoding=utf-8
import jieba, re, string
testDict = "C:/dataset/dict/dict.txt.big"
jieba.load_userdict(testDict)
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import jieba.posseg as pseg
import jianfan


############# find file name to seg ####################


def segmentToListPerAllQuerys(refFileName):
	listPerQuery = []
	listForAllQueryExpand = []
	for line1 in open(refFileName):
		out1 = re.sub('[a-zA-Z]+', '', line1)       
		out1 = re.sub('[%s]' % re.escape(string.punctuation), '', out1)
		words1 = jieba.cut(out1.decode("utf-8"))
		listPerQuery.append(words1)
	listForAllQueryExpand.append(listPerQuery)
	return listForAllQueryExpand

def segmentToListPerQuery(queryString):
	listPerQuery = []
	segedList = []
	out1 = re.sub('[a-zA-Z]+', '', queryString)       
	out1 = re.sub('[%s]' % re.escape(string.punctuation), '', out1)
	#segString = pseg.cut(queryString.decode("utf-8"))
	dd = jianfan.ftoj(out1).encode("utf-8")
	segString = pseg.cut(dd)
	#segString = pseg.cut(queryString.decode("utf-8"))
	#segString = jieba.cut(queryString,cut_all=False)
	#print ".. ".join(segString)
	#for i in segString:
	#	listPerQuery.append(i)

	for z in segString:
		#print z.word + "\n"
		#if z.flag == "n" or z.flag == "ns" or z.flag == "v" or z.flag == "t" or z.flag == "a" or z.flag == "nr" or z.flag == "nz" or z.flag == "i" or z.flag == "m":
		if z.flag != "x":
			#segedList.append(z.word.encode("utf-8"))
			dd = jianfan.jtof(z.word).encode("utf-8")
                        #segedList.append(dd)
			segedList.append(z.word)
	return segedList

	
	
