import requests
from bs4 import BeautifulSoup
import time

class Main():
    def __init__(self, dicts, shell, title, link, price, date):
        self.dict = dicts
        self.shell = shell
        self.title = title
        self.link = link
        self.price = price 
        self.date = date






# getting all ours links
    def takeLinks(self):
        self.links = []
        for i in self.dict:
            self.links.append(self.dict[i])
        print(self.links)

    def main(self):
        # folder name
        self.folderName = 'output'
        y = 0
        z = 0



        for i in range(0 , len(self.links)):
            # first page link
            url = self.links[i]
            # 
            r = requests.get(url)
            html = BeautifulSoup(r.content, "html.parser")
            pag = html.find('span', attrs={
                "class": "totalcount"
            })
            spug = int(int(pag.text)/120)
            print(spug)
            #
            print(self.links[i])
            # open file.txt
            f = open('out'+ str(y)+'.txt','w', encoding="utf-8")
            y+=1


            for r in range(spug):
                pages = (requests.get(url+str("?s="+str(0+ z))))
                z += 120
                bhtml = BeautifulSoup(pages.content,"html.parser")
                print(url+str("?s="+str(0+ z)))
                for el in bhtml.select(self.shell):
                    #take all data's
                    title = el.select(self.title)
                    link = el.select(self.title)
                    price = el.select(self.price)
                    date = el.select(self.date)

                    # write all this in txt file
                    
                    f.write(date[0].text)
                    f.write('---')
                    f.write(title[0].text)
                    f.write(' --- ')
                    f.write(price[0].text)
                    f.write(' --- ')
                    f.write(link[0].get('href'))
                    f.write('\n')

            # close file    
            f.close()
