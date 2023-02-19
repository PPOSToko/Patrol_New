from flask import request, render_template, jsonify, Flask
import pathlib
import datetime
from werkzeug.utils import secure_filename
import os, shutil
from app import _mod_conn
import time

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
FILE_CONFIG = os.path.join(APP_ROOT, 'config.cfg')

class configs:
   @staticmethod
   def get_email_address():
      file = str(os.path.isfile(FILE_CONFIG))
      if file == 'True':
         lines = open(FILE_CONFIG, "r").readlines()
         email = lines[9].split("=")[1].replace("'","").replace("\n","")
      else:
         email = ''
      return email

   @staticmethod
   def get_website():
      file = str(os.path.isfile(FILE_CONFIG))
      if file == 'True':
         lines = open(FILE_CONFIG, "r").readlines()
         website = lines[10].split("=")[1].replace("'","").replace("\n","")
      else:
         website = ''
      return website

   @staticmethod
   def get_template_title():
      file = str(os.path.isfile(FILE_CONFIG))
      if file == 'True':
         lines = open(FILE_CONFIG, "r").readlines()
         template_title = lines[11].split("=")[1].replace("'","")
      else:
         template_title = ''
      return template_title

   @staticmethod
   def get_head_content():
      file = str(os.path.isfile(FILE_CONFIG))
      if file == 'True':
         lines = open(FILE_CONFIG, "r").readlines()
         hd_content = lines[12].split("=")[1].replace("'","").replace("\n","")
      else:
         hd_content = ''
      return hd_content

   @staticmethod
   def get_log_content():
      file = str(os.path.isfile(FILE_CONFIG))
      if file == 'True':
         lines = open(FILE_CONFIG, "r").readlines()
         log_content = lines[13].split("=")[1].replace("'","").replace("\n","")
      else:
         log_content = ''
      return log_content

   @staticmethod
   def get_config():
      lnk = request.form['link']
      file = str(os.path.isfile(FILE_CONFIG))
      if file == 'True':
         lines = open(FILE_CONFIG, "r").readlines()
         dbg = lines[1].split("=")[1].replace("\n","")
         env = lines[2].split("=")[1].replace("'","").replace("\n","")
         temp_reload = lines[3].split("=")[1].replace("\n","")
         dbhost = lines[4].split("=")[1].replace("'","").replace("\n","")
         dbname = lines[5].split("=")[1].replace("'","").replace("\n","")
         serv_name = lines[6].split("=")[1].replace("'","").replace("\n","")
         serv_port = lines[7].split("=")[1].replace("'","").replace("\n","")
         secret = lines[8].split("=")[1].replace("'","").replace("\n","")
         email = lines[9].split("=")[1].replace("'","").replace("\n","")
         website = lines[10].split("=")[1].replace("'","").replace("\n","")
         template_title = lines[11].split("=")[1].replace("'","").replace("\n","")
         hd_content = lines[12].split("=")[1].replace("'","").replace("\n","")
         log_content = lines[13].split("=")[1].replace("'","").replace("\n","")
         app_start = lines[43].split("=")[1].replace("'","").replace("\n","")
      else:
         dbg = 'False'
         env = ''
         temp_reload = 'False'
         dbhost = ''
         dbname = ''
         serv_name = ''
         serv_port = ''
         secret = ''
         email = ''
         website = ''
         template_title = ''
         hd_content = ''
         log_content = ''
         app_start = ''
      
      return render_template(lnk, dbg=dbg, env=env, temp_reload=temp_reload, dbhost=dbhost, dbname=dbname,\
               serv_name=serv_name, serv_port=serv_port, secret=secret, email=email, website=website,\
               template_title=template_title, hd_content=hd_content, log_content=log_content, app_start=app_start)
   
   @staticmethod
   def get_bankdata():
      file = str(os.path.isfile(FILE_CONFIG))
      if file == 'True':
         lines = open(FILE_CONFIG, "r").readlines()
         dbhost = lines[4].split("=")[1].replace("'","").replace("\n","")
         dbname = lines[5].split("=")[1].replace("'","").replace("\n","")
      return jsonify({'status':1, 'dbhost':dbhost, 'dbname':dbname})
   
   @staticmethod
   def simpan_bankdata():
      dbhost = request.form['dbhost']
      dbname = request.form['dbname']
      file = str(os.path.isfile(FILE_CONFIG))
      if file == 'True':
         try:
            lines = open(FILE_CONFIG, "r").readlines()
            lines[4] = "DB_HOST='"+dbhost+"'\n"
            lines[5] = "DB_NAME='"+dbname+"'\n"
            out = open(FILE_CONFIG, 'w')
            out.writelines(lines)
         except:
            return jsonify({'status':0})
         else:
            out.close()
            return jsonify({'status': 1})

   @staticmethod
   def update_config():
      debugs = request.form['debugs']
      env = request.form['env']
      temp_reload = request.form['temp_reload']
      dbhost = request.form['dbhost']
      dbname = request.form['dbname']
      serv_name = request.form['serv_name']
      serv_port = request.form['serv_port']
      secret = request.form['secret']
      email = request.form['email']
      website = request.form['website']
      template_title = request.form['template_title']
      hd_content = request.form['hd_content']
      log_content = request.form['log_content']
      app_start = request.form['app_start']
      file = str(os.path.isfile(FILE_CONFIG))
      if file == 'True':
         try:
            lines = open(FILE_CONFIG, "r").readlines()
            lines[1] = "DEBUG="+debugs+"\n"
            lines[2] = "ENV='"+env+"'\n"
            lines[3] = "TEMPLATES_AUTO_RELOAD="+temp_reload+"\n"
            lines[4] = "DB_HOST='"+dbhost+"'\n"
            lines[5] = "DB_NAME='"+dbname+"'\n"
            lines[6] = "SERVER_HOST='"+serv_name+"'\n"
            lines[7] = "SERVER_PORT="+serv_port+"\n"
            lines[8] = "SECRET_KEY='"+secret+"'\n"
            lines[9] = "EMAIL_ADDRESS='"+email+"'\n"
            lines[10] = "WEBSITE='"+website+"'\n"
            lines[11] = "TEMPLATE_TITLE='"+template_title+"'\n"
            lines[12] = "HEAD_CONTENT='"+hd_content+"'\n"
            lines[13] = "FRONT_CONTENT='"+log_content.replace("\n", " ")+"'\n"
            lines[43] = "APP_START='"+app_start.replace("\n", " ")+"'\n"
            out = open(FILE_CONFIG, 'w')
            out.writelines(lines)
         except:
            return jsonify({'status':0})
         else:
            out.close()
            return jsonify({'status': 1})

   @staticmethod
   def get_db():
      dblist = []
      conn = _mod_conn.connectdb()
      cur = conn.cursor()
      # cur.execute("SHOW TABLES WHERE tables_in_scb_default <> '_data_instansi' AND tables_in_scb_default <> '_mainmenu'\
      #             AND tables_in_scb_default <> '_menu' AND tables_in_scb_default <> '_isi_kamar'\
      #             AND tables_in_scb_default <> '_menuotr' AND tables_in_scb_default <> '_mst_icd9'\
      #             AND tables_in_scb_default <> '_mst_icdx' AND tables_in_scb_default <> '_mst_inacbg'\
      #             AND tables_in_scb_default <> '_mst_klasifikasi' AND tables_in_scb_default <> '_mst_pasien'\
      #             AND tables_in_scb_default <> '_mst_poli' AND tables_in_scb_default <> '_riwayat_pasien'\
      #             AND tables_in_scb_default <> '_user'")
      cur.execute("SHOW TABLES")
      dt = cur.fetchall()
      for (tblname,) in dt:
         cur2 = conn.cursor()
         cur2.execute("SELECT COUNT(*) FROM %s" % (tblname,))
         dt2 = cur2.fetchall()
         for (count,) in dt2:
               dblist.append({'tblname':(tblname,), 'count':(count,)})
         cur2.close()
      cur.close()
      conn.close()
      return jsonify({'data':dblist})

   @staticmethod
   def clear_db():
      tblname = request.form['tblname']
      conn = _mod_conn.connectdb()
      try:
         cur = conn.cursor()
         cur.execute("DELETE FROM %s" % tblname)
      except:
         conn.close()
         msg = 'Database gagal dibersihkan !'
         return jsonify({'satatus':0, 'msg':msg})
      else:
         conn.commit()
         conn.close()
         msg = 'Database berhasil dibersihkan.'
         return jsonify({'satatus':1, 'msg':msg})

   @staticmethod
   def get_address(lnk):
      conn = _mod_conn.connectdb()
      cur = conn.cursor()
      cur.execute("SELECT nm_instansi, almt, kdpos, kota, tlp, fax, email FROM _data_instansi")
      dt = cur.fetchone()
      if dt is not None:
         nminstansi = dt[0]
         almt = dt[1]
         kdpos = dt[2]
         kota = dt[3]
         tlp = dt[4]
         fax = dt[5]
         email = dt[6]
      
      conn.close()
      return render_template(lnk, nminstansi=nminstansi, almt=almt, kdpos=kdpos, kota=kota, tlp=tlp,\
               fax=fax, email=email)
   
def get_app_start():
   file = str(os.path.isfile(FILE_CONFIG))
   if file == 'True':
      lines = open(FILE_CONFIG, "r").readlines()
      app_start = lines[43].split("=")[1].replace("'","").replace("\n","")
      return app_start
   else:
      app_start = 'OFF'
      return app_start