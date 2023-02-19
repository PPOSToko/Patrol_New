import email
from flask import request, jsonify, json, render_template
from flask.globals import session
from app import _mod_funct
from app import _mod_conn
import datetime

now = datetime.datetime.now()
tgl = now.strftime('%d/%m/%Y')

class cls_src_user:
    def __init__(self, cari=None):
        self.cari = cari

    def cari_list_user(self):
        dtlist = []
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur.execute("SELECT username, nama FROM _users WHERE (level<>'0' AND username LIKE '%s') OR (level<>'0' AND nama LIKE '%s')"\
                    % ('%'+self.cari+'%', '%'+self.cari+'%'))
        dt = cur.fetchall()
        for username, nama in dt:
            dtlist.append({'id':username, 'value':nama})
        cur.close()
        conn.close()
        return json.dumps(dtlist)

class cls_src_level:
   @staticmethod
   def list_level():
      conn = _mod_conn.connectdb()
      cur = conn.cursor()
      dtlist = []
      cur.execute("SELECT id, des FROM _user_level WHERE id<>0")
      dt = cur.fetchall()
      for idlevel, level in dt:
         dtlist.append({'idlevel':idlevel, 'level':level})
      conn.close()
      return jsonify({'data':dtlist})

   @staticmethod
   def list_group():
      conn = _mod_conn.connectdb()
      cur = conn.cursor()
      dtlist = []
      cur.execute("SELECT kd_group,nm_group from _user_group order by kd_group")
      dt = cur.fetchall()
      for kd_group,nm_group in dt:
         dtlist.append({'kd_group':kd_group, 'nm_group':nm_group})
      conn.close()
      return jsonify({'data':dtlist})
# // 
class cls_src_point:
   @staticmethod
   def list_point():
      conn = _mod_conn.connectdb()
      cur = conn.cursor()
      dtlist = []
      cur.execute("SELECT id_point, description,id_induk FROM point where id_point = 1 ORDER BY id_point")
      dt = cur.fetchall()
      for kode, nama, id_induk in dt:
         dtlist.append({'kode':kode, 'nama':nama,'induk':id_induk})
      conn.close()
      return jsonify({'data':dtlist})

   @staticmethod
   def list_golonganobat():
      conn = _mod_conn.connectdb()
      cur = conn.cursor()
      dtlist = []
      cur.execute("SELECT kode, nama FROM jenislaporan ORDER BY nama")
      dt = cur.fetchall()
      for kode, nama in dt:
         dtlist.append({'kode':kode, 'nama':nama})
      conn.close()
      return jsonify({'data':dtlist})

   @staticmethod
   def cari_klasifikasiobat():
      conn = _mod_conn.connectdb()
      cur = conn.cursor()
      dtlistklas = []
      cur.execute("SELECT kode, nama FROM jenisobat ORDER BY nama")
      data = cur.fetchall()
      for kode, nama in data:
         dtlistklas.append([kode, nama])
      cur.close()
      return dtlistklas
class cls_src_golterapi:
   def __init__(self, cari=None):
      self.cari = cari

   def cari_golterapi(self):
      lnk = request.form['link']
      key = request.form['key']
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      sql = "select a.kdgol,a.golongan,a.kd_terapi,b.nama from GOLONGAN a INNER JOIN TERAPI b ON a.kd_terapi = b.kode WHERE kdgol = '" + self.cari + "'" 
      cur.execute(sql)
      dt = cur.fetchone()
      if dt is not None:
         kdgol = dt[0]
         nmgol = dt[1]
         kdterapi =dt[2]
         nmterapi=dt[3]
         conn.close()
         return jsonify({'status':1, 'kdgol':kdgol, 'nmgol':nmgol,'kdterapi':kdterapi,'nmterapi':nmterapi})
      else:
         conn.close()
         return render_template(lnk, key=key, cari=self.cari)
   def cari_pop_golterapi(self):
      dtlist = []
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      sql = "select a.kdgol,a.golongan,a.kd_terapi,b.nama from GOLONGAN a INNER JOIN TERAPI b ON a.kd_terapi = b.kode WHERE golongan like '%" + self.cari + "%' and kd_terapi is not null" 
      
      cur.execute(sql)
      dt = cur.fetchall()
      for kdgol, nmgol,kdterapi,nmterapi in dt:
         dtlist.append({'kdgol':kdgol, 'nmgol':nmgol,'kdterapi':kdterapi,'nmterapi':nmterapi})
      conn.close()
      return jsonify({'data':dtlist})

class cls_src_generik:
   def __init__(self, cari=None):
      self.cari = cari

   def cari_generik(self):
      lnk = request.form['link']
      key = request.form['key']
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      sql = "SELECT kode, nama  FROM GENERIK WHERE kode = '" + self.cari + "'" 
      cur.execute(sql)
      dt = cur.fetchone()
      if dt is not None:
         kode = dt[0]
         nama = dt[1]
         conn.close()
         return jsonify({'status':1, 'kode':kode, 'nama':nama})
      else:
         conn.close()
         return render_template(lnk, key=key, cari=self.cari)

   def cari_pop_generik(self):
      dtlist = []
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      cur.execute("SELECT kode, nama FROM GENERIK  where nama like '%" + self.cari + "%'ORDER BY nama")
      dt = cur.fetchall()
      for kode, nama in dt:
         dtlist.append({'kode':kode, 'nama':nama})
      conn.close()
      return jsonify({'data':dtlist})


class cls_src_satuan:
   def __init__(self, cari=None):
      self.cari = cari
   
   @staticmethod
   def list_satuan():
      dtlist = []
      conn = _mod_conn.connectdb()
      cur = conn.cursor()
      cur.execute("SELECT kode, nama FROM SATUAN ORDER BY nama")
      dt = cur.fetchall()
      for kode, nama in dt:
         dtlist.append({'kdsatuan':kode, 'nmsatuan':nama})
      conn.close()
      return jsonify({'data':dtlist})

   def cari_satuan(self):
      lnk = request.form['link']
      key = request.form['key']
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      sql = "SELECT kode, nama  FROM SATUAN WHERE kode = '" + self.cari + "' or nama = '" + self.cari + "'"
      cur.execute(sql)
      dt = cur.fetchone()
      if dt is not None:
         kode = dt[0]
         nama = dt[1]
         conn.close()
         return jsonify({'status':1, 'kode':kode, 'nama':nama})
      else:
         conn.close()
         return render_template(lnk, key=key, cari=self.cari)
   def cari_regional(self):
      lnk = request.form['link']
      key = request.form['key']
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      sql = "SELECT kd_wilayah, nm_wilayah  FROM wilayah WHERE kd_wilayah = '" + self.cari + "' or nm_wilayah = '" + self.cari + "'"
      cur.execute(sql)
      dt = cur.fetchone()
      if dt is not None:
         kode = dt[0]
         nama = dt[1]
         conn.close()
         return jsonify({'status':1, 'kode':kode, 'nama':nama})
      else:
         conn.close()
         return render_template(lnk, key=key, cari=self.cari)


   def cari_satuanisi(self):
      lnk = request.form['link']
      key = request.form['key']
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      sql = "SELECT kode, nama  FROM SATUANISI WHERE kode = '" + self.cari + "'" 
      cur.execute(sql)
      dt = cur.fetchone()
      if dt is not None:
         kode = dt[0]
         nama = dt[1]
         conn.close()
         return jsonify({'status':1, 'kode':kode, 'nama':nama})
      else:
         conn.close()
         return render_template(lnk, key=key, cari=self.cari)

   def cari_pop_satuan(self):
      dtlist = []
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      sql= "SELECT kode, nama FROM SATUAN  where nama like '%" + self.cari + "%'ORDER BY nama"
      cur.execute(sql)
      dt = cur.fetchall()
      for kode, nama in dt:
         dtlist.append({'kode':kode, 'nama':nama})
      conn.close()
      return jsonify({'data':dtlist})

   def cari_pop_regional(self):
      dtlist = []
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      sql= "SELECT kd_wilayah, nm_wilayah FROM wilayah  where nm_wilayah like '%" + self.cari + "%'ORDER BY nm_wilayah"
      cur.execute(sql)
      dt = cur.fetchall()
      for kd_wiayah, nm_wilayah in dt:
         dtlist.append({'kode':kd_wiayah, 'nama':nm_wilayah})
      conn.close()
      return jsonify({'data':dtlist})

   def cari_pop_satuanisi(self):
      dtlist = []
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      sql = "SELECT kode, nama FROM SATUANISI  where nama like '%" + self.cari + "%'ORDER BY nama"
      cur.execute(sql)
      dt = cur.fetchall()
      for kode, nama in dt:
         dtlist.append({'kode':kode, 'nama':nama})
      conn.close()
      return jsonify({'data':dtlist})

