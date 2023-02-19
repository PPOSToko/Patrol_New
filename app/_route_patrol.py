from app import app
from flask import url_for, render_template, abort, redirect, session, request, jsonify, abort
from app._mods import  _mod_patrol as _mst_patrol

@app.route('/startpatrol', methods=['GET'])
def startpatrol():
   if 'username' in session:
      data = _mst_patrol.cls_mst_patrol.trx_patrol()
      return data
   else:
      abort(403)

@app.route('/listunfinish',methods=['GET','POST'])
def listunfinish():
   if 'username' in session:
      data = _mst_patrol.cls_mst_patrol.list_unfinish()
      return data
   else:
      abort(403)

@app.route('/mulaipatrol',methods=['GET','POST'])
def mulaipatrol():
   if 'username' in session:
      data = _mst_patrol.cls_mst_patrol.mulaipatrol()
      return data
   else:
      abort(403)
@app.route('/simpanpatrol',methods=['GET','POST'])
def simpanpatrol():
   if 'username' in session:
      data = _mst_patrol.cls_mst_patrol.simpan_patrol()
      return data
   else:
      abort(403)

@app.route('/simpanhasilpatrol',methods=['GET','POST'])
def simpanhasilpatrol():
   if 'username' in session:
      data = _mst_patrol.cls_mst_patrol.simpan_hasilpatrol()
      return data
   else:
      abort(403)
@app.route('/stophasilpatrol',methods=['GET','POST'])
def stophasilpatrol():
   if 'username' in session:
      data = _mst_patrol.cls_mst_patrol.stop_hasilpatrol()
      return data
   else:
      abort(403)
@app.route('/viewdetilpatrol',methods=['GET','POST'])
def viewdetilpatrol():
   if 'username' in session:
      data = _mst_patrol.cls_mst_patrol.detil_viewpatrol()
      return data
   else:
      abort(403)
@app.route('/vieweditdetilpatrol',methods=['GET','POST'])
def vieweditdetilpatrol():
   if 'username' in session:
      data = _mst_patrol.cls_mst_patrol.detil_editviewpatrol()
      return data
   else:
      abort(403)

@app.route('/viewpatrol',methods=['GET','POST'])
def viewpatrol():
   if 'username' in session:
      data = _mst_patrol.cls_mst_patrol.view_patrol()
      return data
   else:
      abort(403)
@app.route('/viewhistorypatrol',methods=['GET','POST'])
def viewhistorypatrol():
   if 'username' in session:
      data = _mst_patrol.cls_mst_patrol.view_historypatrol()
      return data
   else:
      abort(403)
@app.route('/detilhispatrol',methods=['GET','POST'])
def detilhispatrol():
   if 'username' in session:
      data = _mst_patrol.cls_mst_patrol.detil_historypatrol()
      return data
   else:
      abort(403)
@app.route('/edithispatrol',methods=['GET','POST'])
def edithispatrol():
   if 'username' in session:
      data = _mst_patrol.cls_mst_patrol.edit_historypatrol()
      return data
   else:
      abort(403)
@app.route('/edithasilpatrol',methods=['GET','POST'])
def edithasilpatrol():
   if 'username' in session:
      data = _mst_patrol.cls_mst_patrol.edit_hasilpatrol()
      return data
   else:
      abort(403)
@app.route('/editremarkpatrol',methods=['GET','POST'])
def editremarkpatrol():
   if 'username' in session:
      data = _mst_patrol.cls_mst_patrol.edit_remarkpatrol()
      return data
   else:
      abort(403)

      

# app.route('/viewdetilhistorypatrol',methods=['GET','POST'])
# def viewdetilhistorypatrol():


