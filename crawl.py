import requests
from bs4 import BeautifulSoup
r=requests.get("http://midas.iiitd.edu.in/")
soup=BeautifulSoup(r.content)
print(soup.prettify())
#For Paragraphs i.e. Texts
soup.find_all("p")
for paragraph in soup.find_all("p"):
    print(paragraph.text)
print("\n\n\n")
#For Image Links
for image in soup.find_all("img"):
    print(image.get('src'))
 print("\n\n\n")
#For Web Links   
for link in soup.find_all("a"):
    print("<a href='%s'>%s</a>"%(link.get("href"), link.text))

    