#coding=utf-8

import pymongo
from pymongo import MongoClient


# 连接mongodb数据库
client = MongoClient('mongodb://mongodb:27017/')
# 指定数据库名称
db = client.tbk_database
# 获取非系统的集合
db.collection_names(include_system_collections=False)
print (db.collection_names())

def save_caiji_goods(goods):
    c = db.cai
    c.insert({'quan_url':goods[0],'good_url':goods[1], 'status':0})




