lit = []
with open("sitemap.xml") as sm:
	for i in sm:
		if "http://" in i:
			lit.append(i[7:len(i)-7])
with open("siteURL","w")as out:
	for i in lit:
		out.write(i + "\r\n")

