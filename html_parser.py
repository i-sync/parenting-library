#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import re

class HtmlParser():
    
    def __init__(self):
        self.RE_ID_PATTERN = re.compile('<mpvoice.*voice_encode_fileid="([a-zA-Z0-9]*)".*></mpvoice>')
    
    def parse(self):
        pass

    def parse_id(self, html_content):
        result = self.RE_ID_PATTERN.search(html_content)
        if result:
            return result.group(1)
