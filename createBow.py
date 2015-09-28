#-*- coding:utf-8 - *-

def createBow(segmentedPage):
	"""Input: pathToFile output: numList and dictionary"""
	pageList = []
	wDic1 = {}
	wDic2 = {}
	dcount = 0
	with open(segmentedPage) as f:
		for line in f:
			if not line.isspace():
				words = line.split()
				pageList.append(words)
				for word in words:
					if word not in wDic1:
						wDic1[word] = dcount
						wDic2[dcount] = word
						dcount += 1
	revertedMap = []
	for line in pageList:
		tempList = []
		for word in line:
			for key, value in wDic2.iteritems():
				if value == word:
					tempList.append(key)
		revertedMap.append(tempList)
	#revertedMap = filter(None, revertedMap)
	return revertedMap, wDic2 




