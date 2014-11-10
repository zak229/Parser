# Written for Python 3.x
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
#as of 11-10-14
fourteen = 23129
while case <= newestcase:
	option = 0
	spindashoff = 0
	spinoff = 0
	insider = 0
	divest = 0
	fraud = 0
	call = 0
	put = 0
	pyramid = 0
	misleading = 0
	try:
		urllib.request.urlopen(url + str(case) + suffix)
	except urllib.error.URLError:
		try:
			urllib.request.urlopen(url + str(case) + suffix2)
		except urllib.error.URLError:
			case += 1
		else:
			soup = BeautifulSoup(urllib.request.urlopen(url + str(case) + suffix2))
			text = soup.get_text().lower()
			option = text.count("option")
			spindashoff = text.count("spin-off")
			spinoff = text.count("spinoff")
			insider = text.count("insider")
			divest = text.count("divest")
			fraud = text.count("fraud")
			call = text.count("call")
			put = text.count("put")
			pyramid = text.count("pyramid")
			misleading = text.count("misleading")														
			logging.info("%d,option %d,spin-off %d,spinoff %d,insider %d,divest %d,fraud %d,call %d,put %d,pyramid %d,misleading %d" % (case, option, spindashoff, spinoff, insider, divest, fraud, call, put, pyramid, misleading))
			print(case)
			case += 1
	else:
		soup = BeautifulSoup(urllib.request.urlopen(url + str(case) + suffix))
		text = soup.get_text().lower()
		option = text.count("option")
		spindashoff = text.count("spin-off")
		spinoff = text.count("spinoff")
		insider = text.count("insider")
		divest = text.count("divest")
		fraud = text.count("fraud")
		call = text.count("call")
		put = text.count("put")
		pyramid = text.count("pyramid")
		misleading = text.count("misleading")														
		logging.info("%d,option %d,spin-off %d,spinoff %d,insider %d,divest %d,fraud %d,call %d,put %d,pyramid %d,misleading %d" % (case, option, spindashoff, spinoff, insider, divest, fraud, call, put, pyramid, misleading))
		print(case)
		case += 1
while case <= ohsix:
	option = 0
	spindashoff = 0
	spinoff = 0
	insider = 0
	divest = 0
	fraud = 0
	call = 0
	put = 0
	pyramid = 0
	misleading = 0
	try:
		urllib.request.urlopen(url2 + "2006/lr" + str(case) + suffix)
	except urllib.error.URLError:
		case += 1
	else:
		soup = BeautifulSoup(urllib.request.urlopen(url2 + "2006/lr" + str(case) + suffix))
		text = soup.get_text().lower()
		option = text.count("option")
		spindashoff = text.count("spin-off")
		spinoff = text.count("spinoff")
		insider = text.count("insider")
		divest = text.count("divest")
		fraud = text.count("fraud")
		call = text.count("call")
		put = text.count("put")
		pyramid = text.count("pyramid")
		misleading = text.count("misleading")														
		logging.info("%d,option %d,spin-off %d,spinoff %d,insider %d,divest %d,fraud %d,call %d,put %d,pyramid %d,misleading %d" % (case, option, spindashoff, spinoff, insider, divest, fraud, call, put, pyramid, misleading))
		print(case)
		case += 1	
while case <= ohseven:
	option = 0
	spindashoff = 0
	spinoff = 0
	insider = 0
	divest = 0
	fraud = 0
	call = 0
	put = 0
	pyramid = 0
	misleading = 0
	try:
		urllib.request.urlopen(url2 + "2007/lr" + str(case) + suffix)
	except urllib.error.URLError:
		case += 1
	else:
		soup = BeautifulSoup(urllib.request.urlopen(url2 + "2007/lr" + str(case) + suffix))
		text = soup.get_text().lower()
		option = text.count("option")
		spindashoff = text.count("spin-off")
		spinoff = text.count("spinoff")
		insider = text.count("insider")
		divest = text.count("divest")
		fraud = text.count("fraud")
		call = text.count("call")
		put = text.count("put")
		pyramid = text.count("pyramid")
		misleading = text.count("misleading")														
		logging.info("%d,option %d,spin-off %d,spinoff %d,insider %d,divest %d,fraud %d,call %d,put %d,pyramid %d,misleading %d" % (case, option, spindashoff, spinoff, insider, divest, fraud, call, put, pyramid, misleading))
		print(case)
		case += 1	
