from app import app
from flask import url_for, render_template, abort, redirect, session, request, jsonify, abort
import os, pathlib, platform

# Root
from app import _mod_conn, _mod_config
from app._mods import _mod_login, _mod_mainmenu, _mod_users, _mod_otorisasi, _mod_instansi
from app._mods import _mod_searching,_mod_user

# =====================================================================
# ROOT
# =====================================================================
@app.route('/')
def index():
   if _mod_config.get_app_start().strip() == 'ON':
      try:
         _mod_conn.connectdb()
         if session.get('username') is not None:
            return redirect(url_for('home'))
         else:
            return redirect(url_for('login'))
      except:
         return redirect(url_for('errorpage'))
      if session.get('username') is not None:
         return redirect(url_for('home'))
      else:
         return redirect(url_for('login'))
   else:
      return render_template('maintenance.html')

@app.route('/errorpage')
def errorpage():
   return render_template('error_con.html')

@app.route('/login')
def login():
   if _mod_config.get_app_start().strip() == 'ON':
      try:
         _mod_conn.connectdb()
         if session.get('username') is not None:
            return redirect(url_for('home'))
         else:
            return render_template('login.html')
      except:
         return redirect(url_for('errorpage'))
   else:
      return render_template('maintenance.html')

@app.route('/login', methods=['POST'])
def auth():
   if session.get('username') is not None:
      print("Masuk Ke Home 1")  
      return redirect(url_for('home'))
   else:
      data = _mod_login.cls_logins.user_login()
      return data

@app.route('/home')
def home():
   # print("Proses Home woiiiii")
   if _mod_config.get_app_start().strip() == 'ON':
      try:
         _mod_conn.connectdb()
         if session.get('username') is not None:
            # model = _mod_login.cls_usermenu()
            # model.username = session['username']
            # mainmenu = model.mainmenu()
            xurl = request.host_url
            xos = platform.system()
            conn = _mod_conn.connectdb()
            cur = conn.cursor()
            cur.execute("select username,level from _users where username = '" + session['username'] + "'")
            dt = cur.fetchone()
            if dt is not None:
               xlevel = dt[1]
            else: 
               xlevel = ""
            cur.execute("select mn01,mn02,mn03,mn04,mn05,mn06,mn07,mn08,mn09,mn10,mn11,mn12,mn13,mn14 from _aksesmenu where level = '" + xlevel + "'")
            dt = cur.fetchone()
            if dt is None:
               mn01 = "" 
               mn02 = ""
               mn03 = ""
               mn04 = ""
               mn05 = ""
               mn06 = ""
               mn07 = ""
               mn08 = ""
               mn09 = ""
               mn10 = ""
               mn11 = ""
               mn12 = ""
               mn13 = ""
               mn14 = ""
            else:
               mn01 = dt[0]
               mn02 = dt[1]
               mn03 = dt[2]
               mn04 = dt[3]
               mn05 = dt[4]
               mn06 = dt[5]
               mn07 = dt[6]
               mn08 = dt[7]
               mn09 = dt[8]
               mn10 = dt[9]
               mn11 = dt[10]
               mn12 = dt[11]
               mn13 = dt[12]
               mn14 = dt[13]
            # template_title = _mod_config.configs.get_template_title()
            # return render_template('home.html', title=template_title, mainmenu=mainmenu, host=xurl, operating=xos)
            return render_template('home.html', title="Patrol", host=xurl, operating=xos,xmn01=mn01,xmn02=mn02,xmn03=mn03,xmn04=mn04,xmn05=mn05,
                                             xmn06=mn06,xmn07=mn07,xmn08=mn08,xmn09=mn09,xmn10=mn10,xmn11=mn11,xmn12=mn12,xmn13=mn13,xmn14=mn14)

         else:
            return redirect(url_for('login'))
      except:
         return redirect(url_for('errorpage'))
   else:
      return render_template('maintenance.html')

# @app.route('/gridmenu', methods=['POST'])
# def gridmenu():
#    if 'username' in session:
#       lnk = request.form['link']
#       desmenu = request.form['desmenu']
#       model = _mod_login.cls_usermenu()
#       model.idmenu = request.form['idmenu']
#       model.username = session['username']
#       menu = model.menu()
#       if model.idmenu == '' and desmenu == 'Beranda':
#             # Home Load
#             # return render_template(lnk)
#             data = _mod_config.configs.get_address(lnk)
#             return data
#       else:
#             return render_template(lnk, url=lnk, desmenu=desmenu, menu=menu)
#    else:
#       abort(403)

@app.route('/loadpage', methods=['POST'])
def loadpage():
   if 'username' in session:
      lnk = request.form['link']
      kdsp = session['lokasi']
      return render_template(lnk,kdsp=kdsp)
   else:
      abort(403)

@app.route('/loadpaged', methods=['POST'])
def loadpaged():
   if 'username' in session:
      lnk = request.form['link']
      data = request.form['nosp']
      return render_template(lnk,keydata=data)
   else:
      abort(403)
@app.route('/loadpagedapp', methods=['POST'])
def loadpagedapp():
   if 'username' in session:
      lnk = request.form['link']
      data = request.form['nosp']
      nofaktur = request.form['nofaktur']
      return render_template(lnk,nosp=data,nofaktur=nofaktur)
   else:
      abort(403)

# Unutk 3 Parameter selection 
# Ext : lokasigudang  + suplier
@app.route('/loadpageds', methods=['POST'])
def loadpageds():
   if 'username' in session:
      lnk = request.form['link']
      kdgudang = request.form['kdgudang']
      kdpemasok = request.form['kdpemasok']
      return render_template(lnk,kdgudang=kdgudang,kdpemasok=kdpemasok)
   else:
      abort(403)

# @app.route('/loadhome', methods=['POST'])
# def loadhome():
#    if 'username' in session:
#       lnk = request.form['link']
#       # return render_template(lnk, data=_mod_config.configs.get_address)
#       data = _mod_config.configs.get_address(lnk)
#       return data
#    else:
#       abort(403)

@app.route('/openform', methods=['POST'])
def openform():
   if 'username' in session:
      com = request.form['com']
      lnk = request.form['link']
      return render_template(lnk, com=com)
   else:
      abort(403)

@app.route('/logout')
def logout():
   session.clear()
   return redirect(url_for('login'))

@app.route('/loaduploads', methods=['POST'])
def loaduploads():
   if 'username' in session:
      xform = request.form['xform']
      return render_template('popuploads.html', xform=xform)
   else:
      abort(403)

# =====================================================================
# CONFIG
# =====================================================================
@app.route('/getbankdata', methods=['POST'])
def getbankdata():
   data = _mod_config.configs.get_bankdata()
   return data

@app.route('/simpanbankdata', methods=['POST'])
def simpanbankdata():
   data = _mod_config.configs.simpan_bankdata()
   return data

@app.route('/getconfig',methods=['POST'])
def getconfig():
   data = _mod_config.configs.get_config()
   return data

@app.route('/updateconfig', methods=['POST'])
def updateconfig():
   data = _mod_config.configs.update_config()
   return data

@app.route('/getdb', methods=['GET'])
def getdb():
   data = _mod_config.configs.get_db()
   return data

@app.route('/cleardb', methods=['POST'])
def cleardb():
   data = _mod_config.configs.clear_db()
   return data
# =====================================================================
# END CONFIG
# =====================================================================