class cls_src_gudang:
   def __init__(self, cari=None,gudangawal=None):
      self.cari = cari
      self.gudangawal = gudangawal

   def cari_gudang(self):
      lnk = request.form['link']
      key = request.form['key']
      dtlist = []
      conn = _mod_conn.connectdb()
      cur = conn.cursor()
      sql = "SELECT kdsp, nmsp, alamat, kontak  FROM CLIENT WHERE kdsp = '" + self.cari + "' and typeclient = 'PBF' " 
      # sql = "SELECT kdsp, nmsp, alamat, kontak  FROM CLIENT WHERE kdsp = '" + self.cari + "' and typeclient = 'PBF'" 
      cur.execute(sql)
      dt = cur.fetchone()
      if dt is not None:
         kdsp = dt[0]
         nmsp = dt[1]
         alamat = dt[2]
         kontak = dt[3]
         conn.close()
         return jsonify({'status':1, 'kdsp':kdsp, 'nmsp':nmsp, 'alamat':alamat, 'kontak':kontak})
      else:
         conn.close()
         return render_template(lnk, key=key, cari=self.cari,gudangawal=self.gudangawal)
   def cari_gudanggd(self):
      lnk = request.form['link']
      key = request.form['key']
      dtlist = []
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      sql = "SELECT kdsp, nmsp, alamat, kontak ,kd_wilayah FROM CLIENT WHERE kdsp = '" + self.cari + "' and typeclient = 'Gudang'" 
      cur.execute(sql)
      dt = cur.fetchone()
      if dt is not None:
         kdsp = dt[0]
         nmsp = dt[1]
         alamat = dt[2]
         kontak = dt[3]
         kdwilayah=dt[4]
         conn.close()
         return jsonify({'status':1, 'kdsp':kdsp, 'nmsp':nmsp, 'alamat':alamat, 'kontak':kontak,'kd_wilayah':kdwilayah})
      else:
         conn.close()
         return render_template(lnk, key=key, cari=self.cari,gudangawal=self.gudangawal)
   def cari_konfpemasokgd(self):
      lnk = request.form['link']
      key = request.form['key']
      kdobat = request.form['kdobat']
      kdlokasi = request.form['kdlokasi']
      kdpemasok = request.form['kdpemasok']
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      cur2 = conn.cursor()
      cur3 = conn.cursor()
      sql = "Select kdsp,nmsp,discon,discoff,minorder,hdabeli,hdj,satuanbeli,stdbeli from HARGADIS where  kdsp = '" + kdpemasok +  "'and kdbr = '" + kdobat +  "'and kd_client = '" + kdlokasi +  "'and stdbeli = 'Ya'"  
      cur.execute(sql)
      dt = cur.fetchone()
      if dt is not None:
         kdsp= dt[0]
         nmsp = dt[1]
         discon=dt[2]
         discoff=dt[3]
         xpricelist=dt[5]
         minorder=dt[4]
         hrgjadi=dt[6]
         satuanbeli=dt[7]
         stok=0         
         # periksa harga
         sql3 = "select harga from TB001 where kdbr = '" + kdobat + "'"
         cur3.execute(sql3)
         dt3 = cur3.fetchone()
         if dt3 is not None:
            xpricelist = dt3[0]
         #Periksa aturan belanja
         sql3= "select pricelist,disc,hrgjadi,minorder,satuanbeli from stdbelanja where kd_obat = '" + kdobat + "' and kd_suplier = '" + kdpemasok + "'"
         cur3.execute(sql3)
         dt3 = cur3.fetchone()
         if dt3 is not None:
            discon = dt3[1]
            hrgjadi = dt3[2]
            minorder = dt3[3]
            satuanbeli = dt3[4]
            discrp = (xpricelist * discon) /100
            xhrgjadi = xpricelist - discrp

         sql2 = "select COALESCE(SUM(saldo),0) as saldo from SAPOTEK where lokasi = '" + kdsp + "' and kd_obat ='" + kdobat + "'"         
         cur2.execute(sql2)
         dt2 = cur2.fetchone()
         if dt2 is not None:
            if dt2[0]==None:
               stok = 0
            else:
               stok = dt2[0]
         else:
            stok = 0
         conn.close()
         return jsonify({'status':1, 'kdsp':kdsp, 'nmsp':nmsp, 'discon':str("{:,.2f}".format(discon)), 'discoff':str(discoff),'pricelist':str(xpricelist),
                         'minorder':str(minorder),'hrgjadi': str("{:,.2f}".format(xhrgjadi)),'stok':str(stok),'satuanbeli':str(satuanbeli),'discrp':str("{:,.2f}".format(discrp))})
      else:
         conn.close()
         return render_template(lnk, key=key, cari=self.cari,kdlokasi=kdlokasi,kdobat=kdobat)
     

   def cari_gudangingd(self):
      lnk = request.form['link']
      key = request.form['key']
      kdobat = request.form['kdobat']
      dtlist = []
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      sql = "SELECT kdsp, nmsp, alamat, kontak  FROM CLIENT WHERE nmsp = '" + self.cari + "' and typeclient = 'Gudang' and kdsp <> '" + self.gudangawal + "'" 
      cur.execute(sql)
      dt = cur.fetchone()
      if dt is not None:
         kdsp = dt[0]
         nmsp = dt[1]
         alamat = dt[2]
         kontak = dt[3]
         sql2 = "select COALESCE(SUM(saldo),0) as saldo from SAPOTEK where lokasi = '" + kdsp + "' and kd_obat ='" + kdobat + "'"
         cur2 = conn.cursor()
         cur2.execute(sql2)
         dt2 = cur2.fetchone()
         if dt2 is not None:
            if dt2[0]==None:
               stok = 0
            else:
               stok = dt2[0]
         else:
            stok = 0
         conn.close()
         return jsonify({'status':1, 'kdsp':kdsp, 'nmsp':nmsp, 'alamat':alamat, 'kontak':kontak,'kdobat':kdobat,'kdgudangminta':self.gudangawal,'stock':stok})
      else:
         conn.close()
         return render_template(lnk, key=key, cari=self.cari,kdobat=kdobat,kdgudangminta=self.gudangawal)

   def cari_pop_gudang(self):
      dtlist = []
      conn = _mod_conn.connectdb()
      cur = conn.cursor()
      # sql = "SELECT kdsp, nmsp, alamat, kontak FROM CLIENT WHERE kdsp LIKE '% " + self.cari + "'  OR nmsp LIKE '%" + self.cari + "%' and typeclient = 'PBF' or  kdsp LIKE '% " + self.cari + "'  OR nmsp LIKE '" + self.cari + "' and typeclient = 'Gudang'" 
      sql = "SELECT kdsp, nmsp, alamat, kontak FROM CLIENT WHERE kdsp LIKE '% " + self.cari + "'  OR nmsp LIKE '%" + self.cari + "%' and typeclient = 'PBF' and kdsp <> '" + self.gudangawal + "'"

      cur.execute(sql)
      dt = cur.fetchall()
      for kdsp, nmsp, alamat, kontak  in dt:
         dtlist.append({'kdsp':kdsp, 'nmsp':nmsp, 'alamat':alamat, 'kontak':kontak})
      conn.close()
      return jsonify({'data':dtlist})

   def cari_pop_gudanggd(self):
      dtlist = []
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      # sql = "SELECT kdsp, nmsp, alamat, kontak FROM CLIENT WHERE kdsp LIKE '% " + self.cari + "'  OR nmsp LIKE '%" + self.cari + "%' and typeclient = 'PBF' or  kdsp LIKE '% " + self.cari + "'  OR nmsp LIKE '" + self.cari + "' and typeclient = 'Gudang'" 
      sql = "SELECT kdsp, nmsp, alamat, kontak FROM CLIENT WHERE kdsp LIKE '% " + self.cari + "'  OR nmsp LIKE '%" + self.cari + "%' and typeclient = 'Gudang' "
      cur.execute(sql)
      dt = cur.fetchall()
      for kdsp, nmsp, alamat, kontak  in dt:
         dtlist.append({'kdsp':kdsp, 'nmsp':nmsp, 'alamat':alamat, 'kontak':kontak})
      conn.close()
      return jsonify({'data':dtlist})
   
   def cari_pop_gudangingd(self):
      dtlist = []
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      cur2 = conn.cursor()
      kdobat = request.args.get('kdobat',None)
      # sql = "SELECT kdsp, nmsp, alamat, kontak FROM CLIENT WHERE kdsp LIKE '% " + self.cari + "'  OR nmsp LIKE '%" + self.cari + "%' and typeclient = 'PBF' or  kdsp LIKE '% " + self.cari + "'  OR nmsp LIKE '" + self.cari + "' and typeclient = 'Gudang'" 
      sql = "SELECT kdsp, nmsp, alamat, kontak FROM CLIENT WHERE kdsp LIKE '% " + self.cari + "' and kdsp <> '" + self.gudangawal + "'  OR nmsp LIKE '%" + self.cari + "%' and typeclient = 'Gudang' and kdsp <> '" + self.gudangawal + "'"
      cur.execute(sql)
      dt = cur.fetchall()
      stok = 0
      for kdsp, nmsp, alamat, kontak  in dt:
         sql2 = "select COALESCE(SUM(saldo),0) as saldo from SAPOTEK where lokasi = '" + kdsp + "' and kd_obat = '" + kdobat + "'"
         cur2.execute(sql2)
         dt2 = cur2.fetchone()
         if dt2 is not None:
            stok = dt2[0]
         dtlist.append({'kdsp':kdsp, 'nmsp':nmsp, 'alamat':alamat, 'kontak':kontak,'stock':str(stok)})
      conn.close()
      return jsonify({'data':dtlist})
class cls_src_sp:
   def __init__(self, cari=None):
      self.cari = cari

   def cari_spgd(self):
      lnk = request.form['link']
      key = request.form['key']
      kdclient = request.form['kdclient']
      kdgudang = session['lokasi']
      dtlist = []
      # Isi kiriman yg masih kosong
      conn = _mod_conn.connectdbgd()
      curi = conn.cursor()
      curi2 = conn.cursor()
      curi3 = conn.cursor()
      curi4 = conn.cursor()
      curi5 = conn.cursor()
      curi6 = conn.cursor()
      curi7 = conn.cursor()
      curi8 = conn.cursor()
      curi9 = conn.cursor()
      curi10 = conn.cursor()
      sqli = "Select tgl_sp,no_sp,jumlah from KONFIRMASISP where kd_client = '"  + kdclient +  "'and flag_proses = 'V' and flag_transaksi is null and kd_gudang  = '" + kdgudang + "'order by no_sp"
      curi.execute(sqli)
      dti = curi.fetchall()
      for tgl_sp,no_sp,jumlah in dti:
         sql2i = "select kd_obat,nm_obat,qty,qtysedia,qtykirim,tgl_pesan,tgl_kirim,tgl_booking from DTKIRIMBRG where no_sp = '" + no_sp +  "'and kd_client = '" + kdclient +  "'and qtysedia = 0"
         curi2.execute(sql2i)
         dt2i = curi2.fetchall()
         for kd_obat,nm_obat,qty,qtysedia,qtykirim,tgl_pesan,tgl_kirim,tgl_booking in dt2i:
            sql3i = "select batch,tgl_ed,saldo from SAPOTEK where kd_obat = '" + kd_obat + "'and lokasi = '" + kdgudang + "' and saldo > 0  order by STR_TO_DATE(tgl_ed,'%d/%m/%Y') asc"
            curi3.execute(sql3i)
            dt3i = curi3.fetchall()
            for batch,tgl_ed,saldo in dt3i:
               if saldo >= qty:
                  # Booking beserta batchno dan tgl ed nya
                  sql7i = "select kd_obat from DTKIRIMBRG where kd_obat = '" + kd_obat + "'and batch = '" + batch + "' and no_sp = '" + no_sp + "'and kd_client = '" + kdclient + "'"
                  curi7.execute(sql7i)
                  dt7i = curi7.fetchone()
                  if dt7i is None:
                     sql8i = "INSERT INTO DTKIRIMBRG set no_sp = '" + no_sp + "',kd_obat = '" + kd_obat + "',nm_obat = '" + nm_obat + "',batch = '" + batch + "',tgl_ed = '" + tgl_ed + "',qty = '" + str(qty) + "',qtysedia = '" +\
                            str(qty) + "',tgl_pesan = '" + tgl_pesan + "',tgl_kirim = '" + tgl_kirim + "', kd_gudang = '" + kdgudang + "',tgl_booking = '" + tgl_booking + "',kd_client = '" + kdclient + \
                            "',user_id = '" + session['username'] + "'"
                     curi8.execute(sql8i)
                     # Kurangi Stok
                     sql9i = "UPDATE SAPOTEK set saldo = (saldo - '" + str(qty) + "') where kd_obat = '" + kd_obat + "'and lokasi = '" + kdgudang + "'and batch = '" + batch + "'"
                     curi9.execute(sql9i)
                     # Hapus kiriman yg tidak ada nomor batchnya
                     sql10i = "DELETE FROM DTKIRIMBRG where kd_obat = '" + kd_obat + "'and batch = '' and no_sp = '" + no_sp + "'and kd_client = '" + kdclient + "'"
                     curi10.execute(sql10i)
                     conn.commit()
                     
               else:
                  sql4i = "select kd_obat from DTKIRIMBRG where kd_obat = '" + kd_obat + "'and batch = '" + batch + "' and no_sp = '" + no_sp + "'and kd_client = '" + kdclient + "'"
                  curi4.execute(sql4i)
                  dt4i = curi4.fetchone()
                  if dt4i is None:
                     sql5i = "INSERT INTO DTKIRIMBRG set no_sp = '" + no_sp + "',kd_obat = '" + kd_obat + "',nm_obat = '" + nm_obat + "',batch = '" + batch + "',tgl_ed = '" + tgl_ed + "',qty = '" + str(saldo) + "',qtysedia = '" +\
                            str(saldo) + "',tgl_pesan = '" + tgl_pesan + "',tgl_kirim = '" + tgl_kirim + "', kd_gudang = '" + kdgudang + "',tgl_booking = '" + tgl_booking + "',kd_client = '" + kdclient + \
                            "',user_id = '" + session['username'] + "'"
                     curi5.execute(sql5i)
                     # Kurangi Stok
                     # sql6 = "UPDATE SAPOTEK set saldo = (saldo - '" + qty + "') where kd_obat = '" + kd_obat + "'and lokasi = '" + kdgudang + "'and batch = '" + batch + "'"
                     sql6i = "DELETE FROM SAPOTEK where kd_obat = '" + kd_obat + "'and lokasi = '" + kdgudang + "'and batch = '" + batch + "'"
                     curi6.execute(sql6i)
                     # Hapus kiriman yg tidak ada nomor batchnya
                     qty = qty - saldo
                     sql6i = "UPDATE DTKIRIMBRG  set qty = (qty - '" + str(saldo) + "') where kd_obat = '" + kd_obat + "'and batch = '' and no_sp = '" + no_sp + "'and kd_client = '" + kdclient + "'"
                     curi6.execute(sql6i)
                     conn.commit()
# Mulai Ambil data
      cur = conn.cursor()
      cur2 = conn.cursor()
      sql = "Select tgl_sp,no_sp,jumlah from KONFIRMASISP where kd_client = '"  + kdclient +  "'and flag_proses = 'V' and flag_transaksi is null and kd_gudang  = '" + kdgudang + "' and no_sp = '" + self.cari + "'order by no_sp"
      cur.execute(sql)
      dt = cur.fetchone()
      if dt is not None:
         sqlp = "select kd_obat,qty,qtysedia,qtykirim from DTKIRIMBRG where no_sp = '" + dt[1] +  "'and kd_client = '" + kdclient +  "'and qtysedia > 0"
         cur2.execute(sqlp)
         datap = cur2.fetchone()
         if datap is None:
            msg ="Penjualan untuk Pesanan barang no : " + dt[1] + "<br>Tidak bisa dilakukan, stok persediaan barang belum ada !"
            return jsonify({'status':0, 'msg':msg})
         else:
            tglsp = dt[0]
            nosp = dt[1]
            jumlah=dt[2]
            conn.close()
            return jsonify({'status':1, 'tglsp':tglsp, 'nosp':nosp, 'jumalah':jumlah})
      else:
         conn.close()
         return render_template(lnk, key=key, kdclient=kdclient,cari=self.cari)

   def cari_pop_sp(self):
      dtlist = []
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      cur2 = conn.cursor()
      cur3 = conn.cursor()
      kdclient = request.args.get('kdclient', None)
      kdgudang = session['lokasi']
      # Isi Konfirmasi SP

      sql = "select no_sp,kd_client,tgl_pesan,kd_gudang from DTKIRIMBRG where qtysedia > 0 order by no_sp"
      cur.execute(sql)
      dt = cur.fetchall()
      for no_sp,kd_client,tgl_pesan,kd_gudang in dt:
         sql2 = "select no_sp  from KONFIRMASISP where kd_gudang = '" + kd_gudang + "' and kd_client = '" + kd_client + "' and no_sp = '" + no_sp + "'"
         cur2.execute(sql2)
         dt2 = cur2.fetchone()
         
         if dt2 is None:
            sql3 = "INSERT INTO KONFIRMASISP set jumlah = 0,kd_gudang = '" + kd_gudang + "',flag_proses = 'V',kd_client = '" + kd_client + "',no_sp = '" + no_sp + "',tgl_sp = '" + tgl_pesan + "'"
            cur3.execute(sql3)
            conn.commit()

      sql = "Select no_sp,tgl_sp,jumlah from KONFIRMASISP where kd_client = '"  + kdclient +  "'and flag_proses = 'V' and flag_transaksi is null and kd_gudang  = '" + kdgudang + "' order by no_sp"
      cur.execute(sql)
      dt = cur.fetchall()
      for no_sp, tgl_sp, jumlah  in dt:
         dtlist.append({'nosp':no_sp, 'tglsp':tgl_sp, 'jumlah':"{:,.2f}".format(jumlah) })
      conn.close()
      return jsonify({'data':dtlist})