while case <= oheight:
	option = 0
	spindashoff = 0
	spinoff = 0
	insider = 0
	divest = 0
	fraud = 0
	call = 0
	put = 0
	pyramid = 0
	misleading = 0
	try:
		urllib.request.urlopen(url2 + "2008/lr" + str(case) + suffix)
	except urllib.error.URLError:
		case += 1
	else:
		soup = BeautifulSoup(urllib.request.urlopen(url2 + "2008/lr" + str(case) + suffix))
		text = soup.get_text().lower()
		option = text.count("option")
		spindashoff = text.count("spin-off")
		spinoff = text.count("spinoff")
		insider = text.count("insider")
		divest = text.count("divest")
		fraud = text.count("fraud")
		call = text.count("call")
		put = text.count("put")
		pyramid = text.count("pyramid")
		misleading = text.count("misleading")														
		logging.info("%d,option %d,spin-off %d,spinoff %d,insider %d,divest %d,fraud %d,call %d,put %d,pyramid %d,misleading %d" % (case, option, spindashoff, spinoff, insider, divest, fraud, call, put, pyramid, misleading))
		print(case)
		case += 1	
while case <= ohnine:
	option = 0
	spindashoff = 0
	spinoff = 0
	insider = 0
	divest = 0
	fraud = 0
	call = 0
	put = 0
	pyramid = 0
	misleading = 0
	try:
		urllib.request.urlopen(url2 + "2009/lr" + str(case) + suffix)
	except urllib.error.URLError:
		case += 1
	else:
		soup = BeautifulSoup(urllib.request.urlopen(url2 + "2009/lr" + str(case) + suffix))
		text = soup.get_text().lower()
		option = text.count("option")
		spindashoff = text.count("spin-off")
		spinoff = text.count("spinoff")
		insider = text.count("insider")
		divest = text.count("divest")
		fraud = text.count("fraud")
		call = text.count("call")
		put = text.count("put")
		pyramid = text.count("pyramid")
		misleading = text.count("misleading")														
		logging.info("%d,option %d,spin-off %d,spinoff %d,insider %d,divest %d,fraud %d,call %d,put %d,pyramid %d,misleading %d" % (case, option, spindashoff, spinoff, insider, divest, fraud, call, put, pyramid, misleading))
		print(case)
		case += 1	
while case <= ten:
	option = 0
	spindashoff = 0
	spinoff = 0
	insider = 0
	divest = 0
	fraud = 0
	call = 0
	put = 0
	pyramid = 0
	misleading = 0
	try:
		urllib.request.urlopen(url2 + "2010/lr" + str(case) + suffix)
	except urllib.error.URLError:
		case += 1
	else:
		soup = BeautifulSoup(urllib.request.urlopen(url2 + "2010/lr" + str(case) + suffix))
		text = soup.get_text().lower()
		option = text.count("option")
		spindashoff = text.count("spin-off")
		spinoff = text.count("spinoff")
		insider = text.count("insider")
		divest = text.count("divest")
		fraud = text.count("fraud")
		call = text.count("call")
		put = text.count("put")
		pyramid = text.count("pyramid")
		misleading = text.count("misleading")														
		logging.info("%d,option %d,spin-off %d,spinoff %d,insider %d,divest %d,fraud %d,call %d,put %d,pyramid %d,misleading %d" % (case, option, spindashoff, spinoff, insider, divest, fraud, call, put, pyramid, misleading))
		print(case)
		case += 1	
