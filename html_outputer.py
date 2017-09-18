#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import os.path

class HtmlOutputer():

    def output_file(self, title, file_content):
        file_name = r'files/{}.mp3'.format(title.replace('|', ''))
        if os.path.exists(file_name):
            os.remove(file_name)
        with open(file_name, 'wb') as f:
            f.write(file_content)