class cls_src_pelanggan:
   def __init__(self, cari=None):
      self.cari = cari
   
   def cari_pelanggan(self):
      lnk = request.form['link']
      key = request.form['key']
      dtlist = []
      conn = _mod_conn.connectdb()
      cur = conn.cursor()
      # Tambahin status hanya yg statusnya Pelanggan yg masih prosepect tidak boleh muncul
      cur.execute("SELECT kdsp, nmsp, alamat, kontak, hp,apoteker,tgl_ijin,flapon,typeclient,lama_bayar,kd_klasifikasiclient,\
                   cara_bayar,nm_sales,sik,nm_pkp,nonpwp,kd_wilayah FROM CLIENT WHERE kdsp='%s'" \
                  % ( self.cari))
      dt = cur.fetchone()
      if dt is not None:
         kdsp = dt[0]
         nmsp = dt[1]
         alamat = dt[2]
         kontak = dt[3]
         hp = dt[4]
         apoteker=dt[5]
         tglijin=dt[6]
         flapon=dt[7]
         typeclient=dt[8]
         tempo=dt[9]
         kdklasifikasi = dt[10]
         carabayar=dt[11]
         sales = dt[12]
         sik=dt[13]
         nmwp = dt[14]
         nonpwp=dt[15]
         sql2 = "select kdsp from SUPLIER where kd_wilayah = '" +dt[16] + "'and stspbf = 2"
         cur2 = conn.cursor()
         cur2.execute(sql2)
         dt2 = cur2.fetchone()
         if dt2 is not None:
            kdsuplier = dt2[0]
         else:
            kdsuplier = ""
         cur3 = conn.cursor()
         cur3.execute("select nm_klas from KLASIFIKASI where kd_klas = '" + kdklasifikasi + "'")
         dt3 = cur3.fetchone()
         if dt3 is not None:
            nmklasifikasi = dt3[0]
         conn.close()
         return jsonify({'status':1, 'kdsp':kdsp, 'nmsp':nmsp, 'alamat':alamat, 'kontak':kontak, 'hp':hp,'apoteker':apoteker,'tglijin':tglijin,'flapon':flapon,
                         'typeclient':typeclient,'tempo':tempo,'kdklasifikasi':kdklasifikasi,'nmklasifikasi':nmklasifikasi,'carabayar':carabayar,'sales':sales,
                         'sik':sik,'nmwp':nmwp,'nonpwp':nonpwp,'kdsuplier':kdsuplier})

      else:
         conn.close()
         return render_template(lnk, key=key, cari=self.cari)

class cls_src_pelanggan:
   def __init__(self, cari=None):
      self.cari = cari
   def cari_jualpelanggangd(self):
      lnk = request.form['link']
      key = request.form['key']
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      cur.execute("SELECT kdsp, nmsp, alamat, kontak, hp,apoteker,tgl_ijin,flapon,typeclient,lama_bayar,kd_klasifikasiclient,\
                   cara_bayar,nm_sales,sik,nm_pkp,nonpwp,kd_wilayah,komisi,no_ijin,tgl_ijinapotek,margin,telepon,alamat2 FROM CLIENT WHERE kdsp='%s'" \
                  % ( self.cari))
      dt = cur.fetchone()
      if dt is not None:
         kdsp = dt[0]
         nmsp = dt[1]
         alamat = dt[2]+ " " + dt[22]
         kontak = dt[3]
         hp = dt[4]
         apoteker=dt[5]
         tglijin=dt[6]
         flapon=dt[7]
         typeclient=dt[8]
         tempo=dt[9]
         kdklasifikasi = dt[10]
         carabayar=dt[11]
         sales = dt[12]
         sik=dt[13]
         nmwp = dt[14]
         nonpwp=dt[15]
         komisi=dt[17]
         ijinsarana=dt[18]
         tglsarana=dt[19]
         margin=dt[20]
         telp=dt[21]
         sql2 = "select nm_wilayah from wilayah where kd_wilayah = '" +dt[16] + "'"
         cur2 = conn.cursor()
         cur2.execute(sql2)
         dt2 = cur2.fetchone()
         if dt2 is not None:
            regional = dt2[0]
         else:
            regional = ""
         sql2 = "select kdsp from SUPLIER where kd_wilayah = '" +dt[16] + "'and stspbf = 1"
         cur2 = conn.cursor()
         cur2.execute(sql2)
         dt2 = cur2.fetchone()
         if dt2 is not None:
            kdsuplier = dt2[0]
         else:
            kdsuplier = ""
         nmklasifikasi = ""
         cur3 = conn.cursor()
         cur3.execute("select nm_klas from KLASIFIKASI where kd_klas = '" + kdklasifikasi + "'")
         dt3 = cur3.fetchone()
         if dt3 is not None:
            nmklasifikasi = dt3[0]
         conn.close()
         return jsonify({'status':1, 'kdsp':kdsp, 'nmsp':nmsp, 'alamat':alamat, 'kontak':kontak, 'hp':hp,'apoteker':apoteker,'tglijin':tglijin,'flapon':str("{:,}".format(flapon)),
                         'typeclient':typeclient,'tempo':tempo,'kdklasifikasi':kdklasifikasi,'nmklasifikasi':nmklasifikasi,'carabayar':carabayar,'sales':sales,
                         'sik':sik,'nmwp':nmwp,'nonpwp':nonpwp,'kdsuplier':kdsuplier,'komisi':komisi,'ijinsarana':ijinsarana,'tglsarana':tglsarana,'margin':margin,
                         'regional':regional,'telp':telp})

      else:
         conn.close()
         return render_template(lnk, key=key, cari=self.cari)

   def cari_pelanggangd(self):
      lnk = request.form['link']
      key = request.form['key']
      dtlist = []
      # conn = _mod_conn.connectdbgd()
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      # Tambahin status hanya yg statusnya Pelanggan yg masih prosepect tidak boleh muncul
                  #        0    1      2        3      4   5      6          7    8            9        0                                
      # if key == "Data-From-Pelanggangd-jual":

      cur.execute("SELECT kdsp, nmsp, alamat, kontak, hp,apoteker,tgl_ijin,flapon,typeclient,lama_bayar,kd_klasifikasiclient,\
                   cara_bayar,nm_sales,sik,nm_pkp,nonpwp,kd_wilayah,komisi,no_ijin,tgl_ijinapotek,margin FROM CLIENT WHERE kdsp='%s'" \
                  % ( self.cari))
                  #    1        2        3    4      5        6         7    8          9
      dt = cur.fetchone()
      if dt is not None:
         kdsp = dt[0]
         nmsp = dt[1]
         alamat = dt[2]
         kontak = dt[3]
         hp = dt[4]
         apoteker=dt[5]
         tglijin=dt[6]
         flapon=dt[7]
         typeclient=dt[8]
         tempo=dt[9]
         kdklasifikasi = dt[10]
         carabayar=dt[11]
         sales = dt[12]
         sik=dt[13]
         nmwp = dt[14]
         nonpwp=dt[15]
         komisi=dt[17]
         ijinsarana=dt[18]
         tglsarana=dt[19]
         margin=dt[20]
# Periksa pemakaian limit
         sql2 = "select nm_wilayah from wilayah where kd_wilayah = '" +dt[16] + "'"
         cur2 = conn.cursor()
         cur2.execute(sql2)
         dt2 = cur2.fetchone()
         if dt2 is not None:
            regional = dt2[0]
         else:
            regional = ""
         # Cek Total terpakai
         sql2 = "select COALESCE(SUM(total),0) as tothutang from DTAPOTEK where no_rm = '" + kdsp + "'"
         print(sql2)
         cur2.execute(sql2)
         dt2 = cur2.fetchone()
         if dt2 is not None:
            if dt2[0]==None:
               terpakai = 0
            else:
               terpakai = dt2[0]
         sql2 = "select kdsp from SUPLIER where kd_wilayah = '" +dt[16] + "'and stspbf = 1"
         cur2 = conn.cursor()
         cur2.execute(sql2)
         dt2 = cur2.fetchone()
         if dt2 is not None:
            kdsuplier = dt2[0]
         else:
            kdsuplier = ""
         nmklasifikasi = ""
         cur3 = conn.cursor()
         cur3.execute("select nm_klas from KLASIFIKASI where kd_klas = '" + kdklasifikasi + "'")
         dt3 = cur3.fetchone()
         if dt3 is not None:
            nmklasifikasi = dt3[0]
         conn.close()
         return jsonify({'status':1, 'kdsp':kdsp, 'nmsp':nmsp, 'alamat':alamat, 'kontak':kontak, 'hp':hp,'apoteker':apoteker,'tglijin':tglijin,'flapon':str("{:,}".format(flapon)),
                         'typeclient':typeclient,'tempo':tempo,'kdklasifikasi':kdklasifikasi,'nmklasifikasi':nmklasifikasi,'carabayar':carabayar,'sales':sales,
                         'sik':sik,'nmwp':nmwp,'nonpwp':nonpwp,'kdsuplier':kdsuplier,'komisi':komisi,'ijinsarana':ijinsarana,'tglsarana':tglsarana,
                         'margin':margin,'regional':regional,'terpakai':"{:,}".format(terpakai)})

      else:
         conn.close()
         return render_template(lnk, key=key, cari=self.cari)
   # def cari_gudanggd(self):
   #    lnk = request.form['link']
   #    key = request.form['key']
   #    dtlist = []
   #    conn = _mod_conn.connectdbgd()
   #    cur = conn.cursor()
   #    # Tambahin status hanya yg statusnya Pelanggan yg masih prosepect tidak boleh muncul
   #    cur.execute("SELECT kdsp, nmsp, alamat, kontak, hp,apoteker,tgl_ijin,flapon,typeclient,lama_bayar,kd_klasifikasiclient,\
   #                 cara_bayar,nm_sales,sik,nm_pkp,nonpwp,kd_wilayah FROM CLIENT WHERE kdsp='%s' and typeclient = 'Gudang'" \
   #                % ( self.cari))
   #    dt = cur.fetchone()
   #    if dt is not None:
   #       kdsp = dt[0]
   #       nmsp = dt[1]
   #       alamat = dt[2]
   #       kontak = dt[3]
   #       hp = dt[4]
   #       apoteker=dt[5]
   #       tglijin=dt[6]
   #       flapon=dt[7]
   #       typeclient=dt[8]
   #       tempo=dt[9]
   #       kdklasifikasi = dt[10]
   #       carabayar=dt[11]
   #       sales = dt[12]
   #       sik=dt[13]
   #       nmwp = dt[14]
   #       nonpwp=dt[15]
   #       # sql2 = "select kdsp from SUPLIER where kd_wilayah = '" +dt[16] + "'and stspbf = 1"
   #       # cur2 = conn.cursor()
   #       # cur2.execute(sql2)
   #       # dt2 = cur2.fetchone()
   #       # if dt2 is not None:
   #       #    kdsuplier = dt2[0]
   #       # else:
   #       #    kdsuplier = ""
   #       # cur3 = conn.cursor()
   #       # cur3.execute("select nm_klas from KLASIFIKASI where kd_klas = '" + kdklasifikasi + "'")
   #       # dt3 = cur3.fetchone()
   #       # if dt3 is not None:
   #       #    nmklasifikasi = dt3[0]
   #       conn.close()
   #       return jsonify({'status':1, 'kdsp':kdsp, 'nmsp':nmsp, 'alamat':alamat, 'kontak':kontak, 'hp':hp,'apoteker':apoteker,'tglijin':tglijin,'flapon':flapon,
   #                       'typeclient':typeclient,'tempo':tempo,'carabayar':carabayar,'sales':sales,
   #                       'sik':sik,'nmwp':nmwp,'nonpwp':nonpwp})

   #    else:
   #       conn.close()
   #       return render_template(lnk, key=key, cari=self.cari)

   def cari_pop_pelanggan(self):
      dtlist = []
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      cur.execute("SELECT kdsp, nmsp, alamat, kontak, hp\
               FROM CLIENT WHERE kdsp LIKE '%s' OR nmsp LIKE '%s' " \
               % ( '%'+self.cari+'%', '%'+self.cari+'%'))
      dt = cur.fetchall()
      for kdsp, nmsp, alamat, kontak, hp  in dt:
         dtlist.append({'kdsp':kdsp, 'nmsp':nmsp, 'alamat':alamat, 'kontak':kontak, 'hp':hp})
      conn.close()
      return jsonify({'data':dtlist})

   def cari_pop_jualpelanggan(self):
      dtlist = []
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      cur2 = conn.cursor()
      sql = "select DISTINCT kd_client,nm_client from DTKIRIMBRG where qtysedia > 0"
      # sql = "select kd_client,nm_client  from KONFIRMASISP"
      cur.execute(sql)
      dt = cur.fetchall()
      for kd_client,nm_client in dt:
         print(kd_client)
         sql2 = "select kdsp,nmsp,alamat,kontak,hp from CLIENT where kdsp = '" + kd_client + "'"
         cur2.execute(sql2)
         dt2 = cur2.fetchone()
         if dt2 is not None:
            dtlist.append({'kdsp':dt2[0], 'nmsp':dt2[1], 'alamat':dt2[2], 'kontak':dt2[3], 'hp':dt2[4]})
      conn.close()
      return jsonify({'data':dtlist})


