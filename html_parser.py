# encoding=utf-8
from bs4 import BeautifulSoup
import re
import urllib.parse as urlparse

class HtmlParser(object):
    def parser(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return None
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data
    def _get_new_urls(self,page_url,soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/piclist3/[0-9]*.html"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls
    def _get_new_data(self,page_url,soup):
        res_data = {}
        lst = []
        title_node= soup.find('div',class_="n_bd").find_all('img')
        for node in title_node:
            #print ('craw %s url:%s' % (node['alt'],node['src'])) 
            lst.append(node['src'])
            res_data['alt']=node['alt']
        res_data['lst']=lst
        return res_data