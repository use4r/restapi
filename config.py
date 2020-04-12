# config.py
# файл конфигурации

from pymongo import MongoClient

DATABASE = MongoClient()['sys_eng_restapi']  # имя базы
DEBUG = True
client = MongoClient('localhost', 27017)  # на 127.0.0.1 порт 27017
