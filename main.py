import requests
import gzip
from xml.dom.minidom import parseString
import os


class ReadGZFile:
    def __init__(self, url):
        self.url = url

    def save_file(self):
        r = requests.get(self.url, allow_redirects=True)
        with open('item.gz', 'wb') as file:
            file.write(r.content)
            file.close()
        ReadGZFile.read_file()

    @staticmethod
    def read_file():
        infile = gzip.open("item.gz")
        content = infile.read()

        dom = parseString(content)
        print(dom.toxml())
        ReadGZFile.delete_file()

    @staticmethod
    def delete_file():
        os.system("rm item.gz")


if __name__ == '__main__':
    ReadGZFile(url='https://www.mynet.com/haber/sitemap/2019-07_2-newsweb.xml.gz').save_file()
