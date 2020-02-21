from urllib.request import urlretrieve
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from methods import Methods as m
import os

paths = m.parseXml(os.getcwd()+'/code/xml/lamoda.xml')

for path in paths:
    m.make_sure_path_exists(path.split('/')[5])
    html = urlopen(path)
    bsObj = BeautifulSoup(html, "html.parser")

    j = 1
    try:
        for link in bsObj.find("div", {"class":"products-catalog__list"}).findAll("div", {"class":"products-list-item"}):
            if 'data-gallery' in link.attrs:
                result = link.attrs['data-gallery'].strip('[').strip(']').strip('"')
                r = result.split('" , "')
                for i in range(len(r)):
                    print('https:'+r[i], path.split('/')[5]+'.'+str(j)+'.'+str(i)+'.jpeg')
                j += 1
    except HTTPError as err:
        if err.code == 404:
            pass