class cls_src_dokter:
   def __init__(self, cari=None):
      self.cari = cari
   
   def cari_dokter(self):
      lnk = request.form['link']
      key = request.form['key']
      dtlist = []
      conn = _mod_conn.connectdb()
      if key == 'Dokter-From-Daftar-Poli':
         kdpoli = request.form['kdpoli']
         cur = conn.cursor()
         cur.execute("SELECT kd_dok, nm_dok FROM _mst_dokter WHERE kd_dok='%s' AND kd_poli='%s' AND aktif='1'" % (self.cari, kdpoli))
      else:
         cur = conn.cursor()
         cur.execute("SELECT kd_dok, nm_dok FROM _mst_dokter WHERE kd_dok='%s' AND aktif='1'" % (self.cari))

      dt = cur.fetchone()
      if dt is not None:
         kddok = dt[0]
         nmdok = dt[1]
         
         conn.close()
         return jsonify({'status':1, 'kddok':kddok, 'nmdok':nmdok})

      else:
         conn.close()
         if key == 'Dokter-From-Daftar-Poli':
            return render_template(lnk, key=key, cari=self.cari, kdpoli=kdpoli)
         else:
            return render_template(lnk, key=key, cari=self.cari)

   def cari_pop_dokter(self):
      key = request.args.get('key', None)
      dtlist = []
      conn = _mod_conn.connectdb()
      cur = conn.cursor()
      if key == 'Dokter-From-Daftar-Poli':
         kdpoli = request.args.get('kdpoli', None)
         cur.execute("SELECT a.kd_dok, a.nm_dok, a.kd_poli, b.nm_poli FROM _mst_dokter a\
                     INNER JOIN _mst_poli b ON b.kd_poli = a.kd_poli\
                     WHERE (a.kd_dok LIKE '%s' OR a.nm_dok LIKE '%s') AND a.kd_poli='%s'\
                     AND a.aktif='1'" % ('%'+self.cari+'%', '%'+self.cari+'%', kdpoli))
      else:
         cur.execute("SELECT a.kd_dok, a.nm_dok, a.kd_poli, b.nm_poli FROM _mst_dokter a\
                     INNER JOIN _mst_poli b ON b.kd_poli = a.kd_poli\
                     WHERE a.kd_dok LIKE '%s' OR a.nm_dok LIKE '%s'\
                     AND a.aktif='1'" % ('%'+self.cari+'%', '%'+self.cari+'%'))

      dt = cur.fetchall()
      for kddok, nmdok, kdpoli, nmpoli in dt:
         dtlist.append({'kddok':kddok, 'nmdok':nmdok, 'kdpoli':kdpoli, 'nmpoli':nmpoli})
      conn.close()
      return jsonify({'data':dtlist})

class cls_src_icd:
   def __init__(self, cari=None):
      self.cari = cari
   
   def cari_icd(self):
      lnk = request.form['link']
      key = request.form['key']
      
      conn = _mod_conn.connectdb()
      cur = conn.cursor()
      cur.execute("SELECT icd, penyakit FROM _mst_icdx WHERE icd='%s'" % self.cari)
      dt = cur.fetchone()
      if dt is not None:
         icd = str(dt[0])
         penyakit = str(dt[1])
         conn.close()
         return jsonify({'status':1, 'icd':icd, 'penyakit':penyakit})
      else:
         conn.close()
         return render_template(lnk, key=key, cari=self.cari)

   def cari_pop_icd(self):
      dtlist = []
      conn = _mod_conn.connectdb()
      cur = conn.cursor()
      cur.execute("SELECT icd, penyakit FROM _mst_icdx WHERE icd LIKE '%s' OR penyakit LIKE '%s'"\
                  % ('%'+self.cari+'%', '%'+self.cari+'%'))
      dt = cur.fetchall()
      for icd, penyakit in dt:
         dtlist.append({'icd':icd, 'penyakit':penyakit})
      conn.close()
      return jsonify({'data':dtlist})
   
