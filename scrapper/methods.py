import os
import errno
import xml.etree.cElementTree as element


class Methods:

    def make_sure_path_exists(path):
        try:
            os.mkdir(os.getcwd()+'/code/images/'+path, 0o777)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise

    def parseXml(xmlFile):
        directory = list()
        tree = element.ElementTree(file=xmlFile)
        root = tree.getroot()
        children = root.getchildren()
        for child in children:
            ch = child.getchildren()
            if ch[0].text is not None:
                directory.append(ch[0].text)
        return directory
