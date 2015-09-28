#! /usr/local/bin/python3
import cgitb
cgitb.enable()
import sys
import cgi 
import urllib

import os, sys, inspect
# realpath() with make your script run, even if you symlink it :)
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
if cmd_folder not in sys.path:
	sys.path.insert(0, cmd_folder)
# use this if you want to include modules from a subforder
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"subfolder")))
if cmd_subfolder not in sys.path:
	sys.path.insert(0, cmd_subfolder)

import yate
import mainmodel
import markup

####################SINGLE QUERY ##########################################
def jsonPaserForOnePage(each_json):
	titles = []
	contents = []
	urls = []
	####### each JSON means each page result in a JSON 
	for result in each_json['responseData']['results']:
		temp_title = urllib.unquote(result['titleNoFormatting']).encode('utf-8')
		titles.append(temp_title)
		temp_content = result['content'].encode('utf-8').strip("<b>...</b>").replace("<b>",'').replace("</b>",'').replace("&#39;","'").strip()
		contents.append(temp_content)
		temp_url = urllib.unquote(result['unescapedUrl']).encode('utf-8')
		urls.append(temp_url)
	return titles, contents, urls
	
def each_jsonPaser(each_json):
	all_result = []
	for result in each_json['responseData']['results']:
		each_result = []
		temp_title = urllib.unquote(result['titleNoFormatting']).encode('utf-8')
		each_result.append(temp_title)
		temp_content = result['content'].encode('utf-8').strip("<b>...</b>").replace("<b>",'').replace("</b>",'').replace("&#39;","'").strip()
		each_result.append(temp_content)
		temp_url = urllib.unquote(result['unescapedUrl']).encode('utf-8')
		each_result.append(temp_url)
		all_result.append(each_result)
	return all_result
	
def each_jsonPaserUsingDic(each_json):
	all_result = {}
	for result in each_json['responseData']['results']:
		temp_title = urllib.unquote(result['titleNoFormatting']).encode('utf-8')
		all_result['title'] = temp_title
		each_result.append(temp_title)
		temp_content = result['content'].encode('utf-8').strip("<b>...</b>").replace("<b>",'').replace("</b>",'').replace("&#39;","'").strip()
		each_result.append(temp_content)
		temp_url = urllib.unquote(result['unescapedUrl']).encode('utf-8')
		each_result.append(temp_url)
		all_result.append(each_result)
	return all_result
	
########## MULTIPLE query ########################



####### controller process #############3

form_data = cgi.FieldStorage()
term = form_data['terms'].value

# "results" are the JSONs list containing each page result FOR ONE QUERY [[ONE PAGE - title,content,url],[ONE PAGE - JSON]]
results = mainmodel.get_googleResult_from_firstQuery(term)

#for each in results:	
#	fordiaply = each_jsonPaser(each)

for each in results:	
	onePageTitles,onePageContents,onePageUrls  = jsonPaserForOnePage(each)

print(yate.start_response())
print(yate.include_header("The is a search page for " + str(term)))
print(yate.include_menu({"satisfied, go back Google": "/index.html"}, str(term) ))
#print(yate.start_form("controller2.py"))
#print(yate.input_text('terms',str(term)))
#print(yate.end_form("enter to my app"))
#print(yate.para("Query for:" + str(term)))

#print("<br /><br />")
for title, content, url in zip(onePageTitles,onePageContents,onePageUrls):
		print(yate.render_search_result(title,content,url))
#mypage = markup.page()
#mypage.addfooter("fuck you")
#print (mypage)


#print("<button type="button" onclick="alert('Hello world!')">Click Me!</button>")