class cls_src_produk:
   def __init__(self, cari=None):
      self.cari = cari

   def cari_obat(self):      
      lnk = request.form['link']
      key = request.form['key']
      if key == 'Obat-From-Booking':
         kdklasifikasi=request.form['kdklasifikasi']
         conn = _mod_conn.connectdbgd()
         cur = conn.cursor()
         cur.execute("SELECT kdbr,nama,satuanbeli,harga,pabrik,nmklasifikasiobat,konversi FROM TB001 where kdbr='%s'" % self.cari)
         dt = cur.fetchone()
         if dt is not None:
            kdobat = dt[0]
            nmobat = dt[1]
            satuan = dt[2]
            harga = str(dt[3]).replace(",", "")
            pabrik = dt[4]
            golongan=dt[5]
            stok = 0
            minorder = 0
            hrgjadi = harga
            sql3 = "select sum(saldo) from SAPOTEK where kd_obat = '" + kdobat + "' and lokasi <> '00001' and lokasi <> '00002'"
            cur3 = conn.cursor()
            cur3.execute(sql3)
            dt3 = cur3.fetchone()
            if dt3 is not None:
               stok = dt3[0]

            # Cek harga
            sql2 = "select acuanhrg,flag_atur,pricelist,pricelist2,discjual,discjualon,discjualoff,disc,minorder,hrgjadi from stdjualobatpbf where kd_obat = '" + kdobat +  "'and kd_klasifikasiclient = '"  + kdklasifikasi +  "' and jual = 'Ya'" 
            cur2 = conn.cursor()
            cur2.execute(sql2)
            dt2 = cur2.fetchone()
            if dt2 is not None:
               # Cek discount Beli dan Jual
               xdiscbeli = 0
               xdiscjual = 0
               harga = str(dt2[2]).replace(",", "")
               minorder=dt2[8]
               hrgjadi=dt2[9]

            conn.close()
            return jsonify({'status':1, 'kdobat':kdobat, 'nmobat':nmobat, 'satuan':satuan, 'harga':harga, 'pabrik':pabrik,
                           'golongan':golongan,'stok':stok,'minorder':minorder,'hrgjadi':hrgjadi})
         else:
            conn.close()
            return render_template(lnk, key=key, cari=self.cari)

      else:
         conn = _mod_conn.connectdbgd()
         cur = conn.cursor()
         cur.execute("SELECT kdbr,nama,satuanbeli,harga,pabrik,nmklasifikasiobat FROM TB001 where kdbr='%s'" % self.cari)
         dt = cur.fetchone()
         if dt is not None:
            kdobat = dt[0]
            nmobat = dt[1]
            satuan = dt[2]
            harga = str(dt[3]).replace(",", "")
            pabrik = dt[4]
            golongan=dt[5]
            stok = 0

            conn.close()
            return jsonify({'status':1, 'kdobat':kdobat, 'nmobat':nmobat, 'satuan':satuan, 'harga':harga, 'pabrik':pabrik,
                           'golongan':golongan})
         else:
            conn.close()
            return render_template(lnk, key=key, cari=self.cari)
   @staticmethod
   def cari_obatpengganti():
      lnk = request.form['link']
      key = request.form['key']
      kdobat = request.form['kdobat']
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      sql = "select kd_persamaan from persamaanobat where kd_obat = '" + kdobat + "'"
      cur.execute(sql)
      dt = cur.fetchone()
      if dt is not None:
         kdpersamaan = dt[0]
      else:
         kdpersamaan = kdobat
      return render_template(lnk, key=key, cari=kdobat,kdpersamaan=kdpersamaan)
   
   def cari_persamaanobatgd(self):
      lnk = request.form['link']
      key = request.form['key']
      kdobat = request.form['kdobat']
      kdklasifikasi = request.form['kdklasifikasi']
      return render_template(lnk, key=key, cari=kdobat,kdklasifikasi=kdklasifikasi)
      # return render_template(lnk, key=key, cari=self.cari)
      # conn = _mod_conn.connectdbgd()
      # cur = conn.cursor()
      # sql = "select kd_persamaan from persamaanobat where kd_obat = '" + self.cari + "'"
      # cur.execute(sql)
      # dt = cur.fetchone()
      # if dt is not None:
      #    xkdpersamaan = dt[0]
      # else:
      #    xkdpersamaan = self.cari

   def cari_obatgd(self):      
      lnk = request.form['link']
      key = request.form['key']
      if key == 'Obat-From-Bookinggd':
         kdklasifikasi=request.form['kdklasifikasi']
         kdsp=request.form['kdsp']
         conn = _mod_conn.connectdbgd()
         sqlg = "select a.kd_wilayah,b.kd_gudang  from CLIENT a INNER JOIN wilayah b ON a.kd_wilayah = b.kd_wilayah where kdsp = '" + kdsp + "'"
         curg = conn.cursor()
         curg.execute(sqlg)
         dtg = curg.fetchone()
         kdgudang = ""
         if dtg is not None:
            kdgudang = dtg[1]

         cur = conn.cursor()
         cur.execute("SELECT kdbr,nama,satuan,harga,pabrik,nmklasifikasiobat,konversi FROM TB001 where kdbr='%s'" % self.cari)
         dt = cur.fetchone()
         if dt is not None:
            kdobat = dt[0]
            nmobat = dt[1]
            satuan = dt[2]
            harga = str(dt[3]).replace(",", "")
            pabrik = dt[4]
            golongan=dt[5]
            stok = 0
            minorder = 0
            hrgjadi = harga
            #cek stok 
            # sql3 = "select sum(saldo) from SAPOTEK where kd_obat = '" + kdobat + "' and lokasi <> '00001' and lokasi <> '00002' and lokasi <> '00126'"
            sql3 = "select sum(saldo) from SAPOTEK where kd_obat = '" + kdobat + "' and lokasi = '" + kdgudang + "'"
            cur3 = conn.cursor()
            cur3.execute(sql3)
            dt3 = cur3.fetchone()
            if dt3 is not None:
               stok = dt3[0]
            # Cek harga
            xbolehbeli = "Tidak"
            sql2 = "select acuanhrg,flag_atur,pricelist,pricelist2,discjual,discjualon,discjualoff,disc,minorder,hrgjadi,angka2 from stdjualobat where kd_obat = '" + kdobat +  "'and kd_klasifikasiclient = '"  + kdklasifikasi +  "' and jual = 'Ya'" 
            print(sql2)
            cur2 = conn.cursor()
            cur2.execute(sql2)
            dt2 = cur2.fetchone()
            if dt2 is not None:
               if dt2[0] == "Price List":
                  if dt2[1] == "Tetap":
                     if dt[3] >dt2[2]:
                        msg = "Harga Jual obat : " + dt[1] + " dibawah harga beli !<br>Hubungi penyelia untuk update harga penjualan"
                        return jsonify({'status':0,'msg':msg})
                     else:
                        xdiscbeli = 0
                        xdiscjual = 0
                        harga = str(dt2[2]).replace(",", "")
                        discon = dt2[5]
                        disconrp = (dt2[2] * dt2[5] ) / 100
                        discoff=dt2[6]
                        discoffrp = (dt2[2] * dt2[6] ) / 100
                        minorder=dt2[8]
                        hrgjadi=dt2[2] - disconrp
                        xbolehbeli = "Ya"
                  else:
                     xdiscbeli = 0
                     xdiscjual = 0
                     harga = str(dt2[2]).replace(",", "")
                     discon = dt2[5]
                     disconrp = (dt2[2] * dt2[5] ) / 100
                     discoff=dt2[6]
                     discoffrp = (dt2[2] * dt2[6] ) / 100
                     minorder=dt2[8]
                     hrgjadi=dt2[2] - disconrp
                     xbolehbeli = "Ya"
               elif dt2[0] == "Harga Jadi":
                  if dt2[1] == "Harga Jadi":
                     xdiscbeli = 0
                     xdiscjual = 0
                     harga = str(dt2[9]).replace(",", "")
                     discon = dt2[5]
                     disconrp = 0
                     discoff=0
                     discoffrp = 0
                     minorder=dt2[8]
                     hrgjadi=dt2[9] - disconrp
                     xbolehbeli = "Ya"
                  elif dt2[1] == "Price List":  
                     xdiscbeli = 0
                     xdiscjual = 0
                     harga = str(dt2[2]).replace(",", "")
                     discon = dt2[5]
                     disconrp = (dt2[2] * dt2[5] ) / 100
                     discoff=dt2[6]
                     discoffrp = (dt2[2] * dt2[6] ) / 100
                     minorder=dt2[8]
                     hrgjadi=dt2[2] - disconrp
                     xbolehbeli = "Ya"
                  elif dt2[1] == "Tetap":  
                     if dt[3] >dt2[2]:
                        msg = "Harga Jual obat : " + dt[1] + " dibawah harga beli !<br>Hubungi penyelia untuk update harga penjualan"
                        return jsonify({'status':0,'msg':msg})
                     else:
                        xdiscbeli = 0
                        xdiscjual = 0
                        harga = str(dt2[10]).replace(",", "")
                        discon = dt2[5]
                        disconrp = (dt2[10] * (dt2[5]+dt2[6])) / 100
                        discoff=dt2[6]
                        discoffrp = (dt2[10] * dt2[6] ) / 100
                        minorder=dt2[8]
                        hrgjadi=dt2[10] - disconrp
                        xbolehbeli = "Ya"
                  elif dt2[1] == "Margin PL":  
                     xpricelist = dt2[2] / ((100 - dt2[10]) / 100)
                     xdiscbeli = 0
                     xdiscjual = 0
                     harga = str(xpricelist).replace(",", "")
                     discon = dt2[5]
                     disconrp = (xpricelist * dt2[5] ) / 100
                     discoff=dt2[6]
                     discoffrp = (xpricelist * dt2[6] ) / 100
                     minorder=dt2[8]
                     hrgjadi=xpricelist - disconrp
                     xbolehbeli = "Ya"
                  elif dt2[1] == "Margin HJ": 
                     xpricelist = dt2[9] / ((100 - dt2[10]) / 100)
                     xdiscbeli = 0
                     xdiscjual = 0
                     harga = str(xpricelist).replace(",", "")
                     discon = dt2[5]
                     disconrp = (xpricelist * dt2[5] ) / 100
                     discoff=dt2[6]
                     discoffrp = (xpricelist * dt2[6] ) / 100
                     minorder=dt2[8]
                     hrgjadi=xpricelist - disconrp
                     xbolehbeli = "Ya"
               elif dt2[0] == "Tetap":
                  if dt2[10] < dt2[9]:
                     msg = "Harga Jual obat : " + dt[1] + " dibawah harga beli !<br>Hubungi penyelia untuk update harga penjualan"
                     return jsonify({'status':0,'msg':msg})
                  else:
                     if dt2[1] == "Tetap":
                        xpricelist = dt2[3] 
                        xdiscbeli = 0
                        xdiscjual = 0
                        harga = str(xpricelist).replace(",", "")
                        discon = 0
                        disconrp = 0
                        discoff=dt2[6]
                        discoffrp = (xpricelist * dt2[6] ) / 100
                        minorder=dt2[8]
                        hrgjadi=xpricelist - disconrp
                        xbolehbeli = "Ya"
                     else:
                        xpricelist = dt2[9] / ((100 - dt2[10]) / 100)
                        xdiscbeli = 0
                        xdiscjual = 0
                        harga = str(xpricelist).replace(",", "")
                        discon = dt2[5]
                        disconrp = (xpricelist * dt2[5] ) / 100
                        discoff=dt2[6]
                        discoffrp = (xpricelist * dt2[6] ) / 100
                        minorder=dt2[8]
                        hrgjadi=xpricelist - disconrp
                        xbolehbeli = "Ya"
            else:
               sql3 = "select acuanhrg,flag_atur,pricelist,pricelist2,discjual,discjualon,discjualoff,disc,minorder,hrgjadi from stdjualobat where kd_obat = '" + kdobat +  "'and kd_klasifikasiclient = '"  + kdklasifikasi +  "'" 
               cur3 = conn.cursor()
               cur3.execute(sql3)
               dt3 = cur3.fetchone()
               if dt3 is not None:
                  xdiscbeli = 0
                  xdiscjual = 0
                  harga = str(dt3[2]).replace(",", "")
                  discon = dt3[5]
                  disconrp = (dt3[3] * dt3[5] ) / 100
                  discoff=dt3[6]
                  discoffrp = (dt3[3] * dt3[4] ) / 100

                  minorder=dt3[8]
                  hrgjadi=dt3[9]
                  xbolehbeli = "Tidak"
               else:
                  discoff = 0
                  discon = 0
                  disconrp  = 0
                  discoffrp = 0
                  minorder = 1
                  hrgjadi = harga
                  xbolehbeli = "Tidak"
                  # conn.close()
                  # msg = "Standar Penjualan untuk klasifikasi pelanggan belum ditetapkan,<br>HUBUNGI PENYELIA !!!"
                  # return jsonify({'status':0,'msg':msg})
            if stok == None:
               stok = 0
            conn.close()
            discon = round(discon,3)
            return jsonify({'status':1, 'kdobat':kdobat, 'nmobat':nmobat, 'satuan':satuan, 'harga':harga, 'pabrik':pabrik,'discoff':discoff,'discoffrp':discoffrp,
                           'golongan':golongan,'stok':str(stok),'minorder':minorder,'discon':discon,'disconrp':disconrp,'hrgjadi':hrgjadi,'bolehbeli':xbolehbeli})
         else:
            conn.close()
            return render_template(lnk, key=key, cari=self.cari,kdklasifikasi=kdklasifikasi,kdsp=kdsp)
      elif key == 'Obat-From-Bookinggd-int':
         kdapotek=request.form['kdsp']
         kdklasifikasi=request.form['kdklasifikasi']
         conn = _mod_conn.connectdbgd()
         cur = conn.cursor()
         cur2 = conn.cursor()
         cur3 = conn.cursor()
         cur4 = conn.cursor()
         cur5 = conn.cursor()
         cur6 = conn.cursor()
         cur7 = conn.cursor()
         sql = "SELECT a.kdbr,a.nama,a.satuan,a.harga,a.pabrik,b.kd_persamaan,a.nmklasifikasiobat FROM TB001 a INNER JOIN persamaanobat b ON a.kdbr = b.kd_obat where a.kdbr='%s'" % self.cari
         cur.execute(sql)
         dt = cur.fetchone()
         if dt is not None:
            kdobat = dt[0]
            nmobat = dt[1]
            satuan = dt[2]
            harga = str(dt[3]).replace(",", "")
            pabrik = dt[4]
            kdpersamaan=dt[5]
            golongan = dt[6]
            cur2.execute("Select kd_obat,nm_obat,qty,satuanjual,qty2,satuanbeli,qtyisi,pricelist,disc,discrp,hrgjadi,acuanhrg,qtyisi from stdbelanjaclient where kd_client = '" + kdapotek + "'and kd_obat = '" + kdobat + "' order by kd_obat")
            dt2 = cur2.fetchone()
            if dt2 is None:
               # sql2= "select * from stdbelanja where kd_obat = '" + kdobat + "'and kd_klasifikasi = '001' and stdbeli = 'Ya'" 
               sql2 = "Select minorder,satuanbeli from kiriminternal where kd_obat = '" + kdobat + "' and kd_gudang = '" + kdapotek + "'"
               cur3.execute(sql2)
               dt3 = cur3.fetchone()
               if dt3 is not None:
                  # cek satuan beli
                  cur4.execute("select a.kdsatuan1,b.nama from TB001 a INNER JOIN SATUAN b ON a.kdsatuan1 = b.kode where a.kdbr = '" + kdobat + "'")
                  dt4 = cur4.fetchone()
                  if dt4 is not None:
                     satuanbeli = dt4[1]
                  else:
                     satuanbeli = satuan
                  stok= 0
                  cur5.execute("select sum(saldo) from SAPOTEK where kd_obat = '" + kdobat + "' and lokasi = '" + kdapotek + "'")
                  dt5 = cur5.fetchone()
                  if dt5 is not None:
                     saldo = dt5[0]
                  conn.close()
                  return jsonify({'status':1, 'kdobat':kdobat, 'nmobat':nmobat, 'satuan':satuanbeli, 'harga':harga, 'pabrik':pabrik,'stok':str(stok),'kdapotek':kdapotek,'golongan':golongan})
               else:
                  conn.close()
                  msg = "Standar Belanja belum ditetapkan, HUBUNGI PENYELIA !!!"
                  return jsonify({'status':0,'msg':msg,'kdpersamaan':kdpersamaan})
            else:
               conn.close()
               msg = "Barang yang dipesan barang Konsinyasi !!"
               return jsonify({'status':2,'msg':msg,'kdpersamaan':kdpersamaan})
         else:
            conn.close()
            return render_template(lnk, key=key,kdklasifikasi=kdklasifikasi,kdsp=kdapotek, cari=self.cari)
         
      elif key == 'Obat-From-updateprinsip':
         kdprinsipal=request.form['kdprinsipal']
         conn = _mod_conn.connectdbgd()
         cur = conn.cursor()
         cur3 = conn.cursor()
         cur2 = conn.cursor()
         cur.execute("SELECT kdbr,nama,kdsatuan1,kdsatuan2,satuan,konversi,harga,pabrik,nmklasifikasiobat FROM TB001 where kdbr='%s'" % self.cari)
         dt = cur.fetchone()
         if dt is not None:
            kdobat = dt[0]
            nmobat = dt[1]
            kdsatuanbeli = dt[2]
            kdsatuanjual=dt[3]
            cur2.execute("select nama from SATUAN where kode = '" + dt[2] + "'")
            dt2 = cur2.fetchone()
            if dt2 is not None:
               satuanbeli = dt2[0]
            else:
               satuanbeli = dt[4]   
            cur2.execute("select nama from SATUAN where kode = '" + dt[3] + "'")
            dt2 = cur2.fetchone()
            if dt2 is not None:
               satuanjual = dt2[0]
            else:
               satuanjual = dt[4]   
            isi = dt[5]

            # satuan = dt[2]
            # harga = str(dt[3]).replace(",", "")
            # pabrik = dt[4]
            # golongan=dt[5]
            # stok = 0

            conn.close()
            return jsonify({'status':1, 'kdobat':kdobat, 'nmobat':nmobat, 'satuanbeli':satuanbeli, 'satuanjual':satuanjual, 
                            'isi':isi, 'kdsatuanbeli':kdsatuanbeli,'kdsatuanjual':kdsatuanjual})
         else:
            conn.close()
            return render_template(lnk, key=key, kdprinsipal=kdprinsipal,cari=self.cari)
         
      elif key == 'Obat-From-updatepemasok':
         kdprinsipal=request.form['kdprinsipal']
         kdpemasok=request.form['kdpemasok']
         kdclient=request.form['kdclient']

         conn = _mod_conn.connectdbgd()
         cur = conn.cursor()
         cur3 = conn.cursor()
         cur2 = conn.cursor()
         cur.execute("SELECT kdbr,nama,kdsatuan1,kdsatuan2,satuan,konversi,harga,pabrik,nmklasifikasiobat FROM TB001 where kdbr='%s'" % self.cari)
         dt = cur.fetchone()
         if dt is not None:
            kdobat = dt[0]
            nmobat = dt[1]
            kdsatuanbeli = dt[2]
            kdsatuanjual=dt[3]
            xisi = dt[5]
            pricelist =dt[6]
            cur2.execute("select nama from SATUAN where kode = '" + dt[2] + "'")
            dt2 = cur2.fetchone()
            if dt2 is not None:
               satuanbeli = dt2[0]
            else:
               satuanbeli = dt[4]   
            cur2.execute("select nama from SATUAN where kode = '" + dt[3] + "'")
            dt2 = cur2.fetchone()
            if dt2 is not None:
               satuanjual = dt2[0]
            else:
               satuanjual = dt[4]   
            xisi = dt[5]
