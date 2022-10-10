#web scraping with beautiful soap

from bs4 import BeautifulSoup

with open("Website.html") as file:
    contents=file.read()

soup =BeautifulSoup(contents,"html.parser")

print(soup.title)
print(soup.title.string)
print(soup.li)
print(soup.find_all(name="a"))
allanchortag=soup.find_all(name="a" )

for tag in allanchortag:
    print(tag.getText())
 

import requests
response= requests.get("https://news.ycombinator.com/")
soup=BeautifulSoup(response.text,"html.parser")

stories= soup.find_all(name='span',class_="titleline")


for tag in stories:
    print(tag.getText())
 