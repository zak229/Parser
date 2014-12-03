# Written for Python 3.x (I think urllib will cause issues in Python 2.7.x, I think urllib.request should be changed to urllib2 to work in 2.7.x)
# Requires BeutifulSoup (bs4)
from bs4 import BeautifulSoup
from collections import Counter
import urllib.request, urllib.error, logging
logging.basicConfig(filename='parser.log',level=logging.INFO)
#2006 and on have /year/ after /litreleases/
url = "http://www.sec.gov/litigation/litreleases/lr"
url2 = "http://www.sec.gov/litigation/litreleases/"
#First case should be 14644
case = 14644
#every url ends in .txt until around 16100, it switches back and forth for a while afterword, goes to only .htm after (definitely) 16200.  
#Going to allow 100 cases to be slower to maximize sample size
sufswitchcase = 16100
sufswitchcase2 = 16200
#this is the last case of 1Q2006 -- last year before year was included in url
newestcase = 19635
suffix = ".htm"
suffix2 = ".txt"
#last case in each year
ohsix = 19955
ohseven = 20418
oheight = 20840
ohnine = 21357
ten = 21795
eleven = 22213
twelve = 22582
thirteen = 22900
#as of 12-02-14
fourteen = 23146
option = 0
spindashoff = 0
spinoff = 0
spinspaceoff = 0
spundashoff = 0
spunoff = 0
spunspaceoff = 0
insider = 0
divest = 0
fraud = 0
call = 0
put = 0
pyramid = 0
mislead = 0
misled = 0

while case <= sufswitchcase:
	try:
		urllib.request.urlopen(url + str(case) + suffix2)
	except urllib.error.URLError:
		case += 1
	else:
		text = BeautifulSoup(urllib.request.urlopen(url + str(case) + suffix2)).get_text().lower()
		option = text.count("option")
		spindashoff = text.count("spin-off")
		spinoff = text.count("spinoff")
		spinspaceoff = text.count("spin off")	
		spundashoff = text.count("spun-off")
		spunoff = text.count("spunoff")
		spunspaceoff = text.count("spun off")
		insider = text.count("insider")
		divest = text.count("divest")
		fraud = text.count("fraud")
		call = text.count("call")
		put = text.count("put")
		pyramid = text.count("pyramid")
		mislead = text.count("mislead")
		misled = text.count("misled")													
		logging.info("%d,option %d,spin-off %d,spinoff %d,spin off %d,spun-off %d,spunoff %d,spun off %d,insider %d,divest %d,fraud %d,call %d,put %d,pyramid %d,mislead %d,misled %d" % (case, option, spindashoff, spinoff, spinspaceoff, spundashoff, spunoff, spunspaceoff, insider, divest, fraud, call, put, pyramid, mislead, misled))
		print(case)
		case += 1	
while case <= sufswitchcase2:
	try:
		urllib.request.urlopen(url + str(case) + suffix)
	except urllib.error.URLError:
		try:
			urllib.request.urlopen(url + str(case) + suffix2)
		except urllib.error.URLError:
			case += 1
		else:
			text = BeautifulSoup(urllib.request.urlopen(url + str(case) + suffix2)).get_text().lower()
			option = text.count("option")
			spindashoff = text.count("spin-off")
			spinoff = text.count("spinoff")
			spinspaceoff = text.count("spin off")	
			spundashoff = text.count("spun-off")
			spunoff = text.count("spunoff")
			spunspaceoff = text.count("spun off")
			insider = text.count("insider")
			divest = text.count("divest")
			fraud = text.count("fraud")
			call = text.count("call")
			put = text.count("put")
			pyramid = text.count("pyramid")
			mislead = text.count("mislead")
			misled = text.count("misled")													
			logging.info("%d,option %d,spin-off %d,spinoff %d,spin off %d,spun-off %d,spunoff %d,spun off %d,insider %d,divest %d,fraud %d,call %d,put %d,pyramid %d,mislead %d,misled %d" % (case, option, spindashoff, spinoff, spinspaceoff, spundashoff, spunoff, spunspaceoff, insider, divest, fraud, call, put, pyramid, mislead, misled))
			print(case)
			case += 1
	else:
		text = BeautifulSoup(urllib.request.urlopen(url + str(case) + suffix)).get_text().lower()
		option = text.count("option")
		spindashoff = text.count("spin-off")
		spinoff = text.count("spinoff")
		spinspaceoff = text.count("spin off")	
		spundashoff = text.count("spun-off")
		spunoff = text.count("spunoff")
		spunspaceoff = text.count("spun off")
		insider = text.count("insider")
		divest = text.count("divest")
		fraud = text.count("fraud")
		call = text.count("call")
		put = text.count("put")
		pyramid = text.count("pyramid")
		mislead = text.count("mislead")
		misled = text.count("misled")													
		logging.info("%d,option %d,spin-off %d,spinoff %d,spin off %d,spun-off %d,spunoff %d,spun off %d,insider %d,divest %d,fraud %d,call %d,put %d,pyramid %d,mislead %d,misled %d" % (case, option, spindashoff, spinoff, spinspaceoff, spundashoff, spunoff, spunspaceoff, insider, divest, fraud, call, put, pyramid, mislead, misled))
		print(case)
		case += 1