# Cek Pricelist
            sql3 = "select nettbeli from UPDATEHARGA where kd_obat = '" + kdobat + "'"
            cur3.execute(sql3)
            dt3 = cur3.fetchone()
            if dt3 is not None:
               pricelist = dt3[0]

            sql3 = "Select discon,disconrp,discoff,discoffrp,minorder,konversi from HARGADIS where KDBR = '" + kdobat +  "'and kdprinsip = '" + kdprinsipal +  "'and kdsp = '" + kdpemasok +  "'and kd_client = '" +kdclient + "'"
            cur3.execute(sql3)
            dt3 = cur3.fetchone()
            if dt3 is not None:
               xdiscon = dt3[0]
               xdisconrp = dt3[1]
               xdiscoff = dt3[2]
               xdiscoffrp = dt3[3]
               xminorder = dt3[4]
               xisi = dt3[5]
            else:
               xdiscon = 0
               xdisconrp = 0
               xdiscoff = 0
               xdiscoffrp = 0
               xminorder = 1

            if xdiscon > 0:
               valdiscon = (pricelist * xdiscon)/100
            else:
               valdiscon = xdisconrp
            if xdiscoff > 0:
               valdiscoff = (pricelist * xdiscon)/100
            else:
               valdiscoff = xdiscoffrp
            hrgjadi = pricelist - (valdiscon + valdiscoff)
            selisih = pricelist - hrgjadi
            # pricelist = "{:,}".format(int(pricelist))
            # hrgjadi = "{:,}".format(int(hrgjadi))
            # selisih = "{:,}".format(int(selisih))
            conn.close()
            return jsonify({'status':1, 'kdobat':kdobat, 'nmobat':nmobat, 'satuanbeli':satuanbeli, 'satuanjual':satuanjual, 
                            'isi':xisi, 'kdsatuanbeli':kdsatuanbeli,'kdsatuanjual':kdsatuanjual,'discon':xdiscon,'disconrp':xdisconrp,
                            'discoff':xdiscoff,'discoffrp':xdiscoffrp,'pricelist':pricelist,'minorder':xminorder,'hrgjadi':hrgjadi,'selisih':selisih})
         else:
            conn.close()
            return render_template(lnk, key=key, kdprinsipal=kdprinsipal,cari=self.cari)
      elif key == 'Obat-From-ttbgd':
         conn = _mod_conn.connectdbgd()
         cur = conn.cursor()
         sql = "SELECT kdbr,nama,kdsatuan1,satuanbeli,kdsatuan2,satuan,harga,pabrik,nmklasifikasiobat FROM TB001 where nama='%s'" % self.cari
         cur.execute(sql)
         dt = cur.fetchone()
         if dt is not None:
            kdobat = dt[0]
            nmobat = dt[1]
            kdsatuanbeli = dt[2]
            nmsatuanbeli = dt[3]
            kdsatuanjual = dt[4]
            nmsatuanjual = dt[5]
            harga = str(dt[6]).replace(",", "")
            pabrik = dt[7]
            golongan=dt[8]
            stok = 0
            conn.close()
            return jsonify({'status':1, 'kdobat':kdobat, 'nmobat':nmobat, 'kdsatuanbeli':kdsatuanbeli,'nmsatuanbeli':nmsatuanbeli, 'kdsatuanjual':kdsatuanjual,
                            'nmsatuanjual':nmsatuanjual, 'harga':harga, 'pabrik':pabrik, 'golongan':golongan})
         else:
            conn.close()
            return render_template(lnk, key=key, cari=self.cari)

      else:

         conn = _mod_conn.connectdbgd()
         cur = conn.cursor()
         cur.execute("SELECT kdbr,nama,satuan,harga,pabrik,nmklasifikasiobat FROM TB001 where kdbr='%s'" % self.cari)
         dt = cur.fetchone()
         if dt is not None:
            kdobat = dt[0]
            nmobat = dt[1]
            satuan = dt[2]
            harga = str(dt[3]).replace(",", "")
            pabrik = dt[4]
            golongan=dt[5]
            stok = 0
            conn.close()
            return jsonify({'status':1, 'kdobat':kdobat, 'nmobat':nmobat, 'satuan':satuan, 'harga':harga, 'pabrik':pabrik,
                           'golongan':golongan})
         else:
            conn.close()
            return render_template(lnk, key=key, cari=self.cari)

   def cari_obatbaru(self):
      lnk = request.form['link']
      key = request.form['key']
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      cur2 = conn.cursor()
      if key == "Obat-From-Master":
         lnk = "/_search/popcarimasterobatbaru.html"
         sql = "select KDBR,NAMA,KDSATUAN1,KDSATUAN2,HDA,JENIS,GENERIK,KDGOL,KDTERAPI,KDPRINSIP,HARGA,KONVERSI from TB001 where kdbr = '" + self.cari + "'"
      else:   
         sql = "select KDBR,NAMA,KDSATUAN1,KDSATUAN2,HDA,JENIS,GENERIK,KDGOL,KDTERAPI,KDPRINSIP,HARGA,KONVERSI from TB002 where kdbr = '" + self.cari + "'"
      cur.execute(sql)
      dt = cur.fetchone()
      if dt is not None:
         kdobat = dt[0]
         nmobat = dt[1]
         kdsatuanbeli=dt[2]
         nmprinsipal=""
         sql2 = "SELECT nama from SATUAN where kode = '" + kdsatuanbeli + "'"
         cur2.execute(sql2)
         dt2 = cur2.fetchone()
         if dt2 is not None:
            nmsatuanbeli=dt2[0]
         kdsatuanjual=dt[3]
         sql2 = "SELECT nama from SATUAN where kode = '" + kdsatuanjual + "'"
         cur2.execute(sql2)
         dt2 = cur2.fetchone()
         if dt2 is not None:
            nmsatuanjual=dt2[0]
         hda=dt[4]
         jenis = dt[5]
         generik=dt[6]
         kdgolterapi=dt[7]
         nmgolterapi = ""
         sql2 = "SELECT golongan from GOLONGAN where kdgol = '" + kdgolterapi + "'"
         cur2.execute(sql2)
         dt2 = cur2.fetchone()
         if dt2 is not None:
            nmgolterapi=dt2[0]

         kdterapi=dt[8]
         nmterapi=""
         sql2 = "SELECT nama from TERAPI where kode = '" + kdterapi + "'"
         cur2.execute(sql2)
         dt2 = cur2.fetchone()
         if dt2 is not None:
            nmterapi=dt2[0]

         kdprinsipal=dt[9]
         sql2 = "SELECT nama from PRINSIP where kode = '" + kdprinsipal + "'"
         cur2.execute(sql2)
         dt2 = cur2.fetchone()
         if dt2 is not None:
            nmprinsipal=dt2[0]
         hna=dt[10]
         isi=dt[11]
         conn.close()
         return jsonify({'status':1, 'kdobat':kdobat, 'nmobat':nmobat, 'kdsatuanbeli':kdsatuanbeli,'kdsatuanjual':kdsatuanjual,
                        'hda':hda, 'jenis':jenis,'generik':generik,'kdgolterapi':kdgolterapi,'kdterapi':kdterapi,
                        'kdprinsipal':kdprinsipal,'hna':hna,'isi':isi,'nmsatuanbeli':nmsatuanbeli,'nmsatuanjual':nmsatuanjual,
                        'nmprinsipal':nmprinsipal,'nmgolterapi':nmgolterapi,'nmterapi':nmterapi,'golongan':jenis})
      else:
         conn.close()
         return render_template(lnk, key=key, cari=self.cari)

   def cari_pop_obatbaru(self):
      dtlist = []
      
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      cur.execute("SELECT kdbr,nama,satuanbeli,harga,pabrik FROM TB002 \
                  WHERE kdbr LIKE'%s' OR nama LIKE'%s'"\
                  % ('%'+self.cari+'%', '%'+self.cari+'%'))
      dt = cur.fetchall()
      for kdobat, nmobat, satuan, harga, pabrik  in dt:
         dtlist.append({'status':0, 'kdobat':kdobat, 'nmobat':nmobat, 'satuan':satuan, 'harga':harga, 'pabrik':pabrik})
      conn.close()
      return jsonify({'data':dtlist})

   def cari_pop_masterobatbaru(self):
      dtlist = []
      
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      sql ="SELECT kdbr,nama,satuanbeli,harga,pabrik FROM TB001 WHERE kdbr LIKE'%s' OR nama LIKE'%s'" % ('%'+self.cari+'%', '%'+self.cari+'%')
      cur.execute(sql)
      dt = cur.fetchall()
      for kdobat, nmobat, satuan, harga, pabrik  in dt:
         dtlist.append({'status':0, 'kdobat':kdobat, 'nmobat':nmobat, 'satuan':satuan, 'harga':harga, 'pabrik':pabrik})
      conn.close()
      return jsonify({'data':dtlist})

   def cari_pop_obat(self):
      dtlist = []
      conn = _mod_conn.connectdb()
      cur = conn.cursor()
      cur.execute("SELECT kdbr,nama,satuanbeli,harga,pabrik FROM TB001 \
                  WHERE kdbr LIKE'%s' OR nama LIKE'%s'"\
                  % ('%'+self.cari+'%', '%'+self.cari+'%'))
      dt = cur.fetchall()
      for kdobat, nmobat, satuan, harga, pabrik  in dt:
         dtlist.append({'status':0, 'kdobat':kdobat, 'nmobat':nmobat, 'satuan':satuan, 'harga':harga, 'pabrik':pabrik})
      conn.close()
      return jsonify({'data':dtlist})

   def cari_pop_obatgd(self):
      dtlist = []
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      kdklasifikasi = request.args.get('kdklasifikasi', None)
      kdprinsipal = request.args.get('kdprinsipal', None)
      kdsp = request.args.get('kdsp', None)
      if kdprinsipal == "":
         cur.execute("SELECT kdbr,nama,satuanbeli,harga,pabrik FROM TB001 \
                     WHERE kdbr LIKE'%s' OR nama LIKE'%s'"\
                     % ('%'+self.cari+'%', '%'+self.cari+'%'))
      else:
         sql = "SELECT kdbr,nama,satuanbeli,harga,pabrik FROM TB001 where kdprinsip = '" + kdprinsipal + "'and nama LIKE '%" + self.cari + "%'"
         cur.execute(sql)

      dt = cur.fetchall()
      for kdobat, nmobat, satuan, harga, pabrik  in dt:
         stok =0
         sql3 = "select sum(saldo) from SAPOTEK where kd_obat = '" + kdobat + "' and lokasi <> '00001' and lokasi <> '00002' and lokasi <> '00156'"
         
         cur3 = conn.cursor()
         cur3.execute(sql3)
         dt3 = cur3.fetchone()
         if dt3 is not None:
            stok = dt3[0]
            if stok == None:
               stok = 0
         if kdklasifikasi == "internal":
            sql2 = "select kdsp from HARGADIS where kd_client = '" + kdsp + "'and kdbr = '" + kdobat + "' and stdbeli = 'Ya'"
            cur2 = conn.cursor()
            cur2.execute(sql2)
            dt2 = cur2.fetchone()
            if dt2 is not None:
               jual = "Ya"
            else:
               jual="Tidak"

         else:
            sql2 = "select jual from stdjualobat where kd_obat = '" + kdobat +  "'and kd_klasifikasiclient = '"  + kdklasifikasi +  "' and jual = 'Ya'" 
            cur2 = conn.cursor()
            cur2.execute(sql2)
            dt2 = cur2.fetchone()
            if dt2 is not None:
               jual = "Ya"
            else:
               jual="Tidak"
         dtlist.append({'status':0, 'kdobat':kdobat, 'nmobat':nmobat, 'satuan':satuan, 'harga':harga, 'pabrik':pabrik,'stok':str(stok),'jual':jual})
      conn.close()
      return jsonify({'data':dtlist})
   @staticmethod
   def cari_pop_persamaanbeli():
      dtlist=[]
      kdpersamaan = request.args.get('kdpersamaan', None)
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
# Isi data terlebih dahulu
      sql = "Select kd_obat,nm_obat,prinsipal,nm_suplier,satuanjual,pricelist,disc,discrp,hrgjadi,stdbeli,minorder,satuanbeli,stok from stdbelanja where  kd_persamaan = '" + kdpersamaan +  "'and kd_klasifikasi = '001' order by hrgjadi " 
      cur.execute(sql)
      dt = cur.fetchall()
      for kd_obat,nm_obat,prinsipal,nm_suplier,satuanjual,pricelist,disc,discrp,hrgjadi,stdbeli,minorder,satuanbeli,stok in dt:
         dtlist.append({'kdobat':kd_obat,'nmobat':nm_obat,'prinsipal':prinsipal,'nm_suplier':nm_suplier,'satuanjual':satuanjual,
                         'pricelist':pricelist,'disc':disc,'discrp':discrp,'hrgjadi':hrgjadi,'stdbeli':stdbeli,'minorder':minorder,
                         'satuanbeli':satuanbeli,'stok':str(stok)})
      conn.close()
      return jsonify({'data':dtlist})


   def cari_pop_persamaanobatgd(self):
      dtlist = []
      kdklasifikasi =  request.args.get('kdklasifikasi', None)
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      sql = "select kd_persamaan from persamaanobat where kd_obat = '" + self.cari + "'"
      cur.execute(sql)
      dt = cur.fetchone()
      if dt is not None:
         xkdpersamaan = dt[0]
      else:
         xkdpersamaan = self.cari

      sql2 = "Select a.kd_obat,b.nama,b.satuanbeli,b.harga,b.pabrik  from persamaanobat a INNER JOIN TB001 b ON a.kd_obat = b.kdbr where KD_PERSAMAAN = '" + xkdpersamaan + "' order by m,nm_obat"      
      cur2 = conn.cursor()
      cur2.execute(sql2)
      dt2 = cur2.fetchall()
      for kdobat, nmobat, satuan, harga, pabrik  in dt2:
         sql4 = "select acuanhrg from stdjualobat where kd_obat = '" + kdobat +  "'and kd_klasifikasiclient = '"  + kdklasifikasi +  "' and jual = 'Ya'" 
         cur4 = conn.cursor()
         cur4.execute(sql4)
         dt4 = cur4.fetchone()
         stdjual = "Tidak"
         if dt4 is not None:
            stdjual = "Ya"
            sql3 = "select sum(saldo) from SAPOTEK where kd_obat = '" + kdobat + "' and lokasi <> '00001' and lokasi <> '00002'"
            cur3 = conn.cursor()
            cur3.execute(sql3)
            dt3 = cur3.fetchone()
            if dt3 is not None:
               stok = dt3[0]
            else:
               stok = 0
            if stok == None:
               stok = 0
            dtlist.append({'status':0, 'kdobat':kdobat, 'nmobat':nmobat, 'satuan':satuan, 'harga':harga, 'pabrik':pabrik,'stdjual':stdjual,'stok':str(stok)})
      conn.close()
      return jsonify({'data':dtlist})

