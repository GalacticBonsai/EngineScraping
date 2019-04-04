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
    for url in set(urls):
        uClient = requests.get(url.rstrip())
        page_html = uClient.text
#        print(uClient)        
# turn html into object
        page_soup = soup(page_html, 'html.parser')

        # print page_soup.prettify()

        varDict = {}
        found = False
        anyres = False
        for i in page_soup.stripped_strings:
            #print(i)
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
        db.write("Engine Name; Configuration; Years; Stroke; Bore; Compression Ratio; Displacement; Horsepower; Torque; Redline\n")
        for i in database:
            #print("----engine----")
            #db.write("----engine----\r\n")
            #db.write(";".join(i.values()).encode('utf-8').strip())
            #print(";".join(i.values()).encode('utf-8').strip())
            db.write(i["Also called"].encode('utf-8').strip() +"; "+
                    i["Configuration"].encode('utf-8').strip()+"; "+
                    i["Production"].encode('utf-8').strip() +"; "+
                    i["Piston stroke, mm (inch)"].encode('utf-8').strip()+"; "+
                    i["Cylinder bore, mm (inch)"].encode('utf-8').strip()+"; "+
                    i["Compression ratio"].encode('utf-8').strip() + "; "+
                    i["Displacement"].encode('utf-8').strip() + "; "+
                    i["Power output"].encode('utf-8').strip() + "; "+
                    i["Torque output"].encode('utf-8').strip() + "; "+
                    i["Redline"].encode('utf-8').strip() +
                    "\r\n")

def main():
    get_urls()
    get_data()
    #print_data()


if __name__ == "__main__":
    main()
    print_data()


