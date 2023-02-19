from app import app
from flask import url_for, render_template, abort, redirect, session, request, jsonify, abort
from app._mods import _mod_trs_jual as _trs_jual
from io import BytesIO
import xlsxwriter as xl
import xlrd
from werkzeug.datastructures import Headers
from werkzeug.utils import secure_filename
import os
import datetime

@app.route('/viewjualgd', methods=['GET'])
def viewjualgd():
   if 'username' in session:
      data = _trs_jual.cls_view_trs_penjualan.tblview_trs_penjualangd()
      return data
   else:
      abort(403)

@app.route('/lapjualgd', methods=['POST'])
def lapjualgd():
   if 'username' in session:
      
      data = _trs_jual.cls_view_lap_penjualan.lap_penjualangd()
      return data
   else:
      abort(403)
@app.route('/lappiutang', methods=['POST'])
def lappiutang():
   if 'username' in session:
      data = _trs_jual.cls_view_lap_penjualan.lap_piutang()
      return data
   else:
      abort(403)

      
@app.route('/prosesjualgd', methods=['POST'])
def prosesjualgd():
   if 'username' in session:
      data = _trs_jual.cls_view_trs_penjualan.prosesjualgd()
      return data
   else:
      abort(403)
@app.route('/prosesreturjualgd',methods=['POST'])
def prosesreturjualgd():
   if 'username' in session:
      data = _trs_jual.cls_view_trs_penjualan.prosesreturjualgd()
      return data
   else:
      abort(403)

@app.route('/cetaknotajualgd', methods=['POST'])
def cetaknotajualgd():
   if 'username' in session:
      data = _trs_jual.cls_view_trs_penjualan.cetak_fakturjualgd()
      return data
   else:
      abort(403)
@app.route('/cetaknotareturgd', methods=['POST'])
def cetakcetaknotareturgdnotajualgd():
   if 'username' in session:
      data = _trs_jual.cls_view_trs_penjualan.cetak_returjualgd()
      return data
   else:
      abort(403)


@app.route('/cetakulangnotajualgd', methods=['POST'])
def cetakulangnotajualgd():
   if 'username' in session:
      data = _trs_jual.cls_view_trs_penjualan.cetak_ulang_fakturjualgd()
      return data
   else:
      abort(403)
@app.route('/cetakulangnotareturjualgd',methods=['POST'])
def cetakulangnotareturjualgd():
   if 'username' in session:
      data = _trs_jual.cls_view_trs_penjualan.cetak_ulang_fakturreturjualgd()
      return data
   else:
      abort(403)

@app.route('/ceknota',methods=['POST','GET'])
def ceknota():
   if 'username' in session:
      data = _trs_jual.cls_view_trs_penjualan.cek_nota()
      return data
   else:
      abort(403)

@app.route('/detilreturgd', methods=['POST'])
def detilreturgd():
   if 'username' in session:
      data = _trs_jual.cls_view_trs_penjualan.detil_retur()
      return data
   else:
      abort(403)
@app.route('/simpanreturgd',methods=['POST'])
def simpanreturgd():
   if 'username' in session:
      data = _trs_jual.cls_view_trs_penjualan.simpan_returgd()
      return data
   else:
      abort(403)
@app.route('/viewambilbrg',methods=['POST','GET'])
def viewambilbrg():
   if 'username' in session:
      data = _trs_jual.cls_view_ambilbrg.ambil_brg()
      return data
   else:
      abort(403)
@app.route('/simpanambilbarang',methods=['POST','GET'])
def simpanambilbarang():
   if 'username' in session:
      data = _trs_jual.cls_view_ambilbrg.simpanambil_barang()
      return data
   else:
      abort(403)
@app.route('/cetaksj',methods=['GET','POST'])
def cetaksj():
   if 'username' in session:
      data = _trs_jual.cls_view_ambilbrg.cetak_suratjalan()
      return data
   else:
      abort(403)

@app.route('/ceknotasj',methods=['GET','POST'])
def ceknotasj():
   if 'username' in session:
      data = _trs_jual.cls_view_ambilbrg.cek_suratjalan()
      return data
   else:
      abort(403)