while case <= eleven:
	option = 0
	spindashoff = 0
	spinoff = 0
	insider = 0
	divest = 0
	fraud = 0
	call = 0
	put = 0
	pyramid = 0
	misleading = 0
	try:
		urllib.request.urlopen(url2 + "2011/lr" + str(case) + suffix)
	except urllib.error.URLError:
		case += 1
	else:
		soup = BeautifulSoup(urllib.request.urlopen(url2 + "2011/lr" + str(case) + suffix))
		text = soup.get_text().lower()
		option = text.count("option")
		spindashoff = text.count("spin-off")
		spinoff = text.count("spinoff")
		insider = text.count("insider")
		divest = text.count("divest")
		fraud = text.count("fraud")
		call = text.count("call")
		put = text.count("put")
		pyramid = text.count("pyramid")
		misleading = text.count("misleading")														
		logging.info("%d,option %d,spin-off %d,spinoff %d,insider %d,divest %d,fraud %d,call %d,put %d,pyramid %d,misleading %d" % (case, option, spindashoff, spinoff, insider, divest, fraud, call, put, pyramid, misleading))
		print(case)
		case += 1	
while case <= twelve:
	option = 0
	spindashoff = 0
	spinoff = 0
	insider = 0
	divest = 0
	fraud = 0
	call = 0
	put = 0
	pyramid = 0
	misleading = 0
	try:
		urllib.request.urlopen(url2 + "2012/lr" + str(case) + suffix)
	except urllib.error.URLError:
		case += 1
	else:
		soup = BeautifulSoup(urllib.request.urlopen(url2 + "2012/lr" + str(case) + suffix))
		text = soup.get_text().lower()
		option = text.count("option")
		spindashoff = text.count("spin-off")
		spinoff = text.count("spinoff")
		insider = text.count("insider")
		divest = text.count("divest")
		fraud = text.count("fraud")
		call = text.count("call")
		put = text.count("put")
		pyramid = text.count("pyramid")
		misleading = text.count("misleading")														
		logging.info("%d,option %d,spin-off %d,spinoff %d,insider %d,divest %d,fraud %d,call %d,put %d,pyramid %d,misleading %d" % (case, option, spindashoff, spinoff, insider, divest, fraud, call, put, pyramid, misleading))
		print(case)
		case += 1
while case <= thirteen:
	option = 0
	spindashoff = 0
	spinoff = 0
	insider = 0
	divest = 0
	fraud = 0
	call = 0
	put = 0
	pyramid = 0
	misleading = 0
	try:
		urllib.request.urlopen(url2 + "2013/lr" + str(case) + suffix)
	except urllib.error.URLError:
		case += 1
	else:
		soup = BeautifulSoup(urllib.request.urlopen(url2 + "2013/lr" + str(case) + suffix))
		text = soup.get_text().lower()
		option = text.count("option")
		spindashoff = text.count("spin-off")
		spinoff = text.count("spinoff")
		insider = text.count("insider")
		divest = text.count("divest")
		fraud = text.count("fraud")
		call = text.count("call")
		put = text.count("put")
		pyramid = text.count("pyramid")
		misleading = text.count("misleading")														
		logging.info("%d,option %d,spin-off %d,spinoff %d,insider %d,divest %d,fraud %d,call %d,put %d,pyramid %d,misleading %d" % (case, option, spindashoff, spinoff, insider, divest, fraud, call, put, pyramid, misleading))
		print(case)
		case += 1	
while case <= fourteen:
	option = 0
	spindashoff = 0
	spinoff = 0
	insider = 0
	divest = 0
	fraud = 0
	call = 0
	put = 0
	pyramid = 0
	misleading = 0
	try:
		urllib.request.urlopen(url2 + "2014/lr" + str(case) + suffix)
	except urllib.error.URLError:
		case += 1
	else:
		soup = BeautifulSoup(urllib.request.urlopen(url2 + "2014/lr" + str(case) + suffix))
		text = soup.get_text().lower()
		option = text.count("option")
		spindashoff = text.count("spin-off")
		spinoff = text.count("spinoff")
		insider = text.count("insider")
		divest = text.count("divest")
		fraud = text.count("fraud")
		call = text.count("call")
		put = text.count("put")
		pyramid = text.count("pyramid")
		misleading = text.count("misleading")														
		logging.info("%d,option %d,spin-off %d,spinoff %d,insider %d,divest %d,fraud %d,call %d,put %d,pyramid %d,misleading %d" % (case, option, spindashoff, spinoff, insider, divest, fraud, call, put, pyramid, misleading))
		print(case)
		case += 1		
print("DONE!")