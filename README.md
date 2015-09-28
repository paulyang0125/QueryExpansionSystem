#Apriori-based query expansion system for Chinese IR

This is the python-based prototype of Chinese query expansion system using CKIP eHownet dictionary and association mining algorithm – Apriori in order to explore more query options for user in Google. However, as this still belongs to init version and prototype, codes of interface, HTTP server and database use simple sqlite and CGI script for development and it doesn’t integrate the web-framework like Django and doesn't use the ways like multiprocessing or threading to improve cal performance. In addition, the full usage of ehownet through SQL is not for free, thus the number of terms in the current dictionary to expand the user query is limited. 

[the slide for more detail](http://www.slideshare.net/paulyang0125/web-query-expansion-based-on-association-rules-mining-with-e-hownet-and-google-chrome-extension-release)

## Quick-start

1.	[Jieba](https://github.com/fxsjy/jieba) is required to be installed in advance 

```
easy_install jieba

or 

pip install jieba
```

2.	Run *simple_httpd.py* to start the http development server
3.	Open *index.html* by any your preferred browser to enter the entry of the system
4.	Know about the status by checking *logs\server_info.log*


## Preview

![Demo](http://1.bp.blogspot.com/-mf13HX84GRI/VglDat6q9PI/AAAAAAAACuU/kM8D9BRqa4w/s640/output_h7oq54.gif)



## Technical Overview

- Make use of [Google Web Search API](https://developers.google.com/web-search/docs/?hl=zh-TW) to get the web snippet from Google index server   
- Use Bag of word and TF/IDF for feature exaction
- Use [Apriori algorithm](http://en.wikipedia.org/wiki/Apriori_algorithm)to mine the association rule in a webpage and use eHowbet and a simple weighted scheme to prioritize the rules
- Introduction to utilizing [CKIP ehownet](http://www.aclclp.org.tw/use_ckip_c.php)   


#### Use case diagram
![Demo1](http://3.bp.blogspot.com/-qj5S36hQXnQ/VglDha34LhI/AAAAAAAACuc/tGDYpMqxdH0/s640/arch1.png)

#### Flow chart
![Demo2](http://1.bp.blogspot.com/-IB0hM4P-OgY/VglDZ6LN5aI/AAAAAAAACtY/1oz-fhNQBCY/s640/flowchart.png)

#### Retrieval based on two dimensional system
![Demo3](http://2.bp.blogspot.com/-YFh8zg2Pgw8/VglDZwb6NKI/AAAAAAAACuY/tpAU-pgNqoM/s640/Result.png)


## License
The MIT License (MIT) Copyright (c) 2013 Yang Yao-Nien 

Permission is hereby granted, free of charge, to any person obtaining a copy ofthis software and associated documentation files (the "Software"), to deal inthe Software without restriction, including without limitation the rights touse, copy, modify, merge, publish, distribute, sublicense, and/or sell copies ofthe Software, and to permit persons to whom the Software is furnished to do so,subject to the following conditions: The above copyright notice and this permission notice shall be included in allcopies or substantial portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS ORIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESSFOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS ORCOPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHERIN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR INCONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


