#encoding=utf-8
import sqlite3
#import segQuery
import ModifiedGoogleSearch
import itertools
import glob
import re, string
import pickle 
from itertools import izip

db_name = 'myquery1.sqlite'
eHownetMapping = '../data/mapping.conf'
cheatFakeAll = '../data/ehownet/'
airplaneRef = '../data/ehownet/airplane/'
comicRef = '../data/ehownet/comic/'
dramaRef = '../data/ehownet/drama/'

######### init ##############

def generateIndex(segString):
#"""not completed yet"""
	index = str
	#with open(airplaneRef + "A.txt",'rt') as F1, open(airplaneRef + "B.txt",'rt') as F2:
	#	for f1, f2 in izip(F1, F2):
	#		if f1.find(queryString) >= 0:
	for data in glob.glob(airplaneRef + "*.txt"):
		if data.find(queryString) >= 0:
			index = airplane
			return index
	for data in glob.glob(comicRef + "*.txt"):
		if data.find(queryString) >= 0:
			index = comic
			return index
	for data in glob.glob(dramaRef + "*.txt"):
		if data.find(queryString) >= 0:
			index = drama
			return index


def set_FakeListToStore(cheat = True):
#""" chating and suck coding  ... Ouput: {'airplane' or 'comic' or 'drama':{A or B: words}} """
	dicToPickle = {}
	tempDic = {}
	tempA = []
	tempB = []
	###### cheat 
	#if index == airplane:
	try:
		data_files_1 = open(airplaneRef + "A.txt")
		data_files_2 = open(airplaneRef + "B.txt")
		aIndex = 'airplane'
		#data_files = glob.glob(airplaneRef + "*.txt")
	#elif index == comic:
		data_files_3 = open(comicRef+ "A.txt") 
		data_files_4 = open(comicRef + "B.txt")
		cIndex = 'comic'
		#data_files = glob.glob(comicRef + "*.txt")
	#else index == comic:
		data_files_5 = open(dramaRef + "A.txt") 
		data_files_6 = open(dramaRef + "B.txt")
		dIndex = 'drama'
		#data_files = glob.glob(dramaRef + "*.txt")
	except IOError as ioerr:
		print('File error (get_coach_data): ' + str(ioerr))
		pass
	for line1, line2 in zip(data_files_1,data_files_2):
		tempA.append(line1.replace('\n', '').decode("utf-8").encode("utf-8"))
		tempB.append(line2.replace('\n', '').decode("utf-8").encode("utf-8"))
		tempDic['A'] = tempA
		tempDic['B'] = tempB
	dicToPickle[aIndex] = tempDic
	
	tempDic = {}
	tempA = []
	tempB = []
	
	#for line1, line2 in zip(data_files_3,data_files_4):
	#	tempA.append(line1)
	#	tempB.append(line2)
	#	tempDic['A'] = tempA
	#	tempDic['B'] = tempB
	#dicToPickle[cIndex] = tempDic
	
	tempDic = {}
	tempA = []
	tempB = []
	
	#for line1, line2 in zip(data_files_3,data_files_4):
	#	tempA.append(line1)
	#	tempB.append(line2)
	#	tempDic['A'] = tempA
	#	tempDic['B'] = tempB
		
	#dicToPickle[dIndex] = tempDic
	try:
		with open('../data/ehownet.pickle', 'wb') as ehw:
			pickle.dump(dicToPickle, ehw)
	except IOError as ioerr:
		print('File error (put_and_store): ' + str(ioerr))
	
	"""for line1, line2 in zip(data_files_1,data_files_2):
		tempA.append(line1)
		tempB.append(line2)
		tempDic['A'] = tempA
		tempDic['B'] = tempB
	dicToPickle[index] = tempDic
	try:
        with open('../data/ehownet.pickle', 'wb') as ehw:
            pickle.dump(dicToPickle, ehw)
    except IOError as ioerr:
        print('File error (put_and_store): ' + str(ioerr))
	"""
	
	
	return (dicToPickle)

def get_FakeListToStore(cheat = True, index = 'airplane'):
	dicFromPickle = {}
	try:
		with open('../data/ehownet.pickle', 'rb') as ehw:
			dicFromPickle = pickle.load(ehw)
	except IOError as ioerr:
		print('File error (get_from_store): ' + str(ioerr))

	return (dicFromPickle)



############  NORMAL GOOGLE QUERY #################### 

## controller passes the cgi "which_query" to model file: ModififedGoogleSearch.py 
## 

def segment_Query(userQuery):
#""" use chinese segment to seg query """
	segmentedQuery = segQuery.segmentToListPerQuery(userQuery)
	return segmentedQuery