while case <= newestcase:
	try:
		urllib.request.urlopen(url + str(case) + suffix)
	except urllib.error.URLError:
		case += 1
	else:
		text = BeautifulSoup(urllib.request.urlopen(url + str(case) + suffix)).get_text().lower()
		option = text.count("option")
		spindashoff = text.count("spin-off")
		spinoff = text.count("spinoff")
		spinspaceoff = text.count("spin off")	
		spundashoff = text.count("spun-off")
		spunoff = text.count("spunoff")
		spunspaceoff = text.count("spun off")
		insider = text.count("insider")
		divest = text.count("divest")
		fraud = text.count("fraud")
		call = text.count("call")
		put = text.count("put")
		pyramid = text.count("pyramid")
		mislead = text.count("mislead")
		misled = text.count("misled")													
		logging.info("%d,option %d,spin-off %d,spinoff %d,spin off %d,spun-off %d,spunoff %d,spun off %d,insider %d,divest %d,fraud %d,call %d,put %d,pyramid %d,mislead %d,misled %d" % (case, option, spindashoff, spinoff, spinspaceoff, spundashoff, spunoff, spunspaceoff, insider, divest, fraud, call, put, pyramid, mislead, misled))
		print(case)
		case += 1	
while case <= ohsix:
	try:
		urllib.request.urlopen(url2 + "2006/lr" + str(case) + suffix)
	except urllib.error.URLError:
		case += 1
	else:
		text = BeautifulSoup(urllib.request.urlopen(url2 + "2006/lr" + str(case) + suffix)).get_text().lower()
		option = text.count("option")
		spindashoff = text.count("spin-off")
		spinoff = text.count("spinoff")
		spinspaceoff = text.count("spin off")	
		spundashoff = text.count("spun-off")
		spunoff = text.count("spunoff")
		spunspaceoff = text.count("spun off")
		insider = text.count("insider")
		divest = text.count("divest")
		fraud = text.count("fraud")
		call = text.count("call")
		put = text.count("put")
		pyramid = text.count("pyramid")
		mislead = text.count("mislead")
		misled = text.count("misled")													
		logging.info("%d,option %d,spin-off %d,spinoff %d,spin off %d,spun-off %d,spunoff %d,spun off %d,insider %d,divest %d,fraud %d,call %d,put %d,pyramid %d,mislead %d,misled %d" % (case, option, spindashoff, spinoff, spinspaceoff, spundashoff, spunoff, spunspaceoff, insider, divest, fraud, call, put, pyramid, mislead, misled))
		print(case)
		case += 1	
while case <= ohseven:
	try:
		urllib.request.urlopen(url2 + "2007/lr" + str(case) + suffix)
	except urllib.error.URLError:
		case += 1
	else:
		text = BeautifulSoup(urllib.request.urlopen(url2 + "2007/lr" + str(case) + suffix)).get_text().lower()
		option = text.count("option")
		spindashoff = text.count("spin-off")
		spinoff = text.count("spinoff")
		spinspaceoff = text.count("spin off")	
		spundashoff = text.count("spun-off")
		spunoff = text.count("spunoff")
		spunspaceoff = text.count("spun off")
		insider = text.count("insider")
		divest = text.count("divest")
		fraud = text.count("fraud")
		call = text.count("call")
		put = text.count("put")
		pyramid = text.count("pyramid")
		mislead = text.count("mislead")
		misled = text.count("misled")													
		logging.info("%d,option %d,spin-off %d,spinoff %d,spin off %d,spun-off %d,spunoff %d,spun off %d,insider %d,divest %d,fraud %d,call %d,put %d,pyramid %d,mislead %d,misled %d" % (case, option, spindashoff, spinoff, spinspaceoff, spundashoff, spunoff, spunspaceoff, insider, divest, fraud, call, put, pyramid, mislead, misled))
		print(case)
		case += 1	
