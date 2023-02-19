from flask import session, request, jsonify, render_template, json
import datetime
import time
from app import _mod_conn

class cls_view_usr:
    @staticmethod
    def tblview_user():
        conn = _mod_conn.connectdb()
        dtlist = []
        cur = conn.cursor()
        cur2 = conn.cursor()
        # if session['level'] == '0':
        #     cur.execute("SELECT id, username, nama, email, level, DATE_FORMAT(tglreg, '%s') AS tglreg, aktif FROM _users"\
        #                 % "%d/%m/%Y %H:%i:%s")
        # else:
        cur.execute("SELECT a.id, a.username, a.nama, a.email, a.level, b.des, DATE_FORMAT(a.tglreg, '%s'), a.aktif, a.lokasi\
                     FROM _users a\
                     LEFT JOIN _user_level b ON b.id = a.level\
                     WHERE a.level<>'0'" % "%d/%m/%Y %H:%i:%s")
        dt = cur.fetchall()
        for id, username, nama, email, level, deslevel, tglreg, aktif,lokasi in dt:
            cur2.execute("select nmsp from CLIENT where kdsp = '" + lokasi + "'")
            dt2 = cur2.fetchone()
            if dt2 is not None:
                nm_lokasi = dt2[0]
            else:
                nm_lokasi = "-"

            dtlist.append({'id':id,'username':username, 'nama':nama, 'email':email, 'level':level,\
                           'deslevel':deslevel, 'tglreg':str(tglreg), 'aktif':aktif,'nm_lokasi':nm_lokasi})
        cur.close()
        conn.close()
        return jsonify({'data':dtlist})
    def tblview_group():
        conn = _mod_conn.connectdb()
        dtlist = []
        cur = conn.cursor()
        # if session['level'] == '0':
        #     cur.execute("SELECT id, username, nama, email, level, DATE_FORMAT(tglreg, '%s') AS tglreg, aktif FROM _users"\
        #                 % "%d/%m/%Y %H:%i:%s")
        # else:
        cur.execute("SELECT kd_group,nm_group from _user_group order by kd_group")
        dt = cur.fetchall()
        for kd_group,nm_group in dt:
            dtlist.append({'kd_group':kd_group,'nm_group':nm_group})
        cur.close()
        conn.close()
        return jsonify({'data':dtlist})
    
    @staticmethod
    def tblview_userdelegasi():
        conn = _mod_conn.connectdb()
        dtlist = []
        cur = conn.cursor()
        cur.execute("SELECT a.id,a.nama,b.des,a.flag_delegasi FROM _users a INNER JOIN _user_level b ON a.level = b.id and a.aktif = 1")
        dt = cur.fetchall()
        for id, nama, des, flag_delegasi in dt:
            dtlist.append({'id':id,'nama':nama, 'level':des, 'status':flag_delegasi})

        cur.close()
        conn.close()
        return jsonify({'data':dtlist})

    @staticmethod
    def detil_user():
        com = request.form['com']
        lnk = request.form['link']
        id = request.form['id']
        usrname = request.form['usrname']
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur.execute("SELECT id, username, nama, email, level, tglreg FROM _users WHERE id='%s' AND username='%s'" % (id,usrname))
        dt = cur.fetchone()
        if dt is not None:
            id = dt[0]
            uname = dt[1]
            nama = dt[2]
            email = dt[3]
            level = dt[4]
            if dt[5] == '' or dt[5] == None:
                tglreg = ''
            else:
                tglreg = dt[5]
            cur.close()
            conn.close()
            return render_template(lnk, com=com, id=id, uname=uname, nama=nama, email=email, level=level, tglreg=tglreg)
    @staticmethod
    def detil_userdelegasi():
        com = request.form['com']
        lnk = request.form['link']
        id = request.form['nik']
        nama = request.form['nama']
        return render_template(lnk, com=com, nik=id,  nama=nama,)

