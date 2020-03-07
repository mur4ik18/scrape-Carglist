import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook 
# my second files imports:
import scrapFirstPage
import main 
import datetime
 
currentDT = datetime.datetime.now()
 
print (currentDT.strftime("%d-%m-%H:%M:%S"))
date = currentDT.strftime("%d-%m-%H-%M")

workbook = Workbook()
sheet = workbook.active

# Our variables for start page
url = "https://sfbay.craigslist.org/"
shell = ".housing > #sss"
link = "a"
linkText = "span"

# Our variabels for every page 

Pshell = 'li.result-row'
Ptitle = 'a.result-title'
Plink = 'a.result-title'
Pprice = 'span.result-price'
Pdate = '.result-date'










dicti = {}

FirstPage = scrapFirstPage.PageScrap(url, shell, link, linkText)
FirstPage.connect()
dicti = FirstPage.scrap()

main = main.Main(dicti, Pshell, Ptitle, Plink, Pprice, Pdate, date)
main.takeLinks()
main.main()