while case <= oheight:
	try:
		urllib.request.urlopen(url2 + "2008/lr" + str(case) + suffix)
	except urllib.error.URLError:
		case += 1
	else:
		text = BeautifulSoup(urllib.request.urlopen(url2 + "2008/lr" + str(case) + suffix)).get_text().lower()
		option = text.count("option")
		spindashoff = text.count("spin-off")
		spinoff = text.count("spinoff")
		spinspaceoff = text.count("spin off")	
		spundashoff = text.count("spun-off")
		spunoff = text.count("spunoff")
		spunspaceoff = text.count("spun off")
		insider = text.count("insider")
		divest = text.count("divest")
		fraud = text.count("fraud")
		call = text.count("call")
		put = text.count("put")
		pyramid = text.count("pyramid")
		mislead = text.count("mislead")
		misled = text.count("misled")													
		logging.info("%d,option %d,spin-off %d,spinoff %d,spin off %d,spun-off %d,spunoff %d,spun off %d,insider %d,divest %d,fraud %d,call %d,put %d,pyramid %d,mislead %d,misled %d" % (case, option, spindashoff, spinoff, spinspaceoff, spundashoff, spunoff, spunspaceoff, insider, divest, fraud, call, put, pyramid, mislead, misled))
		print(case)
		case += 1	
while case <= ohnine:
	try:
		urllib.request.urlopen(url2 + "2009/lr" + str(case) + suffix)
	except urllib.error.URLError:
		case += 1
	else:
		text = BeautifulSoup(urllib.request.urlopen(url2 + "2009/lr" + str(case) + suffix)).get_text().lower()
		option = text.count("option")
		spindashoff = text.count("spin-off")
		spinoff = text.count("spinoff")
		spinspaceoff = text.count("spin off")	
		spundashoff = text.count("spun-off")
		spunoff = text.count("spunoff")
		spunspaceoff = text.count("spun off")
		insider = text.count("insider")
		divest = text.count("divest")
		fraud = text.count("fraud")
		call = text.count("call")
		put = text.count("put")
		pyramid = text.count("pyramid")
		mislead = text.count("mislead")
		misled = text.count("misled")													
		logging.info("%d,option %d,spin-off %d,spinoff %d,spin off %d,spun-off %d,spunoff %d,spun off %d,insider %d,divest %d,fraud %d,call %d,put %d,pyramid %d,mislead %d,misled %d" % (case, option, spindashoff, spinoff, spinspaceoff, spundashoff, spunoff, spunspaceoff, insider, divest, fraud, call, put, pyramid, mislead, misled))
		print(case)
		case += 1	
while case <= ten:
	try:
		urllib.request.urlopen(url2 + "2010/lr" + str(case) + suffix)
	except urllib.error.URLError:
		case += 1
	else:
		text = BeautifulSoup(urllib.request.urlopen(url2 + "2010/lr" + str(case) + suffix)).get_text().lower()
		option = text.count("option")
		spindashoff = text.count("spin-off")
		spinoff = text.count("spinoff")
		spinspaceoff = text.count("spin off")	
		spundashoff = text.count("spun-off")
		spunoff = text.count("spunoff")
		spunspaceoff = text.count("spun off")
		insider = text.count("insider")
		divest = text.count("divest")
		fraud = text.count("fraud")
		call = text.count("call")
		put = text.count("put")
		pyramid = text.count("pyramid")
		mislead = text.count("mislead")
		misled = text.count("misled")													
		logging.info("%d,option %d,spin-off %d,spinoff %d,spin off %d,spun-off %d,spunoff %d,spun off %d,insider %d,divest %d,fraud %d,call %d,put %d,pyramid %d,mislead %d,misled %d" % (case, option, spindashoff, spinoff, spinspaceoff, spundashoff, spunoff, spunspaceoff, insider, divest, fraud, call, put, pyramid, mislead, misled))
		print(case)
		case += 1	
while case <= eleven:
	try:
		urllib.request.urlopen(url2 + "2011/lr" + str(case) + suffix)
	except urllib.error.URLError:
		case += 1
	else:
		text = BeautifulSoup(urllib.request.urlopen(url2 + "2011/lr" + str(case) + suffix)).get_text().lower()
		option = text.count("option")
		spindashoff = text.count("spin-off")
		spinoff = text.count("spinoff")
		spinspaceoff = text.count("spin off")	
		spundashoff = text.count("spun-off")
		spunoff = text.count("spunoff")
		spunspaceoff = text.count("spun off")
		insider = text.count("insider")
		divest = text.count("divest")
		fraud = text.count("fraud")
		call = text.count("call")
		put = text.count("put")
		pyramid = text.count("pyramid")
		mislead = text.count("mislead")
		misled = text.count("misled")													
		logging.info("%d,option %d,spin-off %d,spinoff %d,spin off %d,spun-off %d,spunoff %d,spun off %d,insider %d,divest %d,fraud %d,call %d,put %d,pyramid %d,mislead %d,misled %d" % (case, option, spindashoff, spinoff, spinspaceoff, spundashoff, spunoff, spunspaceoff, insider, divest, fraud, call, put, pyramid, mislead, misled))
		print(case)
		case += 1	
