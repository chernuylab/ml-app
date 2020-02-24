from urllib.request import urlretrieve
from urllib.request import urlopen
from urllib.parse import quote
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from methods import Methods as m
import os


path = 'https://yandex.ru'
m.make_sure_path_exists('Yandex')
html = urlopen(path+'/images/search?from=tabbar&text='+quote('балетки%20женские'))
bsObj = BeautifulSoup(html, "html.parser")

j = 1
for link in bsObj.find("div", {"class":"serp-controller__content"}).find("div", {"class":"serp-list"}).findAll("div", {"class":"serp-item"}):
    img_link = link.find("div", {"class": "serp-item__preview"}).find("a", {"class": "serp-item__link"}).find("img", {"class": "serp-item__thumb"})

    m.make_sure_path_exists('Yandex/Балетки')
    if 'src' in img_link.attrs:
        #print('https:'+img_link.attrs['src'])
        for i in range(0-999):
            print('https:'+img_link.attrs['src'], m.getImagesDir()+'Yandex/Балетки/Балетки'+'.'+str(j)+'.jpg')
            j += 1
    # if 'data-gallery' in link.attrs:
    #     category_link = link.attrs['data-gallery'].strip('[').strip(']').strip('"')
    #     r = category_link.split('" , "')
    #     for i in range(len(r)):
    #         urlretrieve('https:'+r[i], m.getImagesDir()+'Yandex/Балетки/Балетки'+'.'+str(j)+'.jpeg')
    #     j += 1
    # else:
    #     print(link.attrs)
    #     raise
