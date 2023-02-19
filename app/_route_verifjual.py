from app import app
from flask import url_for, render_template, abort, redirect, session, request, jsonify, abort
from app._mods import _mod_verifjual as _mst_verifjual

@app.route('/viewverifjual', methods=['GET'])
def viewverifjual():
   if 'username' in session:
      data = _mst_verifjual.cls_view_mst_verifjual.tblview_verifjual()
      return data
   else:
      abort(403)

@app.route('/viewappjual', methods=['GET'])
def viewappjual():
   if 'username' in session:
      data = _mst_verifjual.cls_view_mst_verifjual.tblview_appjual()
      return data
   else:
      abort(403)

@app.route('/viewdetilverifjual',methods=['GET'])
def viewdetilverifjual():
   if 'username' in session:
      data = _mst_verifjual.cls_view_mst_verifjual.tbldetilview_verifjual()
      return data
   else:
      abort(403)
@app.route('/viewdetilappjual',methods=['GET'])
def viewdetilappjual():
   if 'username' in session:
      data = _mst_verifjual.cls_view_mst_verifjual.tbldetilview_appjual()
      return data
   else:
      abort(403)


@app.route('/verifjual1', methods=['POST'])
def verifjual1():
   if 'username' in session:
      data = _mst_verifjual.cls_view_mst_verifjual.verifjual1()
      return data
   else:
      abort(403)

@app.route('/verifjual2', methods=['POST'])
def verifjual2():
   if 'username' in session:
      data = _mst_verifjual.cls_view_mst_verifjual.verifjual2()
      return data
   else:
      abort(403)
@app.route('/detilverifjual',methods=['POST','GET'])
def detilverifjual():
   if 'username' in session:
      data = _mst_verifjual.cls_view_mst_verifjual.detilverifjual()
      return data
   else:
      abort(403)
@app.route('/printformpenyaluran',methods=['POST','GET'])
def printformpenyaluran():
   if 'username' in session:
      data = _mst_verifjual.cls_view_mst_verifjual.printformpenyaluran()
      return data
   else:
      abort(403)

@app.route('/validasipenyaluran',methods=['POST','GET'])
def validasipenyaluran():
   if 'username' in session:
      data = _mst_verifjual.cls_view_mst_verifjual.validasipenyaluran()
      return data
   else:
      abort(403)

@app.route('/detilappjual',methods=['POST','GET'])
def detilappjual():
   if 'username' in session:
      data = _mst_verifjual.cls_view_mst_verifjual.detilappjual()
      return data
   else:
      abort(403)

@app.route('/cetakverifpenyaluran',methods=['POST','GET'])
def cetakverifpenyaluran():
   if 'username' in session:
      return render_template('_verifikasijual/frmverifpenyaluran.html')
   else:
      abort(403)
@app.route('/verifpenyaluran',methods=['GET','POST'])
def verifpenyaluran():
   if 'username' in session:
      data = _mst_verifjual.cls_view_mst_verifjual.simpanverifjual()
      return data
   else:
      abort(403)
@app.route('/viewttfakturgd',methods=['GET','POST'])
def viewttfakturgd():
   if 'username' in session:
      data = _mst_verifjual.cls_view_mst_tukarfaktur.vew_ttfaktur()
      return data
   else:
      abort(403)
# Faktur Pajak Standar
@app.route('/viewfps',methods=['POST','GET'])
def viewfps():
   if 'username' in session:
      data = _mst_verifjual.cls_view_mst_tukarfaktur.view_fps()
      return data
   else:
      abort(403)

@app.route('/exportfps',methods=['POST','GET'])
def exportfps():
   if 'username' in session:
      data = _mst_verifjual.cls_view_mst_tukarfaktur.exportfps()
      return data
   else:
      abort(403)

@app.route('/detilterimafakturgd', methods=['POST'])
def detilterimafakturgd():
   if 'username' in session:
      data = _mst_verifjual.cls_view_mst_tukarfaktur.detil_terimafakturgd()
      return data
   else:
      abort(403)
@app.route('/simpanterimafakturjual',methods=['POST'])
def simpanterimafakturjual():
   if 'username' in session:
      data = _mst_verifjual.cls_view_mst_tukarfaktur.simpan_terimafakturjual()
      return data
   else:
      abort(403)
@app.route('/simpanterimafakturfps',methods=['POST'])
def simpanterimafakturfps():
   if 'username' in session:
      data = _mst_verifjual.cls_view_mst_tukarfaktur.simpan_terimafakturfps()
      return data
   else:
      abort(403)

@app.route('/cetakfps',methods=['POST'])
def cetakfps():
   if 'username' in session:
      data = _mst_verifjual.cls_view_mst_tukarfaktur.cetak_fps()
      return data
   else:
      abort(403)
@app.route('/printfps',methods=['POST'])
def printfps():
   if 'username' in session:
      data = _mst_verifjual.cls_view_mst_tukarfaktur.print_fps()
      return data
   else:
      abort(403)

@app.route('/viewtukarfakturpajak',methods=['POST','GET'])
def viewtukarfakturpajak():
   if 'username' in session:
      data = _mst_verifjual.cls_view_mst_tukarfaktur.view_tukarfakturpajak()
      return data
   else:
      abort(403)
@app.route('/detilterimafpsgd',methods=['POST','GET'])
def detilterimafpsgd():
   if 'username' in session:
      data = _mst_verifjual.cls_view_mst_tukarfaktur.detil_terimafpsgd()
      return data
   else:
      abort(403)
