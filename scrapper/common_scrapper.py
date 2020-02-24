from urllib.request import urlretrieve
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from methods import Methods as m
import os


html = urlopen("https://yandex.ru/images/search?from=tabbar&text=балетки%20женские").decode('utf-8')
print(html.read().decode('utf-8'))
#bsObj = BeautifulSoup(html, "html.parser")

#
# j = 1
# for link in bsObj.find("div", {"class":"serp-controller__content"}).find("div", {"class":"serp-list"}).findAll("div", {"class":"serp-item"}):
#     img_link = link.find("div", {"class": "serp-item__preview"}).find("a", {"class": "serp-item__link"})
#     print(str(img_link.attrs['href']))

    # if 'data-gallery' in link.attrs:
    #     category_link = link.attrs['data-gallery'].strip('[').strip(']').strip('"')
    #     r = category_link.split('" , "')
    #     for i in range(len(r)):
    #         urlretrieve('https:'+r[i], m.getImagesDir()+'Yandex/Балетки/Балетки'+'.'+str(j)+'.jpeg')
    #     j += 1
    # else:
    #     print(link.attrs)
    #     raise