def set_firstGoogleResultToSql(json_query_data):
#""" Store data to sqlite db """
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()
	cursor.execute("INSERT INTO newQuery(websnippet) VALUES (?)",unicode(json_query_data),)
	
def set_recursiveResultToSql(rCur):
#""" Store data to sqlite db """
	print rCur
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()
	cursor.execute("INSERT INTO newQuery(expandedContents) VALUES (?)", (unicode(rCur),)  )
	
def set_queryAndSegQueryToSql(originalQuery, segQuery):
#""" Store data to sqlite db """
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()
	cursor.execute("INSERT INTO newQuery(content, segmentedContent) VALUES (?,?)",(unicode(originalQuery),unicode(segQuery),))

def get_googleResult_from_firstQuery(userQuery, multipleQuery = False):
	if multipleQuery == False:
#""" Input: query String (which_query) from google-search bar """
# output: a list of JSONs containing each page result FOR ONE QUERY [[ONE PAGE - JSON],[ONE PAGE - JSON]]
		firstQuery = ModifiedGoogleSearch.pygoogle(userQuery)
		firstQuery.pages = 1
		firstQuery.display_results()
		print '*Found %s results*'%(firstQuery.get_result_count())
		#set_original_googleResultToSql(firstQuery)
		return firstQuery.containerForAllData





############  MY CUSTOM QUERY #################### 

## controller passes the cgi "which_query" to model file: ModififedGoogleSearch.py 

###old noy used######
def get_list_FromAcombinations(e_file):
	eachFileList = [] 
	for line in open(e_file):
		out1 = re.sub('[%s]' % re.escape(string.punctuation), '', line)
		eachFileList.append(out1)
	return eachFileList


def get_allList_from_ehownet(files_list):
	all_list = []
	for each_file in files_list:
		g = get_list_FromAcombinations(each_file)
		all_list.append(g)
	expanedquerys = recursiveFindAllCombinations(all_list)
	#joinExpanedquerys = joinAllWordAsQuery(results)
	return(expanedquerys)

###new######


#def recursiveFindAllCombinations(listOfwords):
def recursiveFindAllCombinations(listA,listB):
	result = list(itertools.product(listA,listB))
	return result 
	
def joinAllWordAsQuery(recursiveResults):
	l1 = []
	for i in recursiveResults:
		q = ''.join(str(e) for e in i)
		l1.append(q)
	return l1


#def resolveFilenameOfeHownet(segWordList = None, unsegWord, fake = TRUE):
#""" should use seged work to locate the FILEs for expanding but for this ver, just """


def get_allExpannedQueryFromStore(userQuery):
	allDics = get_FakeListToStore()
	print allDics
	SQ = segment_Query(userQuery)
	SQ  = [line.strip() for line in SQ ]
	print "SQ"
	print SQ
	tempA = []
	tempB = []
	for index, dic in allDics.items():
	#	for ll in dic['A']:
	#		print "dic A"
	#		print dic['A']
	#		if SQ[0] == ll:
	#			tempA = dic['A']
	#	print tempA
		if SQ[0] in dic['A']:
			tempA = dic['A']
			print "tempA"
			print tempA
		if SQ[1] in dic['B']:
			tempB = dic['B']
			print "tempB"
			print tempB
	rResult = recursiveFindAllCombinations(tempA,tempB)
	print "RrESULT"
	print rResult
	
	#set_recursiveResultToSql(rResult)
	combinedQueryList = joinAllWordAsQuery(rResult)
	return combinedQueryList

def get_googleResult_from_allExpandedQuery(combinedQueryList):
#""" Input: query String (which_query) from google-search bar output: get the list of JSONs """
	allJSON = {}
	for q in combinedQueryList:
		queryResult = ModifiedGoogleSearch.pygoogle(q)
		allJSON[q] = queryResult.containerForAllData
		#print '*Found %s results*'%(firstQuery.get_result_count())
	#set_original_googleResultToSql(firstQuery)
	
	return allJSON

def get_athlete_from_id(athlete_id):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    results = cursor.execute("""SELECT name, dob FROM athletes WHERE id=?""",
                                     (athlete_id,))
    (name, dob) = results.fetchone()
    results = cursor.execute("""SELECT value FROM timing_data WHERE athlete_id=?""",
                                     (athlete_id,))
    data = [row[0] for row in results.fetchall()]
    response = {'Name':   name,
                'DOB':    dob,
                'data':   data,
                'top3':   data[0:3]}
    connection.close()
    return(response)

def get_namesID_from_store():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    results = cursor.execute("""SELECT name, id FROM athletes""")
    response = results.fetchall()
    connection.close()
    return(response)
	
	############################







