import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook 
import datetime
# my second files imports:
import scrapFirstPage
import main 

# date right now 
currentDT       = datetime.datetime.now()
# print time
print (currentDT.strftime("%d-%m-%H:%M:%S"))
# write time now
date            = currentDT.strftime("%d-%m-%H-%M-%S")
# excel variabels
workbook        = Workbook()
# vkladka 
sheet           = workbook.active

# Our variables for start page
url             = "https://sfbay.craigslist.org/"   # global site
shell           = ".housing > #sss"                 # shell 
link            = "a"                               # category link
linkText        = "span"                            # category name
# Our variabels for every page 
Pshell          = 'li.result-row'                   # shell
Ptitle          = 'a.result-title'                  # title
Plink           = 'a.result-title'                  # link
Pprice          = 'span.result-price'               # price
Pdate           = '.result-date'                    # date 

# dictionari for categories : links
dicti           = {}
# first page scraping  
FirstPage       = scrapFirstPage.PageScrap(url, shell, link, linkText)
FirstPage.connect()
dicti           = FirstPage.scrap()
# scraping all all pages what we have in dicti
main            = main.Main(dicti, Pshell, Ptitle, Plink, Pprice, Pdate, date)
main.takeLinks()
main.main()

print("scraping complate")