class cls_src_lab:
   def __init__(self, cari=None):
      self.cari = cari
   
   @staticmethod
   def list_jenis_lab():
      dtlist = []
      conn = _mod_conn.connectdb()
      cur = conn.cursor()
      cur.execute("SELECT kd_jenis, nm_jenis FROM _mst_jenis_lab ORDER BY nm_jenis ASC")
      dt = cur.fetchall()
      for kdjns, nmjns in dt:
         dtlist.append({'kdjns':kdjns, 'nmjns':nmjns})
      conn.close()
      return jsonify({'data':dtlist})

   def cari_jenis_lab(self):
      lnk = request.form['link']
      key = request.form['key']
      conn = _mod_conn.connectdb()
      cur = conn.cursor()
      cur.execute("SELECT kd_jenis, nm_jenis FROM _mst_jenis_lab \
                  WHERE kd_jenis='%s' OR nm_jenis='%s'" % (self.cari, self.cari))
      dt = cur.fetchone()
      if dt is not None:
         kdjenis = dt[0]
         nmjenis = dt[1]
         conn.close()
         return jsonify({'status':1, 'key':key, 'kdjenis':kdjenis, 'nmjenis':nmjenis})
      else:
         return render_template(lnk, key=key, cari=self.cari)

   def cari_pop_jenis_lab(self):
      dtlist = []
      conn = _mod_conn.connectdb()
      cur = conn.cursor()
      cur.execute("SELECT kd_jenis, nm_jenis FROM _mst_jenis_lab \
                  WHERE kd_jenis LIKE'%s' OR nm_jenis LIKE'%s'" % ('%'+self.cari+'%', '%'+self.cari+'%'))
      dt = cur.fetchall()
      for kdjenis, nmjenis in dt:
         dtlist.append({'kdjenis':kdjenis, 'nmjenis':nmjenis})
      conn.close()
      return jsonify({'data':dtlist})

   def cari_tindakan_lab(self):
      lnk = request.form['link']
      key = request.form['key']

      conn = _mod_conn.connectdb()
      cur = conn.cursor()
      if key == 'Tindakan-Lab-From-Rincian-Nilai-Normal':
         kdjns = request.form['kdjns']
         cur.execute("SELECT kd_tindakan, nm_tindakan FROM _mst_lab\
                     WHERE kd_tindakan='%s' AND kd_jenis='%s'" % (self.cari, kdjns))
      else:
         cur.execute("SELECT kd_tindakan, nm_tindakan FROM _mst_lab WHERE kd_tindakan='%s'" % self.cari)

      dt = cur.fetchone()
      if dt is not None:
         kdtindakan = dt[0]
         nmtindakan = dt[1]
         conn.close()
         return jsonify({'status':1, 'key':key, 'kdtindakan':kdtindakan, 'nmtindakan':nmtindakan})
      else:
         if key == 'Tindakan-Lab-From-Rincian-Nilai-Normal':
            return render_template(lnk, key=key, cari=self.cari, kdjns=kdjns)
         elif key == 'Tindakan-Lab-From-Trs-Lab':
            return render_template(lnk, key=key, cari=self.cari, kdjns=kdjns)
         else:
            return render_template(lnk, key=key, cari=self.cari)
   
   def cari_pop_tindakan_lab(self):
      key = request.args.get('key',None)
      dtlist = []
      conn = _mod_conn.connectdb()
      cur = conn.cursor()
      if key == 'Tindakan-Lab-From-Rincian-Nilai-Normal':
         kdjns = request.args.get('kdjns', None)
         cur.execute("SELECT kd_tindakan, nm_tindakan FROM _mst_lab\
                     WHERE (kd_tindakan LIKE'%s' AND kd_jenis='%s') \
                     OR (nm_tindakan LIKE'%s' AND kd_jenis='%s')"\
                     % ('%'+self.cari+'%', kdjns, '%'+self.cari+'%', kdjns))

      else:
         cur.execute("SELECT kd_tindakan, nm_tindakan FROM _mst_lab\
                     WHERE kd_tindakan LIKE'%s' OR nm_tindakan LIKE'%s'"\
                     % ('%'+self.cari+'%', '%'+self.cari+'%'))

      dt = cur.fetchall()
      for kdtindakan, nmtindakan in dt:
         dtlist.append({'kdtindakan':kdtindakan, 'nmtindakan':nmtindakan})
      conn.close()
      return jsonify({'data':dtlist})

   def cari_tarif_lab(self):
      lnk = request.form['link']
      key = request.form['key']
      kdklas = request.form['kdklas']
      kdjns = request.form['kdjns']

      conn = _mod_conn.connectdb()
      cur = conn.cursor()
      cur.execute("SELECT a.kd_tindakan, b.nm_tindakan, a.biaya\
                  FROM _mst_tarif_lab a\
                  INNER JOIN _mst_lab b ON b.kd_tindakan = a.kd_tindakan\
                  WHERE a.kd_tindakan='%s' AND a.kd_klas='%s' AND a.kd_jenis='%s' AND a.biaya > 0"\
                  % (kdklas, kdjns, self.cari))
      dt = cur.fetchone()
      if dt is not None:
         kdtindakan = dt[0]
         nmtindakan = dt[1]
         harga = dt[2]
         conn.close()
         return jsonify({'status':1, 'kdtindakan':kdtindakan, 'nmtindakan':nmtindakan, 'harga':harga})
      else:
         conn.close()
         return render_template(lnk, key=key, kdklas=kdklas, kdjns=kdjns, cari=self.cari)

   def cari_pop_tarif_lab(self):
      kdklas = request.args.get('kdklas', None)
      kdjns = request.args.get('kdjns', None)
      dtlist = []
      conn = _mod_conn.connectdb()
      cur = conn.cursor()
      cur.execute("SELECT a.kd_tindakan, b.nm_tindakan, a.biaya\
                  FROM _mst_tarif_lab a\
                  INNER JOIN _mst_lab b ON b.kd_tindakan = a.kd_tindakan\
                  WHERE b.nm_tindakan LIKE'%s' AND a.kd_klas='%s' AND a.kd_jenis='%s' AND a.biaya > 0"\
                  % ('%'+self.cari+'%', kdklas, kdjns))
      dt = cur.fetchall()
      for kdtindakan, nmtindakan, harga in dt:
         dtlist.append({'kdtindakan':kdtindakan, 'nmtindakan':nmtindakan, 'harga':harga})
      conn.close()
      return jsonify({'data':dtlist})

class cls_src_rad:
   def __init__(self, cari=None):
      self.cari = cari

   def cari_jenis_rad(self):
      lnk = request.form['link']
      key = request.form['key']

      conn = _mod_conn.connectdb()
      cur = conn.cursor()
      cur.execute("SELECT kd_jenis, nm_jenis FROM _mst_jenis_rad WHERE kd_jenis='%s'" % self.cari)
      dt = cur.fetchone()
      if dt is not None:
         kdjenis = dt[0]
         nmjenis = dt[1]
         conn.close()
         return jsonify({'status':1, 'key':key, 'kdjenis':kdjenis, 'nmjenis':nmjenis})
      else:
         return render_template(lnk, key=key, cari=self.cari)

   def cari_pop_jenis_rad(self):
      dtlist = []
      conn = _mod_conn.connectdb()
      cur = conn.cursor()
      cur.execute("SELECT kd_jenis, nm_jenis FROM _mst_jenis_rad WHERE kd_jenis LIKE'%s' OR nm_jenis LIKE'%s'"\
                  % ('%'+self.cari+'%', '%'+self.cari+'%'))
      dt = cur.fetchall()
      for kdjenis, nmjenis in dt:
         dtlist.append({'kdjenis':kdjenis, 'nmjenis':nmjenis})
      conn.close()
      return jsonify({'data':dtlist})

   def cari_tindakan_rad(self):
      lnk = request.form['link']
      kdjns = request.form['kdjns']

      conn = _mod_conn.connectdb()
      cur = conn.cursor()
      cur.execute("SELECT kd_tindakan, nm_tindakan FROM _mst_rad WHERE kd_tindakan='%s' AND kd_jenis='%s'"\
                  % (self.cari, kdjns))
      dt = cur.fetchone()
      if dt is not None:
         kdtindakan = dt[0]
         nmtindakan = dt[1]
         conn.close()
         return jsonify({'status':1, 'kdtindakan':kdtindakan, 'nmtindakan':nmtindakan})
      else:
         conn.close()
         return render_template(lnk, cari=self.cari)

   def cari_pop_tindakan_rad(self):
      kdjns = request.args.get('kdjns', None)
      dtlist = []
      conn = _mod_conn.connectdb()
      cur = conn.cursor()
      cur.execute("SELECT kd_tindakan, nm_tindakan FROM _mst_rad WHERE (kd_tindakan LIKE '%s' OR nm_tindakan LIKE '%s')\
                  AND kd_jenis='%s'" % ('%'+self.cari+'%', '%'+self.cari+'%', kdjns))
      dt = cur.fetchall()
      for kdtindakan, nmtindakan in dt:
         dtlist.append({'kdtindakan':kdtindakan, 'nmtindakan':nmtindakan})
      conn.close()
      return jsonify({'data':dtlist})