while case <= twelve:
	try:
		urllib.request.urlopen(url2 + "2012/lr" + str(case) + suffix)
	except urllib.error.URLError:
		case += 1
	else:
		text = BeautifulSoup(urllib.request.urlopen(url2 + "2012/lr" + str(case) + suffix)).get_text().lower()
		option = text.count("option")
		spindashoff = text.count("spin-off")
		spinoff = text.count("spinoff")
		spinspaceoff = text.count("spin off")	
		spundashoff = text.count("spun-off")
		spunoff = text.count("spunoff")
		spunspaceoff = text.count("spun off")
		insider = text.count("insider")
		divest = text.count("divest")
		fraud = text.count("fraud")
		call = text.count("call")
		put = text.count("put")
		pyramid = text.count("pyramid")
		mislead = text.count("mislead")
		misled = text.count("misled")													
		logging.info("%d,option %d,spin-off %d,spinoff %d,spin off %d,spun-off %d,spunoff %d,spun off %d,insider %d,divest %d,fraud %d,call %d,put %d,pyramid %d,mislead %d,misled %d" % (case, option, spindashoff, spinoff, spinspaceoff, spundashoff, spunoff, spunspaceoff, insider, divest, fraud, call, put, pyramid, mislead, misled))
		print(case)
		case += 1
while case <= thirteen:
	try:
		urllib.request.urlopen(url2 + "2013/lr" + str(case) + suffix)
	except urllib.error.URLError:
		case += 1
	else:
		text = BeautifulSoup(urllib.request.urlopen(url2 + "2013/lr" + str(case) + suffix)).get_text().lower()
		option = text.count("option")
		spindashoff = text.count("spin-off")
		spinoff = text.count("spinoff")
		spinspaceoff = text.count("spin off")	
		spundashoff = text.count("spun-off")
		spunoff = text.count("spunoff")
		spunspaceoff = text.count("spun off")
		insider = text.count("insider")
		divest = text.count("divest")
		fraud = text.count("fraud")
		call = text.count("call")
		put = text.count("put")
		pyramid = text.count("pyramid")
		mislead = text.count("mislead")
		misled = text.count("misled")													
		logging.info("%d,option %d,spin-off %d,spinoff %d,spin off %d,spun-off %d,spunoff %d,spun off %d,insider %d,divest %d,fraud %d,call %d,put %d,pyramid %d,mislead %d,misled %d" % (case, option, spindashoff, spinoff, spinspaceoff, spundashoff, spunoff, spunspaceoff, insider, divest, fraud, call, put, pyramid, mislead, misled))
		print(case)
		case += 1	
while case <= fourteen:
	try:
		urllib.request.urlopen(url2 + "2014/lr" + str(case) + suffix)
	except urllib.error.URLError:
		case += 1
	else:
		text = BeautifulSoup(urllib.request.urlopen(url2 + "2014/lr" + str(case) + suffix)).get_text().lower()
		option = text.count("option")
		spindashoff = text.count("spin-off")
		spinoff = text.count("spinoff")
		spinspaceoff = text.count("spin off")	
		spundashoff = text.count("spun-off")
		spunoff = text.count("spunoff")
		spunspaceoff = text.count("spun off")
		insider = text.count("insider")
		divest = text.count("divest")
		fraud = text.count("fraud")
		call = text.count("call")
		put = text.count("put")
		pyramid = text.count("pyramid")
		mislead = text.count("mislead")
		misled = text.count("misled")													
		logging.info("%d,option %d,spin-off %d,spinoff %d,spin off %d,spun-off %d,spunoff %d,spun off %d,insider %d,divest %d,fraud %d,call %d,put %d,pyramid %d,mislead %d,misled %d" % (case, option, spindashoff, spinoff, spinspaceoff, spundashoff, spunoff, spunspaceoff, insider, divest, fraud, call, put, pyramid, mislead, misled))
		print(case)
		case += 1		
logging.info("DONE!")