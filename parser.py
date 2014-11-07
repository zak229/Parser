from bs4 import BeautifulSoup
import urllib.request, urllib.error, logging
logging.basicConfig(filename='parser.log',level=logging.INFO)
#2006 and on have /year/ after /litreleases/
url = "http://www.sec.gov/litigation/litreleases/lr"
# First Case with .htm
case = 16397
#is actually 23129
newestcase = 17000
suffix = ".htm"
suffix2 = ".txt"
while case <= newestcase:
	soup = BeautifulSoup(urllib.request.urlopen(url + str(case) + suffix))
	if "options" in soup.get_text():
		print(soup.title)
		logging.info(soup.title)
		case += 1
	else:
		print(str(case) + " No")
		case += 1
