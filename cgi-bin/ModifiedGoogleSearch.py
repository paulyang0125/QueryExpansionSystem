# -*- coding: utf-8 -*-  
#!/usr/bin/python
"""
Google AJAX Search Module
http://code.google.com/apis/ajaxsearch/documentation/reference.html
"""
try:
    import simplejson as json
except:
    import json
import urllib

import sys

__author__ = "Kiran Bandla"
__version__ = "0.1"
URL = 'http://ajax.googleapis.com/ajax/services/search/web?'

#Web Search Specific Arguments
#http://code.google.com/apis/ajaxsearch/documentation/reference.html#_fonje_web
#SAFE,FILTER
"""
SAFE
This optional argument supplies the search safety level which may be one of:
    * safe=active - enables the highest level of safe search filtering
    * safe=moderate - enables moderate safe search filtering (default)
    * safe=off - disables safe search filtering
"""
SAFE_ACTIVE     = "active"
SAFE_MODERATE   = "moderate"
SAFE_OFF        = "off"

"""
FILTER
This optional argument controls turning on or off the duplicate content filter:

    * filter=0 - Turns off the duplicate content filter
    * filter=1 - Turns on the duplicate content filter (default)

"""
FILTER_OFF  = 0
FILTER_ON   = 1

#Standard URL Arguments
#http://code.google.com/apis/ajaxsearch/documentation/reference.html#_fonje_args
"""
RSZ
This optional argument supplies the number of results that the application would like to recieve. 
A value of small indicates a small result set size or 4 results. 
A value of large indicates a large result set or 8 results. If this argument is not supplied, a value of small is assumed. 
"""
RSZ_SMALL = "small"
RSZ_LARGE = "large"

"""
HL
This optional argument supplies the host language of the application making the request. 
If this argument is not present then the system will choose a value based on the value of the Accept-Language http header. 
If this header is not present, a value of en is assumed.
"""


#query = '深夜食堂'
#testfolder = "C:/dataset/final/updatedA2/"


