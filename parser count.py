# Written for Python 3.x
# Requires BeutifulSoup (bs4)
from bs4 import BeautifulSoup
from collections import Counter
import urllib.request, urllib.error, logging
logging.basicConfig(filename='parser.log',level=logging.INFO)
#2006 and on have /year/ after /litreleases/
url = "http://www.sec.gov/litigation/litreleases/lr"
case = 14644
#is actually 23129
newestcase = 19516
suffix = ".htm"
suffix2 = ".txt"
search = "options"
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
print("DONE!")