class cls_action_user:
    @staticmethod
    def status_aktif_user():
        id = request.form['id']
        usrname = request.form['usrname']
        aktif = request.form['aktif']
        conn = _mod_conn.connectdb()
        if aktif == '1':
            try:
                cur = conn.cursor()
                cur.execute("UPDATE _users SET aktif='%s' WHERE id='%s' AND username='%s'" % ('0', id, usrname))
            except:
                conn.close()
                msg = 'Pengguna gagal dinon-aktifkan !'
                return jsonify({'status':0, 'msg':msg})
            else:
                conn.commit()
                conn.close()
                msg = 'Pengguna berhasil dinon-aktifkan.'
                return jsonify({'status':1, 'msg':msg})
        else:
            
            try:
                cur = conn.cursor()
                cur.execute("UPDATE _users SET aktif='%s' WHERE username='%s'" % ('1', usrname))
            except:
                conn.close()
                msg = 'Pengguna gagal diaktifkan !'
                return jsonify({'status':0, 'msg':msg})
            else:
                conn.commit()
                conn.close()
                msg = 'Pengguna berhasil diaktifkan.'
                return jsonify({'status':1, 'msg':msg})

    @staticmethod
    def reset_katasandi():
        id = request.form['id']
        usrname = request.form['usrname']
        password = request.form['pass']

        conn = _mod_conn.connectdb()
        try:
            cur = conn.cursor()
            cur.execute("UPDATE _users SET password='%s' WHERE id='%s' AND username='%s'" % (password, id, usrname))
        except:
            conn.close()
            msg = "Kata Sandi gagal direset !"
            return jsonify({'status':0,'msg':msg})
        else:
            conn.commit()
            conn.close()
            msg = 'Kata Sandi berhasil direset.'
            return jsonify({'status':1, 'msg':msg})

    @staticmethod
    def simpan_user():
        usrname = request.form['usrname']
        passwd = request.form['passwd']
        nama = request.form['nama']
        email = request.form['email']
        level = request.form['level']
        kdsp =request.form['kdsp']
        tgl = str(time.strftime("%Y-%m-%d %H:%M:%S"))

        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur.execute("SELECT * FROM _users WHERE username='%s'" % usrname)
        dt = cur.fetchone()
        if dt is None:
            if level == '2':
                xid = request.form['id']
            else:
                cur2 = conn.cursor()
                cur2.execute("SELECT id FROM _users WHERE level<>0 AND level<>2 ORDER BY id DESC LIMIT 1")
                dt2 = cur2.fetchone()
                if dt2 is None:
                    cur2.close()
                    xid = 1
                else:
                    xid = str(int(dt2[0])+1)
                    cur2.close()
            try:
                cur3 = conn.cursor()
                cur3.execute("INSERT INTO _users (id, nama, username, password, email, level, aktif, tglreg,lokasi) \
                            VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (xid, nama, usrname, passwd, \
                            email, level, '1',  tgl,kdsp))
            except:
                conn.close()
                msg = 'Data Gagal diproses !'
                return jsonify({'status':0, 'msg':msg})
            else:
                conn.commit()
                conn.close()
                msg = 'Data Berhasil diproses !'
                return jsonify({'status':1, 'msg':msg})
        else:
            conn.close()
            msg = 'Nama Pengguna sudah tersedia !'
            return jsonify({'status':0, 'msg':msg})
    @staticmethod
    def rubah_delegasi():
        nik = request.form['nik']
        username = request.form['nik']
        tgldelegasi = request.form['tgldelegasi']
        conn = _mod_conn.connectdb()
        try:
            cur = conn.cursor()
            sql = "UPDATE _users set flag_delegasi = 'V',tgl_delegasi = '" + tgldelegasi + "' where id = '" + nik + "'"
            cur.execute(sql)
        except:
            conn.close()
            msg = 'Data gagal diproses !'
            return jsonify({'status':0, 'msg':msg})
        else:
            conn.commit()
            conn.close()
            msg = 'Data berhasil diproses.'
            return jsonify({'status':1, 'msg':msg})

    @staticmethod
    def rubah_user():
      oid = request.form['oid']
      ousrname = request.form['ousrname']
      id = request.form['id']
      usrname = request.form['usrname']
      nama = request.form['nama']
      email = request.form['email']
      level = request.form['level']

      conn = _mod_conn.connectdb()
      try:
         if level == '2':
            xid = id
         else:
            cur = conn.cursor()
            cur.execute("SELECT id FROM _users WHERE level<>0 AND level<>2 ORDER BY id DESC LIMIT 1")
            dt = cur.fetchone()
            if dt is None:
               cur.close()
               xid = 1
            else:
               xid = str(int(dt[0])+1)
               cur.close()

         cur2 = conn.cursor()
         cur2.execute("UPDATE _users SET id='%s', username='%s', nama='%s', email='%s', level='%s'\
                     WHERE id='%s' AND username='%s'" % (xid, usrname, nama, email, level, oid, ousrname))
         
         cur3 = conn.cursor()
         cur3.execute("UPDATE _menuotr SET username='%s' WHERE username='%s'" % (usrname, ousrname))
      except:
         conn.close()
         msg = 'Data gagal diproses !'
         return jsonify({'status':0, 'msg':msg})
      else:
         conn.commit()
         conn.close()
         msg = 'Data berhasil diproses.'
         return jsonify({'status':1, 'msg':msg})

    @staticmethod
    def cek_pass():
        id = request.form['id']
        usrname = request.form['usrname']
        passwd = request.form['passwd']
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur.execute("SELECT * FROM _users WHERE id='%s' AND username='%s' AND password='%s'" \
                    % (id, usrname, passwd))
        dt = cur.fetchone()
        if dt is None:
            conn.close()
            msg = 'Kata Sandi Anda Tidak Cocok !'
            return jsonify({'msg':msg, 'status':0})
        else:
            conn.close()
            status = 1
            return jsonify({'status':status})

    @staticmethod
    def rubah_pass():
        id = request.form['id']
        usrname = request.form['usrname']
        passwd = request.form['passbaru']

        conn = _mod_conn.connectdb()
        try:
            cur = conn.cursor()
            cur.execute("UPDATE _users SET password='%s' WHERE id='%s' AND username='%s'" % (passwd, id, usrname))
        except:
            conn.close()
            msg = 'Kata Sandi Gagal Dirubah !'
            return jsonify({'status':0, 'msg':msg})
        else:
            conn.commit()
            conn.close()
            msg = 'Kata Sandi Berhasil Dirubah !'
            return jsonify({'status':1, 'msg':msg})
