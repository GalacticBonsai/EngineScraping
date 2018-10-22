# import libraries
from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup

# urls to grab
urls = []

# variables I care about
varList = ["Also called",
           "Configuration",
           # "Cylinder block alloy",
           "Piston stroke, mm (inch)",
           "Cylinder bore, mm (inch)",
           "Compression ratio",
           "Displacement",
           "Power output",
           "Torque output",
           "Redline"]
database = []


def get_urls():
    with open("siteURL") as URL:
	for i in URL:
		urls.append(i)
    #print urls
# wget


def get_data():
    for url in urls:
        uClient = uReq(url)
        page_html = uClient.read()
        uClient.close()
        # turn html into object
        page_soup = soup(page_html, 'html.parser')

        # print page_soup.prettify()

        varDict = {}
        found = False
	anyres = False
        for i in page_soup.stripped_strings:
            if found is True:
                varDict[key] = i
                found = False
            elif i in varList:
                key = i
                found = True
		anyres = True
        if anyres is True:
		print varDict
		database.append(varDict)
	


def print_data():
    with open("database.csv","w+") as db:
	    for i in database:
		print "----engine----"
		for j in varList:
		    print j + " : " + i[j]
		#db.write("----engine----\r\n")
		db.write(i["Also called"].encode('utf-8') +"; " +
			i["Configuration"].encode('utf-8') +"; "+
			i["Piston stroke, mm (inch)"].encode('utf-8')+"; " +
			i["Cylinder bore, mm (inch)"].encode('utf-8')+"; " +
			i["Compression ratio"].encode('utf-8') + "; " +
			i["Displacement"].encode('utf-8') + "; "+
			i["Power output"].encode('utf-8') + "; "+
			i["Torque output"].encode('utf-8') + ", "+
			i["Redline"].encode('utf-8') +
			"\r\n")

def main():
    get_urls()
    get_data()
    print_data()


main()

