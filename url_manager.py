#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
import os
import os.path
import json
import random
import requests
import threading
import logging
import time

import html_parser
import html_downloader

crawed_file = 'crawed_urls.txt'

class UrlManager():
    
    def __init__(self):
        self.lock = threading.Lock()
        self.parser = html_parser.HtmlParser()
        self.downloader = html_downloader.HtmlDownloader()
        self.base_url = 'https://mp.weixin.qq.com/mp/homepage?__biz=MzI5OTc5MTMxOA==&hid=2&sn=5ab2f67da2c0ca552463e88b1a53af4f&scene=18&cid={}&begin=0&count={}&action=appmsg_list&f=json&r={}'
        self.file_url = 'https://res.wx.qq.com/voice/getvoice?mediaid={}'
        self.urls = set() # storage file title, link

        self.crawed_urls = self.get_crawed_urls()
        self.articles = self.get_articles(cid = 1)
        self.craw_real_urls()

    def get_crawed_urls(self):
        '''
        from file get carwed urls
        '''
        if os.path.exists(crawed_file):
            with open(crawed_file) as f:
                urls = set()
                for url in f:
                    url = url.strip('\n')
                    urls.add(url)
                return urls
        else:
            logging.info('can\'t find {} file'.format(crawed_file))
            return set()

    def get_articles(self, cid = 0, count = 100):
        '''
        from base url get article page url
        '''
        url = self.base_url.format(cid, count, random.random())
        res = requests.post(url)
        json_data = res.json()
        tmp = set()
        for model in json_data['appmsg_list']:
            tmp.add((model['title'], model['link']))
            logging.info((model['title'], model['link']))
        return tmp

    def craw_real_urls(self):
        '''
        get real urls
        '''
        while len(self.articles):
            article = self.articles.pop()
            article_content = self.downloader.download_article(article[1])
            article_id = self.parser.parse_id(article_content)
            url = self.file_url.format(article_id)
            if url in self.crawed_urls:
                logging.info('file: {} has been downloaded, skip...'.format(article[0]))
                time.sleep(3)
                continue
            self.urls.add((article[0], self.file_url.format(article_id)))
            logging.info((article[0], article_id))
            time.sleep(3)

    def write_url(self, url):
        '''
        write crawed url to file
        '''
        with self.lock:
            with open(crawed_file, 'a+') as f:
                f.write('{}\n'.format(url))
