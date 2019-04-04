import pysitemap

def parse():
	lit = []
	with open("sitemap.xml") as sm:
		for i in sm:
			if "http://" in i:
				lit.append(i[7:len(i)-7])
	with open("siteURL.csv","w")as out:
		for i in lit:
			out.write(i + "\r\n")




#    url = 'http://www.example.com/'  # url from to crawl
#    logfile = 'errlog.log'  # path to logfile
#    oformat = 'xml'  # output format

def newSite(url, logfile, oformat):
	crawl = pysitemap.Crawler(url=url, logfile=logfile, oformat=oformat, outputfile="autodata.a")
	crawl.crawl(echo=True)#pool_size=8)

newSite("https://www.auto-data.net/","autodata.log","xml")