class pygoogle:
    
	def __init__(self,query,pages=10,hl='zh-TW'):
		self.pages = pages          #Number of pages. default 10
		self.query = query
		self.filter = FILTER_ON     #Controls turning on or off the duplicate content filter. On = 1.
		self.rsz = RSZ_LARGE        #Results per page. small = 4 /large = 8
		self.safe = SAFE_OFF        #SafeBrowsing -  active/moderate/off
		self.hl = hl                #Defaults to English (en)
		self.containerForAllData = []    # this is used to collect JSON data 
        #self.testfolder = "C:/dataset/final/updatedB/"
        #self.testfolder = "C:/dataset/final/justfortest/Sep_specific_comic/"
        #self.testFile1 = self.testfolder + "allTest" + '.txt'
        #self.testFile1 = self.testfolder + "allTest" + '.temp'
        #self.allTextFile = self.testfolder + str(self.query).decode("utf-8") + '.all'
        #self.onlyTitleFile = self.testfolder + str(self.query).decode("utf-8") + '.title'
        #self.onlyContentFile = self.testfolder + str(self.query).decode("utf-8") + '.content'
        #self.onlyLinkFile = self.testfolder + str(self.query).decode("utf-8") + '.link'
        #fp1=open(testFile1,"w")
        #self.fp2=open(self.allTextFile,"w")
        #self.fp3=open(self.onlyTitleFile,"w")
        #self.fp4=open(self.onlyContentFile,"w")
        #self.fp5=open(self.onlyLinkFile,"w")
        
	def __search__(self,print_results = False):
		results = []
		for page in range(0,self.pages):
			rsz = 8
			if self.rsz == RSZ_SMALL:
				rsz = 4
			args = {'q' : self.query,
                    'v' : '1.0',
                    'start' : page*rsz,
                    'rsz': self.rsz,
                    'safe' : self.safe, 
                    'filter' : self.filter,    
                    'hl'    : self.hl
                    }
			q = urllib.urlencode(args)
			search_results = urllib.urlopen(URL+q)
			data = json.loads(search_results.read(), encoding="utf-8")
            #self.writeFile(data)
			self.collectJSONDatas(data)
	    #data = json.loads(search_results.read())
			if print_results:
				if data['responseStatus'] == 200:
					for result in  data['responseData']['results']:
						if result:	
							print '[%s]'%(urllib.unquote(result['titleNoFormatting'])).encode('utf-8')
							print result['content'].encode('utf-8').strip("<b>...</b>").replace("<b>",'').replace("</b>",'').replace("&#39;","'").strip()
							print urllib.unquote(result['unescapedUrl']).encode('utf-8') +'\n'                
			results.append(data)
		return data
		
	def collectJSONDatas(self, data):
		self.containerForAllData.append(data)


	def writeFile(self,data):
		fp1=open(self.testFile1,"w")
		fp1.write(json.dumps(data, ensure_ascii=False).encode('utf-8'))
        #data = json.loads(data, encoding="utf-8")
		if data['responseStatus'] == 200:
			for result in data['responseData']['results']:
            #print type(result)
            #print '[%s]'%(urllib.unquote(result['titleNoFormatting']))
				title = urllib.unquote(result['titleNoFormatting']).encode('utf-8')
            #print "title is"
            #print type(title)
				self.fp2.write(title + '\n')
				self.fp3.write(title + '\n')
            #print result['content'].encode('utf-8').strip("<b>...</b>").replace("<b>",'').replace("</b>",'').replace("&#39;","'").strip()
				content = result['content'].encode('utf-8').strip("<b>...</b>").replace("<b>",'').replace("</b>",'').replace("&#39;","'").strip()
				self.fp2.write(content + '\n')
				self.fp4.write(content + '\n')
            #print urllib.unquote(result['unescapedUrl']).encode('utf-8')+'\n'
				url = urllib.unquote(result['unescapedUrl']).encode('utf-8')+'\n'
				self.fp2.write(url + '\n')
				self.fp5.write(url)
            #print type(f[result])
            #print f[result].decode('utf-8').encode('utf-8')    

            #for i in range( len(t) ):
            #print t[i].decode('utf-8').encode('gb2312')
		else:
			print "nothing found"
		fp1.close()
        
        
	def search(self):
		"""Returns a dict of Title/URLs"""
		results = {}
		for data in self.__search__():
			for result in  data['responseData']['results']:
				if result:
					title = urllib.unquote(result['titleNoFormatting'])
					results[title] = urllib.unquote(result['unescapedUrl'])
		return results

	def search_page_wise(self):
		"""Returns a dict of page-wise urls"""
		results = {}
		for page in range(0,self.pages):
			args = {'q' : self.query,
                    'v' : '1.0',
                    'start' : page,
                    'rsz': RSZ_LARGE,
                    'safe' : SAFE_OFF, 
                    'filter' : FILTER_ON,    
                    }
			q = urllib.urlencode(args)
			search_results = urllib.urlopen(URL+q)
			data = json.loads(search_results.read())
			urls = []
			for result in  data['responseData']['results']:
				if result:
					url = urllib.unquote(result['unescapedUrl'])
					urls.append(url)            
			results[page] = urls
		return results
        
	def get_urls(self):
		"""Returns list of result URLs"""
		results = []
		for data in self.__search__():
			for result in  data['responseData']['results']:
				if result:
					results.append(urllib.unquote(result['unescapedUrl']))
		return results

	def get_result_count(self):
		"""Returns the number of results"""
		temp = self.pages
		self.pages = 1
		result_count = 0
		try:
			result_count = self.__search__()[0]['responseData']['cursor']['estimatedResultCount']
		except Exception,e:
			print e
		finally:
			self.pages = temp
		return result_count    
        
	def display_results(self):
		"""Prints results (for command line)"""
		#self.get_fileName(input1)
		self.__search__()
		#self.fp2.close()
		#self.fp3.close()
		#self.fp4.close()
		#self.fp5.close()

    

#filename = "C:/dataset/final/AFileName.txt"
#fp7=open(filename,"r")
#data_list = [word.strip() for word in fp7]

#for i in data_list:
#	print "==== current processed file ===="
#	print i
#	query1 = i
#	g = pygoogle(query1)
#	print '*Found %s results*'%(g.get_result_count())
#	g.pages = 1
#	g.display_results()

	
	#print pygoogle(' '.join(sys.argv[1:])).display_results()
#fp7.close()


