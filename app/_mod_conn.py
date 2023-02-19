import pymysql
import os
from app import app

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
FILE_CONFIG = os.path.join(APP_ROOT, 'config.cfg')

def connectdb():
   file = str(os.path.isfile(FILE_CONFIG))
   if file == 'True':
      lines = open(FILE_CONFIG, "r").readlines()
      dbhost = lines[4].split("=")[1].replace("'", "").replace("\n", "")
      dbname = lines[5].split("=")[1].replace("'", "").replace("\n", "")
      connection = pymysql.connect(host='localhost', user='root', password='', db='patrol', charset='utf8mb4')

   else:
      dbhost = ''
      dbname = ''
      connection = ''
   return connection

