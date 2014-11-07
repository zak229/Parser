from bs4 import BeautifulSoup
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
	try:
		urllib.request.urlopen(url + str(case) + suffix)
	except urllib.error.URLError:
		try:
			urllib.request.urlopen(url + str(case) + suffix2)
		except urllib.error.URLError:
			case += 1
		else:
			soup = BeautifulSoup(urllib.request.urlopen(url + str(case) + suffix2))
			if search in soup.get_text():
				print(str(case) + " has " + search) 
				logging.info(str(case) + " has " + search)
				case += 1
			else:
				print(str(case) + " No")
				case += 1				
	else:
		soup = BeautifulSoup(urllib.request.urlopen(url + str(case) + suffix))
		if search in soup.get_text():
			print(str(case) + " has " + search)
			logging.info(str(case) + " has " + search)
			case += 1
		else:
			print(str(case) + " No")
			case += 1
