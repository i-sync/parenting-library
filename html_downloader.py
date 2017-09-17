#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
import requests

class HtmlDownloader():
    

    def download(self, url):
        pass

    def download_article(self, url):

        if url is None:
            return url
        res = requests.get(url)
        return res.text