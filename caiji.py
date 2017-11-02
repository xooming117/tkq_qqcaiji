#!/usr/bin/env python3

import re
from mongodb1 import *

def get_goods_url(url):
    urls = re.findall('http.+\r\n', url)
    if len(urls) == 2:
        urls[0] = urls[0].strip('\r\n')
        urls[1] = urls[1].strip('\r\n')
        #丢弃短连接
        if urls[1].find('click') > 0:
            return 0, urls
        else:
            return 1, urls
    else:
        return 0, urls

def save(text):
    status, urls = get_goods_url(text)
    if status == 1:
        save_caiji_goods(urls)