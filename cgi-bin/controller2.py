#! /usr/local/bin/python3
import cgitb
cgitb.enable()
import sys
import cgi 
import urllib
import os, sys, inspect
# realpath() with make your script run, even if you symlink it :)
import yate
import mainmodel
import markup
import segQuery
import pickle
import itertools
import time
import myquerypaser


ehowdir = 'data/ehownet/'

#######

def iter_documents(top_directory):
    """Iterate over all documents, yielding a document (=list of utf8 tokens) at a time."""
    for root, dirs, files in os.walk(top_directory):
        for file in filter(lambda file: file.endswith('.txt'), files):
            #filename = file
            #print filename
            document = open(os.path.join(root, file)).read() # read the entire document, as one big string
            yield document # or whatever tokenization suits you

def set_FakeListToStore(cheat = True):
#""" chating and suck coding  ... Ouput: {'airplane' or 'comic' or 'drama':{A or B: words}} """
	eHowNetRef = [line.split() for line in iter_documents(ehowdir)]
	try:
		with open('data/NEWehownet.pickle', 'wb') as ehw:
			pickle.dump(eHowNetRef, ehw)
	except IOError as ioerr:	
		print('File error (put_and_store): ' + str(ioerr))

def get_FakeListToStore(cheat = True, index = 'airplane'):
	try:
		with open('data/NEWehownet.pickle', 'rb') as ehw:
			eHowNetRef = pickle.load(ehw)
	except IOError as ioerr:
		print('File error (get_from_store): ' + str(ioerr))

	return (eHowNetRef)
	
def recursiveFindAllCombinations(listA,listB):
	result = list(itertools.product(listA,listB))
	return result 
	
def joinAllWordAsQuery(recursiveResults):
	l1 = []
	for i in recursiveResults:
		q = ''.join(str(e) for e in i)
		l1.append(q)
	return l1

def get_allExpannedQueryFromStore(SQ):
	eHowNetRefList = get_FakeListToStore()
	print eHowNetRefList
	SQ  = [line.strip() for line in SQ ]
	print "SQ"
	print SQ
	tempPos0 = []
	tempPos1 = []
	for lis in eHowNetRefList:
		if any(SQ[0] in s for s in lis):
			tempPos0 = lis
		elif any(SQ[1] in s for s in lis):
			tempPos1 = lis
	rResult = recursiveFindAllCombinations(tempPos0,tempPos1)
	print "RrESULT"
	print rResult
	combinedQueryList = joinAllWordAsQuery(rResult)
	return combinedQueryList
	
def getDisplayResult(which_page,dicOfAllPagesOfAQuery):
	titles = myquerypaser.dicOfAllPagesOfAQuery[which_page]['titles']
	contents = dicOfAllPagesOfAQuery[which_page]['contents']
	url = dicOfAllPagesOfAQuery[which_page]['url']
	return titles, contents, url
	
def prepareSegDataForAprori(webQuerryResultPerQuery):
	ctListPerQuery = myquerypaser.jsonPaserForOneQuery(webQuerryResultPerQuery, mergeCTResult = True)
	segCTStingListPerQuery = segQuery.segmentCTListPerQuerys(ctListPerQuery)
	return segCTStingListPerQuery

	


# cheat, init ehownet list 

## init 
set_FakeListToStore()

## 
form_data = cgi.FieldStorage()
term = form_data['terms'].value
print(yate.start_response())
print(yate.include_header("Aprori Page for " + str(term)))

## if query exist in SQL or pickle(utlmate result), check, and get the results 



### segment 
segmentedQuery = segQuery.segmentToListPerQuery(term)
print(yate.para("These are segmented query: "))
print ("<h1>" +  str(segmentedQuery) + "<h1>")
print(yate.u_list(segmentedQuery))

### look up from ehownet 
expandedQueries = get_allExpannedQueryFromStore(segmentedQuery)
print(yate.para("These are expanded queries: "))
print(yate.u_list(expandedQueries))

### render the output - rulenum, resultset 
print(yate.para("These are websnippt"))

# "results" are the JSONs list containing each page result FOR ONE QUERY [[ONE PAGE - title,content,url],[ONE PAGE - JSON]]



#for each_query in expandedQueries: 
#	time.sleep(2) # delays for 5 seconds
#	print(yate.include_header("The is a search page for " + str(each_query)))
#	results = mainmodel.get_googleResult_from_firstQuery(each_query)
#	
#	for each in results:
#		if each['responseStatus'] == 200:
#			onePageTitles,onePageContents,onePageUrls  = jsonPaserForOnePage(each)
#			for title, content, url in zip(onePageTitles,onePageContents,onePageUrls):
#				print(yate.render_search_result(title,content,url))
#				
			
### run aprori

final_dic = {}

for each_query in expandedQueries: 
	time.sleep(1) # delays for 5 seconds
	print(yate.include_header("The is a segment page for " + str(each_query)))
	results = mainmodel.get_googleResult_from_firstQuery(each_query)
	segCTList = prepareSegDataForAprori(results)
	for w in segCTList:
		print(yate.render_seg_result(w))

						
 





