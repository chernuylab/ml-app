from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
from methods import Methods as m

path = "Балетки" // путь будет выбираться из каждой секции xml-фида и сопостовляться с категорией
m.make_sure_path_exists(path)

html = urlopen("https://www.lamoda.ru/c/37/shoes-baletki/")
bsObj = BeautifulSoup(html, "html.parser")

j = 1
for link in bsObj.find("div", {"class":"products-catalog__list"}).findAll("div", {"class":"products-list-item"}):
    if 'data-gallery' in link.attrs:
        result = link.attrs['data-gallery'].strip('[').strip(']').strip('"')
        r = result.split('" , "')
        for i in range(len(r)):
            urlretrieve('https:'+r[i], path+'/'+path+'.'+str(j)+'.'+str(i)+'.jpeg')
        j += 1
