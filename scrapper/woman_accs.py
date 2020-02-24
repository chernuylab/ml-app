from urllib.request import urlretrieve
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from methods import Methods as m
import os


path = 'https://www.lamoda.ru'
m.make_sure_path_exists('woman_accs')
html = urlopen(path+'/c/557/accs-zhenskieaksessuary/')
bsObj1 = BeautifulSoup(html, "html.parser")

try:
    for link in bsObj1.find("ul", {"class":"cat-nav dt102_1"}).find("ul", {"class":"cat-nav cat-nav-sub dt102_2"}).findAll("li", {"class":"cat-nav-item dt102_li2"}):
        result = link.find("a", {"class":"link"})

        m.make_sure_path_exists('woman_accs/'+result.contents[0])
        category_html = urlopen(path+result.attrs['href'])
        bsObj2 = BeautifulSoup(category_html, "html.parser")

        j = 1
        for link in bsObj2.find("div", {"class":"products-catalog__list"}).findAll("div", {"class":"products-list-item"}):
            if 'data-gallery' in link.attrs:
                category_link = link.attrs['data-gallery'].strip('[').strip(']').strip('"')
                r = category_link.split('" , "')
                for i in range(len(r)):
                    urlretrieve('https:'+r[i], m.getImagesDir()+'woman_accs/'+result.contents[0]+'/'+result.contents[0]+'.'+str(j)+'.'+str(i)+'.jpeg')
                j += 1
            else:
                print(link.attrs)
                raise
        # print("Ссылка: "+path+result.attrs['href'])
        # print("Категория: "+str(result.contents[0]))
except Exception as e:
    print('Тут произошла ошибка: '+str(e)+' ссылка: '+path+result.attrs['href'])
