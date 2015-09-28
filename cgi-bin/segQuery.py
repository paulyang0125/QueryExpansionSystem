#encoding=utf-8
import jieba, re, string
testDict = "dict/dict.txt.big"
jieba.load_userdict(testDict)
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import jieba.posseg as pseg


############# find file name to seg ####################


def segmentCTListPerQuerys(listOfCTPerQuery):
	segCTStringInAQuery= []
	allLinePerQuery = []
	for line in listOfCTPerQuery:
		out1 = re.sub('[a-zA-Z]+', '', line)       
		out1 = re.sub('[%s]' % re.escape(string.punctuation), '', out1)
		segline = pseg.cut(out1.decode("utf-8"))
		allLinePerQuery.append(segline)
	for line in allLinePerQuery:
		for z in line:
			seglinePerQuery = []
			if z.flag == "n" or z.flag == "ns" or z.flag == "v" or z.flag == "t" or z.flag == "a" or z.flag == "nr" or z.flag == "nz" or z.flag == "i" or z.flag == "m":
				seglinePerQuery.append(z.word.encode("utf-8"))
		seglineString = ' '.join(str(e) for e in seglinePerQuery)
		segCTStringInAQuery.append(seglineString)
	return segCTStringInAQuery

def segmentToListPerQuery(queryString):
	listPerQuery = []
	segedList = []
	out1 = re.sub('[a-zA-Z]+', '', queryString)       
	out1 = re.sub('[%s]' % re.escape(string.punctuation), '', out1)
	#segString = pseg.cut(queryString.decode("utf-8"))
	segString = pseg.cut(queryString.decode("utf-8"))
	#segString = jieba.cut(queryString,cut_all=False)
	#print ".. ".join(segString)
	#for i in segString:
	#	listPerQuery.append(i)

	for z in segString:
		#print z.word + "\n"
		#if z.flag == "n" or z.flag == "ns" or z.flag == "v" or z.flag == "t" or z.flag == "a" or z.flag == "nr" or z.flag == "nz" or z.flag == "i" or z.flag == "m":
		if z.flag != "x":
			segedList.append(z.word.encode("utf-8"))
	return segedList

	
	
