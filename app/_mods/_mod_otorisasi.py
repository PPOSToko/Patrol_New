from flask import request, jsonify
from app import _mod_conn

class cls_view_otoritas:
    @staticmethod
    def get_otoritasmenu():
        usrname = request.args.get('usrname', None)
        dtlist = []
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur.execute("SELECT a.username,a.id_mm,b.des_mm,a.id_mn,c.des_mn \
                    FROM _menuotr AS a \
                    INNER JOIN _mainmenu AS b ON b.id_mm = a.id_mm \
                    INNER JOIN _menu c ON c.id_mn = a.id_mn WHERE a.username='%s'" % usrname)
        dt = cur.fetchall()
        for username, idmm, desmm, idmn, desmn in dt:
            dtlist.append({'usrname':username, 'idmm':idmm, 'desmm':desmm, 'idmn':idmn, 'desmn':desmn})
        conn.close()
        return jsonify({'data':dtlist})

    @staticmethod
    def tblview_sub_menu_oto():
        idmenu = request.args.get('idmenu', None)
        dtlist = []
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur.execute("SELECT id_mn, des_mn FROM _menu WHERE id_mm='%s' AND aktif='1'" % idmenu)
        dt = cur.fetchall()
        for idmn, desmn in dt:
            dtlist.append({'idmn':idmn, 'desmn':desmn})
        conn.close()
        return jsonify({'data':dtlist})

class cls_action_otorisasi:
    @staticmethod
    def simpan_otorisasi():
        usrname = request.form['usrname']
        idmenu = request.form['idmenu']
        idsmenu = request.form['idsmenu']
        conn= _mod_conn.connectdb()
        cur = conn.cursor()
        cur.execute("SELECT * FROM _menuotr WHERE username='%s' AND id_mm='%s' AND id_mn='%s'"\
                    % (usrname, idmenu, idsmenu))
        dt = cur.fetchone()
        if dt is None:
            try:
                cur2 = conn.cursor()
                cur2.execute("INSERT INTO _menuotr(username, id_mm, id_mn) VALUES ('%s','%s','%s')"\
                % (usrname, idmenu,idsmenu))
            except:
                conn.close()
                msg = 'Data Gagal Disimpan !'
                return jsonify({'status':0,'msg':msg})
            else:
                conn.commit()
                conn.close()
                msg = 'Data Berhasil Disimpan.'
                return jsonify({'status':1,'msg':msg})
        else:
            conn.close()
            msg = 'Data Sudah Tersedia !'
            return jsonify({'status':0,'msg':msg})
    
    @staticmethod
    def hapus_otorisasi():
        usrname = request.form['usrname']
        idmenu = request.form['idmenu']
        idsmenu = request.form['idsmenu']
        conn = _mod_conn.connectdb()
        try:
            cur = conn.cursor()
            cur.execute("DELETE FROM _menuotr WHERE username='%s' AND id_mm='%s' AND id_mn='%s'" \
            % (usrname, idmenu, idsmenu))
        except:
            conn.close()
            msg = 'Data Gagal Dihapus !'
            return jsonify({'status':0,'msg':msg})
        else:
            conn.commit()
            conn.close()
            msg = 'Data Berhasil Dihapus.'
            return jsonify({'status':1,'msg':msg})