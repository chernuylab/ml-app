from urllib.request import urlopen
from methods import Methods as m
import os


print(m.parseXml(os.getcwd()+'/code/xml/lamoda.xml'))
