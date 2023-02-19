from app import app
from flask import url_for, render_template, abort, redirect, session, request, jsonify, abort
from app._mods import _mod_user as _mst_users

@app.route('/listuser',methods=['GET'])
def listuser():
   if 'username' in session:
      data = _mst_users.cls_actusr.list_user()
      return data
   else:
      abort(403)
@app.route('/viewlistuser',methods=['GET','POST'])
def viewlistuser():
   if 'username' in session:
      data = _mst_users.cls_actusr.viewlist_user()
      return data
   else:
      abort(403)

@app.route('/resetpassword',methods=['POST','GET'])
def resetpassword():
   if 'username' in session:
      data = _mst_users.cls_actusr.reset_password()
      return data
   else:
      abort(403)
@app.route('/nonaktifuser',methods=['POST','GET'])
def nonaktifuser():
   if 'username' in session:
      data = _mst_users.cls_actusr.nonaktif_user()
      return data
   else:
      abort(403)

@app.route('/createuser', methods=['GET'])
def createuser():
   if 'username' in session:
      data = _mst_users.cls_actusr.create_user()
      return data
   else:
      abort(403)
@app.route('/simpanuser',methods=['GET','POST'])
def simpanuser():
   if 'username' in session:
      data = _mst_users.cls_actusr.simpan_user()
      return data
   else:
      abort(403)

@app.route('/cekaksesuser',methods=['GET','POST'])
def cekaksesuser():
   if 'username' in session:
      data = _mst_users.cls_actusr.cek_aksesuser()
      return data
   else:
      abort(403)

@app.route('/aksesuser', methods=['GET'])
def aksesuser():
   if 'username' in session:
      data = _mst_users.cls_actusr.akses_user()
      return data
   else:
      abort(403)
@app.route('/simpanpassword',methods=['GET','POST'])
def simpanpassword():
   if 'username' in session:
      data = _mst_users.cls_actusr.simpan_password()
      return data
   else:
      abort(403)

@app.route('/rubahpassword', methods=['GET'])
def rubahpassword():
   if 'username' in session:
      data = _mst_users.cls_actusr.rubah_password()
      return data
   else:
      abort(403)
@app.route('/simpanaksesuser',methods=['GET','POST'])
def simpanaksesuser():
   if 'username' in session:
      data = _mst_users.cls_actusr.simpan_akses()
      return data
   else:
      abort(403)
@app.route('/employee', methods=['GET'])
def employee():
   if 'username' in session:
      data = _mst_users.cls_actemployee.employee()
      return data
   else:
      abort(403)

@app.route('/viewemployee',methods=['GET','POST'])
def view_employee():
   if 'username' in session:
      data = _mst_users.cls_actemployee.view_employee()
      return data
   else:
      abort(403)

@app.route('/simpanemployee',methods=['GET','POST'])
def simpanemployee():
   if 'username' in session:
      data = _mst_users.cls_actemployee.simpan_employee()
      return data
   else:
      abort(403)

@app.route('/editemployee',methods=['GET','POST'])
def editemployee():
   if 'username' in session:
      data = _mst_users.cls_actemployee.edit_employee()
      return data
   else:
      abort(403)


