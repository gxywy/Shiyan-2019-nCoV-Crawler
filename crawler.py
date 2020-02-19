#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import time
import json
import requests
from datetime import datetime
from bs4 import BeautifulSoup

headers = {
            'DNT':'1',
            'Host':'www.shiyan.gov.cn',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
        }

def get_article():
    for i in range(10):
        page = str(i)
        if page != '0':
            page = '_' + page
        else:
            page = ''
        url = 'http://www.shiyan.gov.cn/xwzx_2477/syyw_2479/index' + page + '.shtml'

        req = requests.get(url, headers=headers)
        soup = BeautifulSoup(req.text, 'html.parser')
        articles = soup.findAll("div", {"class": "list_cloumn"})
        for article in articles:
            if article.find("a").get('alt').find('十堰市新冠肺炎疫情情况') != -1: #and article.find("p").get_text().find(input_date) != -1:
                return article.get('onclick')[13:][:-3]
        time.sleep(2)
    return None

def get_data(url):
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    content = soup.find("div", {"class": "display_text"}).get_text()
    
    content = content[content.find("累计"):]

    areas = [['病例'], ['出院'], ['病亡'], ['茅箭区'], ['张湾区'], ['丹江口市'], ['竹山县'], ['房县'], ['郧西县'], ['武当山特区'], ['郧阳区'], ['竹溪县'], ['十堰经济技术开发区']]
    for area in areas:
        pattern = re.compile(r'(?<=' + area[0] +')\d+\.?\d*')
        for num in pattern.findall(content):
            area.append(num)
            break
    
    return areas

if __name__ == '__main__':
    today_url = get_article()
    if today_url is not None:
        get_data(today_url)
    input()