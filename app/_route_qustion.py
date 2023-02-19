from app import app
from flask import url_for, render_template, abort, redirect, session, request, jsonify, abort
from app._mods import _mod_mst_question as _mst_question

@app.route('/viewstockobat', methods=['GET'])
def viewstockobat():
   if 'username' in session:
      data = _trs_stock.cls_view_trs_data_stok.tblview_data_stok()
      return data
   else:
      abort(403)

@app.route('/mst-question', methods=['GET'])
def viewstockobatgd():
   if 'username' in session:
      data = _mst_question.cls_mst_question.mst_question()
      return data
   else:
      abort(403)
@app.route('/mst-induk', methods=['GET'])
def mst_induk():
   if 'username' in session:
      data = _mst_question.cls_mst_question.mst_induk()
      return data
   else:
      abort(403)
@app.route('/mst-induk-point', methods=['GET'])
def mst_induk_point():
   if 'username' in session:
      data = _mst_question.cls_mst_question.mst_induk_point()
      return data
   else:
      abort(403)
      
@app.route('/detilpertanyaan',methods=['GET','POST'])
def detilpertanyaan():
   if 'username' in session:
      data = _mst_question.cls_mst_question.detil_pertanyaan()
      return data
   else:
      abort(403)

@app.route('/caripoint',methods=['GET','POST'])
def caripoint():
   if 'username' in session:
      data = _mst_question.cls_cari_pertnyaan.cari_point()
      return data
   else:
      abort(403)

@app.route('/cariinduk',methods=['GET','POST'])
def cariinduk():
   if 'username' in session:
      data = _mst_question.cls_cari_pertnyaan.cari_induk()
      return data
   else:
      abort(403)
@app.route('/carileader',methods=['GET','POST'])
def carileader():
   if 'username' in session:
      data = _mst_question.cls_cari_pertnyaan.cari_leader()
      return data
   else:
      abort(403)
@app.route('/cariopr',methods=['GET','POST'])
def cariopr():
   if 'username' in session:
      data = _mst_question.cls_cari_pertnyaan.cari_opr()
      return data
   else:
      abort(403)

@app.route('/simpanpertanyaan',methods=['GET','POST'])
def simpanpertanyaan():
   if 'username' in session:
      data = _mst_question.cls_simpan_pertnyaan.simpan_pertanyaan()
      return data
   else:
      abort(403)
@app.route('/editpertanyaan',methods=['GET','POST'])
def editpertanyaan():
   if 'username' in session:
      data = _mst_question.cls_simpan_pertnyaan.edit_pertanyaan()
      return data
   else:
      abort(403)

@app.route('/viewpertanyaan',methods=['GET','POST'])
def viewpertanyaan():
   if 'username' in session:
      data = _mst_question.cls_mst_question.viewpertanyaan()
      return data
   else:
      abort(403)

@app.route('/viewunfinish',methods=['GET','POST'])
def viewunfinish():
   if 'username' in session:
      data = _mst_question.cls_mst_question.viewunfinishpatrol()
      return data
   else:
      abort(403)
@app.route('/viewpoint',methods=['POST','GET'])
def viewpoint():
   if 'username' in session:
      data = _mst_question.cls_mst_question.view_point()
      return data
   else:
      abort(403)
@app.route('/viewinduk',methods=['POST','GET'])
def viewinduk():
   if 'username' in session:
      data = _mst_question.cls_mst_question.view_induk()
      return data
   else:
      abort(403)

@app.route('/simpaninduk',methods=['POST','GET'])
def simpaninduk():
   if 'username' in session:
      data = _mst_question.cls_mst_question.simpan_induk()
      return data
   else:
      abort(403)
@app.route('/editinduk',methods=['POST','GET'])
def editinduk():
   if 'username' in session:
      data = _mst_question.cls_mst_question.edit_induk()
      return data
   else:
      abort(403)

@app.route('/simpanpoint',methods=['POST','GET'])
def simpanpoint():
   if 'username' in session:
      data = _mst_question.cls_mst_question.simpan_point()
      return data
   else:
      abort(403)      
@app.route('/editpoint',methods=['POST','GET'])
def editpoint():
   if 'username' in session:
      data = _mst_question.cls_mst_question.edit_point()
      return data
   else:
      abort(403)            