class cls_src_prinsipal:
   def __init__(self, cari=None):
      self.cari = cari

   def cari_prinsipal(self):
      lnk = request.form['link']
      key = request.form['key']
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()

      sql = "SELECT kode, nama FROM PRINSIP WHERE kode ='" + self.cari + "'"
      cur.execute(sql)
      dt = cur.fetchone()
      if dt is not None:
         kode = str(dt[0])
         nama = str(dt[1])
         conn.close()
         return jsonify({'status':0, 'kode':kode, 'nama':nama})
      else:
       return render_template(lnk, key=key,cari=self.cari)
   def cari_rekening(self):
      lnk = request.form['link']
      key = request.form['key']
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      sql = "SELECT kode, nm_bank,no_rekening FROM rekeningbank WHERE no_rekening ='" + self.cari + "'"
      cur.execute(sql)
      dt = cur.fetchone()
      if dt is not None:
         kode = str(dt[0])
         nm_bank = str(dt[1])
         no_rekening = str(dt[2])
         conn.close()
         return jsonify({'status':0, 'kode':kode, 'nm_bank':nm_bank,'no_rekening':no_rekening})
      else:
         print(lnk)
         return render_template(lnk, key=key,cari=self.cari)


   def pop_cari_prinsipal(self):
      dtlist = []
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      cur.execute("SELECT kode, nama, alamat1,alamat2,telp FROM PRINSIP \
                  WHERE nama LIKE'%s' ORDER BY nama" % ("%"+self.cari+"%"))
      dt = cur.fetchall()
      for kode, nama, alamat1,alamat2,telp in dt:
         if alamat1 == None :
            alamat = "-"
         else:
            # alamat = alamat1
            alamat = alamat1 + " " + alamat2
         
         dtlist.append({'kode':kode, 'nama':nama, 'alamat':alamat,'telp':telp})
      conn.close()
      return jsonify({'data':dtlist})

   def pop_carirekening(self):
      dtlist = []
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      sql = "SELECT kode, nm_bank, no_rekening FROM rekeningbank \
                  WHERE no_rekening LIKE'%s' ORDER BY no_rekening" % ("%"+self.cari+"%")
      cur.execute("SELECT kode, nm_bank, no_rekening FROM rekeningbank \
                  WHERE no_rekening LIKE'%s' ORDER BY no_rekening" % ("%"+self.cari+"%"))
      dt = cur.fetchall()
      for kode, nm_bank, no_rekening in dt:
         
         dtlist.append({'kode':kode, 'nm_bank':nm_bank, 'no_rekening':no_rekening})
      conn.close()
      return jsonify({'data':dtlist})


class cls_src_pemasok:
   def __init__(self, cari=None):
      self.cari = cari
   def cari_pemasokgd(self):
      lnk = request.form['link']
      key = request.form['key']
      if key == "Pemasok-piutang":
         prinsipal = ""
         kdregional = ""
      else:
         prinsipal =request.form['kdprinsipal']
         kdregional =request.form['kdregional']
      return render_template(lnk, key=key,prinsipal = prinsipal,kdregional=kdregional,cari=self.cari)


      

   def cari_kontakpemasokgd(self):
      lnk = request.form['link']
      key = request.form['key']
      tglminta =request.form['tglminta']
      return render_template(lnk, key=key,tglminta=tglminta,cari=self.cari)

   def cari_pemasokobat(self):
      lnk = request.form['link']
      key = request.form['key']
      kdobat = request.form['kdobat']
      kdapotek = request.form['kdapotek']
      kdpemasok = request.form['kdpemasok']
      return render_template(lnk, key=key,kdobat = kdobat,kdapotek=kdapotek,cari=self.cari)

   def pop_cari_pemasokobat(self):
      dtlist = []
      key =request.args.get('key', None)
      kdobat = request.args.get('kdobat', None)
      kdapotek =request.args.get('kdapotek', None)
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      sql = "Select kdsp,nmsp,cara_bayar,lama_bayar,minfaktur,minorder,satuanbeli,hdabeli,discon,disconrp,hdj from HARGADIS where kdbr = '" + kdobat + "'and kd_client = '" +kdapotek + "'and stdbeli = 'Ya'"
      # cur.execute("SELECT kdsp, nmsp, alamat, telepon FROM SUPLIER \
      #             WHERE nmsp LIKE'%s' ORDER BY nmsp" % ("%"+self.cari+"%"))
      cur.execute(sql)
      dt = cur.fetchall()
      for kdsp,nmsp,cara_bayar,lama_bayar,minfaktur,minorder,satuanbeli,hdabeli,discon,disconrp,hdj in dt:
         dtlist.append({'kdsp':kdsp,'nmsp':nmsp,'cara_bayar':cara_bayar,'lama_bayar':lama_bayar,'minfaktur':minfaktur,'minorder':minorder,'satuanbeli':satuanbeli,'hdabeli':hdabeli,'discon':discon,'disconrp':disconrp,'hdj':hdj})
      conn.close()
      return jsonify({'data':dtlist})
   def cari_pemasok(self):
      lnk = request.form['link']
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      sql = "SELECT kdsp, nmsp, alamat, telepon FROM SUPLIER WHERE kdsp='" + self.cari + "'"
      cur.execute(sql)
      dt = cur.fetchone()
      if dt is not None:
         kdsp = str(dt[0])
         nmsp = str(dt[1])
         almt = str(dt[2])
         telp = str(dt[3])
         conn.close()
         return jsonify({'status':0, 'kdsp':kdsp, 'nmsp':nmsp, 'almt':almt, 'telp':telp})
      else:
         conn.close()
         return render_template(lnk, cari=self.cari)

   def cari_pemasoktukarfps(self):
      lnk = request.form['link']
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      sql = "SELECT kdsp, nmsp, alamat, telepon,alamat2,kontak,email,lama_bayar,rekening,bank FROM SUPLIER WHERE kdsp='" + self.cari + "'"
      cur.execute(sql)
      dt = cur.fetchone()
      if dt is not None:
         kdsp = str(dt[0])
         nmsp = str(dt[1])
         almt = str(dt[2])
         telp = str(dt[3])
         alamat2=str(dt[4])
         kontak=str(dt[5])
         email=str(dt[6])
         tempo=str(dt[7])
         rekening=str(dt[8])
         bank=str(dt[9])
         conn.close()
         return jsonify({'status':0, 'kdsp':kdsp, 'nmsp':nmsp, 'almt':almt, 'telp':telp,'alamat2':alamat2,'kontak':kontak,'rekening':rekening,'bank':bank,'email':email,'tempo':tempo})
      else:
         conn.close()
         return render_template(lnk, cari=self.cari)   
   def pop_cari_pemasokgd(self):
      prinsipal =request.args.get('prinsipal', None)
      kdregional =request.args.get('kdregional', None)
      dtlist = []
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      if prinsipal == "":
         sql = "Select kdsp, nmsp, alamat, telepon from SUPLIER where NMSP like '%" + self.cari + "%'and stspbf = 0 or \
                     NMSP like '%" + self.cari + "%' and stspbf = 1 or kdsp = '" + self.cari + "' and stspbf = 1"
      else:
         sql = "Select kdsp, nmsp, alamat, telepon from SUPLIER2 where NMSP like '%" + self.cari + "%'and KD_PRINSIP = '" + prinsipal + "'and kd_wilayah = '" + kdregional + "'and stspbf = 0 or KDSP like '%" + self.cari + "%'and KD_PRINSIP = '" + prinsipal + "'"
         # sql = "Select kdsp, nmsp, alamat, telepon from SUPLIER2 where NMSP like '%" + self.cari + "%'and KD_PRINSIP = '" + prinsipal + "'and kd_wilayah = '" + kdregional + "'and stspbf = 0 or \
         #             NMSP like '%" + self.cari + "%'and KD_PRINSIP = '" + prinsipal + "'and stspbf = 1 and kd_prinsip = '" + prinsipal + "' or kdsp = '" + self.cari + "' and stspbf = 1  and kd_wilayah <> '" + kdregional + "'"
      cur.execute(sql)
      dt = cur.fetchall()
      for kdsp, nmsp, almt, telp in dt:
         dtlist.append({'kdsp':kdsp, 'nmsp':nmsp, 'almt':almt, 'telp':telp})
      conn.close()
      return jsonify({'data':dtlist})

   def pop_cari_kontakpemasokgd(self):
      tglminta =request.args.get('tglminta', None)
      dtlist = []
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      sql = "select DISTINCT a.kdsp,b.nmsp as nmsp ,b.alamat,b.telepon from verifikasipesanan a INNER JOIN SUPLIER b ON a.kdsp = b.kdsp where a.no_rekap = '" + tglminta + "' and a.rencanakirim = '' "
      cur.execute(sql)
      dt = cur.fetchall()
      for kdsp, nmsp, almt, telp in dt:
         dtlist.append({'kdsp':kdsp, 'nmsp':nmsp, 'almt':almt, 'telp':telp})
      conn.close()
      return jsonify({'data':dtlist})

   def pop_cari_pemasoktukarfps(self):
      dtlist = []
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      sql = "Select kdsp, nmsp, alamat, telepon from SUPLIER where NMSP like '%" + self.cari + "%'"
      cur.execute(sql)
      dt = cur.fetchall()
      for kdsp, nmsp, almt, telp in dt:
         dtlist.append({'kdsp':kdsp, 'nmsp':nmsp, 'almt':almt, 'telp':telp})
      conn.close()
      return jsonify({'data':dtlist})

   def pop_cari_pemasokkonfgd(self):
      kdobat =request.args.get('kdobat', None)
      kdlokasi =request.args.get('kdlokasi', None)
      dtlist = []
      sql = "Select kdsp,nmsp,discon,discoff,satuanbeli,stdbeli from HARGADIS where  nmsp like '%" + self.cari +  "%'and kdbr = '" + kdobat +  "'and kd_client = '" + kdlokasi +"' and stdbeli = 'Ya'   order by stdbeli desc,nmsp"
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      cur2 = conn.cursor()
      cur.execute(sql)
      dt = cur.fetchall()
      for kdsp,nmsp,discon,discoff,satuanbeli,stdbeli in dt:
         sql2 = "select kd_suplier,disc,satuanbeli from stdbelanja where kd_obat = '" + kdobat + "'and kd_suplier = '" + kdsp + "'"
         cur2.execute(sql2)
         dt2 = cur2.fetchone()
         if dt2 is not None:
            xdisc = dt2[1]-discoff
            xsatuanbeli = dt2[2]
         else:
            xdisc = discon
            xsatuanbeli = satuanbeli
         dtlist.append({'kdsp':kdsp, 'nmsp':nmsp,'discon':xdisc,'discoff':discoff,'satuanbeli':xsatuanbeli,'stdbeli':stdbeli})
      conn.close()
      return jsonify({'data':dtlist})
      
   def cari_pemasokspgd(self):
      lnk = request.form['link']
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      cur2 = conn.cursor()
      kdapotek = request.form['kdapotek']
      cur.execute( "select distinct a.kdsp,a.nmsp,b.alamat,b.telepon,b.minorder from TMPSP3 a INNER JOIN SUPLIER b ON a.kdsp = b.kdsp where a.kdsp ='%s' and lokasi = '%s'" %(self.cari,kdapotek))
      # cur.execute("SELECT kdsp, nmsp, alamat, telepon FROM SUPLIER WHERE kdsp='%s'"\ %(nmpenanggungjawab, noijin, masaberlaku, status,kdsp))
      #             % self.cari)
      dt = cur.fetchone()
      if dt is not None:
         kdsp = str(dt[0])
         nmsp = str(dt[1])
         almt = str(dt[2])
         telp = str(dt[3])
         minorder=str(dt[4])
         # Hitung Total Order
         xtotalsp = '0'
         cur2.execute("select sum(hrgjadi*qty) as total from TMPSP3 where kdsp = '" + kdsp + "'")
         dt2 = cur2.fetchone()
         if dt2 is not None:
            xtotalsp = str(dt2[0])
        
         xkurang = str((int(minorder) - int(xtotalsp)))
         xkurang2 = str((int(minorder) - int(xtotalsp)))
         xtotalsp = "{:,}".format(int(xtotalsp))
         xkurang = "{:,}".format(int(xkurang))
         minorder = "{:,}".format(int(minorder))
         conn.close()
         return jsonify({'status':0, 'kdsp':kdsp, 'nmsp':nmsp, 'almt':almt, 'telp':telp,'minorder':minorder, 'totalsp':xtotalsp,'kurang':xkurang,'kurang2':xkurang2})
      else:
         conn.close()
         return render_template(lnk, cari=self.cari,kdapotek=kdapotek)
   
   # Gels New
   def pop_cari_pemasokspgd(self):
      dtlist = []
      kdapotek =request.args.get('kdapotek', None)
      conn = _mod_conn.connectdbgd()
      cur = conn.cursor()
      sql = "select distinct a.kdsp,a.nmsp,b.alamat,b.telepon,b.minorder from TMPSP3 a INNER JOIN SUPLIER b ON a.kdsp = b.kdsp WHERE a.nmsp LIKE'%s' and lokasi='%s' ORDER BY a.nmsp" % ("%"+self.cari+"%",kdapotek)
      cur.execute(sql)
      # cur.execute("SELECT kdsp, nmsp, alamat, telepon FROM SUPLIER \
      #             WHERE nmsp LIKE'%s' ORDER BY nmsp" % ("%"+self.cari+"%"))
      dt = cur.fetchall()
      for kdsp, nmsp, almt, telp,minorder in dt:
         dtlist.append({'kdsp':kdsp, 'nmsp':nmsp, 'almt':almt, 'telp':telp,'minorder':minorder})
      conn.close()
      return jsonify({'data':dtlist})
