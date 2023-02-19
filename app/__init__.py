from flask import Flask
from flask_compress import Compress
import os

import config

# app = Flask(__name__)
# COMPRESS_MIMETYPES = ['text/html', 'text/css', 'aplication/json']
# COMPRESS_LEVEL = 6
# COMPRESS_MIN_SIZE = 500
# Compress(app)


app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = '/static/uploads/'
STORE_UPLOAD = '/static/img/rad/'
app.config['APP_ROOT'] = APP_ROOT
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['STORE_UPLOAD'] = STORE_UPLOAD
ALLOWED_EXTENSIONS = set(['xls', 'text', 'csv', 'ods', 'xlsx'])
COMPRESS_MIMETYPES = ['text/html', 'text/css', 'aplication/json']
COMPRESS_LEVEL = 6
COMPRESS_MIN_SIZE = 500
Compress(app)

# Master
# from app import _route, _route_menu, _route_searching
from app import _route,_route_qustion,_route_patrol,_route_user
# from app import _route_users
# from app import _route_otoritas
# Transaksi Penjualan & TTB & Quarantine
# from app import _route_jual,_route_ttb,_routetagihanpiutang,_route_kas,_route_quarantine

app.config.from_pyfile(os.path.join(".", "config.cfg"), silent=False)
app.secret_key = app.config.get('SECRET_KEY')
app.jinja_env.auto_reload = True