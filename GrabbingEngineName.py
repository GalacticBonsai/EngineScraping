# import libraries
from bs4 import BeautifulSoup as soup
import requests

# urls to grab
urls = []

# variables I care about
varList = ["Also called","Configuration","Production",
           # "Cylinder block alloy",
           "Piston stroke, mm (inch)","Cylinder bore, mm (inch)",
           "Compression ratio","Displacement",
           "Power output","Torque output","Redline"]
database = []


def get_urls():
    with open("siteURL.csv") as URL:
        for i in URL:
            urls.append(i)
    #print urls
# wget


def get_data():
    for url in urls:
        uClient = requests.get(url.rstrip())
        page_html = uClient.text
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
                print(varDict)
                database.append(varDict)



def print_data():
    with open("database.csv","w+") as db:
        db.write("Engine Name; Configuration; Years; Stroke; Bore; Compression Ratio; Displacement; Horsepower; Torque; Redline")
        for i in database:
            print("----engine----")
            #db.write("----engine----\r\n")
            db.write(i["Also called"] +"; "+
                    i["Configuration"]+"; "+
                    i["Production"] +"; "+
                    i["Piston stroke, mm (inch)"]+"; "+
                    i["Cylinder bore, mm (inch)"]+"; "+
                    i["Compression ratio"] + "; "+
                    i["Displacement"] + "; "+
                    i["Power output"] + "; "+
                    i["Torque output"] + "; "+
                    i["Redline"] +
                    "\r\n")

def main():
    get_urls()
    get_data()
    print_data()


#main()

