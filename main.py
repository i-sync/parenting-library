#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import os
import os.path
import logging
logfile =os.path.join( os.path.dirname(os.path.abspath(__file__)), 'logs/spider.log')
logging.basicConfig(level = logging.INFO)

import json
import requests
import url_manager
import html_downloader
import html_outputer
import html_parser
import html_parser

'''
cid=0,1
begin=0,5,10,15,20,25,30

https://mp.weixin.qq.com/mp/homepage?__biz=MzI5OTc5MTMxOA==&hid=2&sn=5ab2f67da2c0ca552463e88b1a53af4f&scene=18&cid=0&begin=5&count=5&action=appmsg_list&f=json&r=0.7179149502113482


voice_encode_fileid="MzI5OTc5MTMxOF8yMjQ3NDg3NTAx"
'''

def start():
    list_url = ''
    file_url = 'https://res.wx.qq.com/voice/getvoice?mediaid={}'

    id = 'MzI5OTc5MTMxOF8yMjQ3NDg3NTIw'

    mp3 = requests.get(file_url.format(id))
    with open('test.mp3', 'wb') as f:
        f.write(mp3.content)


class SpiderMain(object):

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    
    def craw(self):
        
        while len(self.urls):
            title, url = self.urls.pop()
            

if __name__ == '__main__':
    spider_main = SpiderMain()


