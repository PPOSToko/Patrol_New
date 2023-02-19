from flask import request, render_template, jsonify
from app import _mod_conn

class cls_view_mainmenu:
    # Menu
    @staticmethod
    def tblview_menu():
        dtlist = []
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur.execute("SELECT id_mm, des_mm, icon, aktif FROM _mainmenu")
        dt = cur.fetchall()
        for idmm, desmm, icon, aktif in dt:
            dtlist.append({'idmm':idmm, 'desmm':desmm, 'icon':icon, 'aktif':aktif})
        conn.close()
        return jsonify({'data':dtlist})

    @staticmethod
    def list_menu():
        listmenu = []
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur.execute("SELECT id_mm, des_mm FROM _mainmenu WHERE aktif='1'")
        dt = cur.fetchall()
        for idmm, desmm in dt:
            listmenu.append({'idmm':idmm, 'desmm':desmm})
        conn.close()
        return listmenu
    
    @staticmethod        
    def detil_menu():
        com = request.form['com']
        lnk = request.form['link']
        idmm = request.form['idmm']
        desmm = request.form['desmm']
        icon = request.form['icon']
        return render_template(lnk, com=com, idmm=idmm, desmm=desmm, icon=icon)
    
    # SubMenu
    @staticmethod
    def list_submenu():
        idmenu = request.form['idmenu']
        listsubmenu = []
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur.execute("SELECT id_mn, des_mn FROM _menu WHERE id_mm='%s' AND aktif='1'" % idmenu)
        dt = cur.fetchall()
        for idmn, desmn in dt:
            listsubmenu.append({'idmn':idmn, 'desmn':desmn})
        conn.close()
        return listsubmenu

    # Sub Menu
    @staticmethod
    def tblview_submenu():
        dtlist = []
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur.execute("SELECT a.id_mn,a.des_mn,a.id_mm,b.des_mm,a.icon,a.lnk,a.aktif,a.info \
                    FROM _menu a INNER JOIN _mainmenu b ON b.id_mm = a.id_mm")
        dt = cur.fetchall()
        for idmn, desmn, idmm, desmm, icon, link, aktif, info in dt:
            dtlist.append({'idmn':idmn, 'desmn':desmn, 'idmm':idmm, 'desmm':desmm, \
                        'icon':icon, 'link':link, 'aktif':aktif, 'info':info})
        conn.close()
        return jsonify({'data':dtlist})
    
    @staticmethod
    def detil_submenu():
        com = request.form['com']
        lnk = request.form['link']
        idmn = request.form['idmn']
        desmn = request.form['desmn']
        idmm = request.form['idmm']
        icon = request.form['icon']
        linked = request.form['linked']
        info = request.form['info']
        return render_template(lnk, com=com, idmn=idmn, desmn=desmn, icon=icon, idmm=idmm, linked=linked, info=info)
    
class cls_action_mainmenu:
    # Menu
    @staticmethod
    def status_aktif_menu():
        idmm = request.form['idmm']
        aktif = request.form['aktif']
        conn = _mod_conn.connectdb()
        if aktif == '1':
            try:
                cur = conn.cursor()
                cur.execute("UPDATE _mainmenu SET aktif='%s' WHERE id_mm='%s'" % ('0', idmm))
            except:
                conn.close()
                msg = 'Data gagal dinon-aktifkan !'
                return jsonify({'status':0, 'msg':msg})
            else:
                conn.commit()
                conn.close()
                msg = 'Data berhasil dinon-aktifkan.'
                return jsonify({'status':1, 'msg':msg})
        else:
            
            try:
                cur = conn.cursor()
                cur.execute("UPDATE _mainmenu SET aktif='%s' WHERE id_mm='%s'" % ('1', idmm))
            except:
                conn.close()
                msg = 'Data gagal diaktifkan !'
                return jsonify({'status':0, 'msg':msg})
            else:
                conn.commit()
                conn.close()
                msg = 'Data berhasil diaktifkan.'
                return jsonify({'status':1, 'msg':msg})

    @staticmethod
    def simpan_menu():
        desmm = request.form['desmm']
        icon = request.form['icon']
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur.execute("SELECT id_mm FROM _mainmenu ORDER BY id_mm DESC LIMIT 1")
        dt = cur.fetchone()
        if dt is None:
            idmm = '001'
            cur.close()
        else:
            idmm = str(int(dt[0])+1).zfill(3)
            cur.close()

        try:
            cur2 = conn.cursor()
            cur2.execute("INSERT INTO _mainmenu (id_mm,des_mm,icon,lnk,aktif) \
                        VALUES ('%s','%s','%s','%s','%s')" \
                        % (idmm, desmm, icon, 'gridmenu.html', '1'))
        except:
            conn.close()
            msg = "Data gagal disimpan !"
            return jsonify({'status':0, 'msg':msg})
        else:
            conn.commit()
            conn.close()
            msg = "Data berhasil disimpan."
            return jsonify({'status':1, 'msg':msg})

    @staticmethod
    def rubah_menu():
        idmm = request.form['idmm']
        desmm = request.form['desmm']
        icon = request.form['icon']
        conn = _mod_conn.connectdb()
        try:
            cur = conn.cursor()
            cur.execute("UPDATE _mainmenu SET des_mm='%s', icon='%s' \
                        WHERE id_mm='%s'" % (desmm, icon, idmm))
        except:
            conn.close()
            msg = "Data gagal diperbaharui !"
            return jsonify({'status':0, 'msg':msg})
        else:
            conn.commit()
            conn.close()
            msg = "Data berhasil diperbaharui !"
            return jsonify({'status':1, 'msg':msg})

    # Sub Menu
    @staticmethod
    def status_aktif_submenu():
        idmn = request.form['idmn']
        aktif = request.form['aktif']
        conn = _mod_conn.connectdb()
        if aktif == '1':
            try:
                cur = conn.cursor()
                cur.execute("UPDATE _menu SET aktif='%s' WHERE id_mn='%s'" % ('0', idmn))
            except:
                conn.close()
                msg = 'Data gagal dinon-aktifkan !'
                return jsonify({'status':0, 'msg':msg})
            else:
                conn.commit()
                conn.close()
                msg = 'Data berhasil dinon-aktifkan.'
                return jsonify({'status':1, 'msg':msg})
        else:
            
            try:
                cur = conn.cursor()
                cur.execute("UPDATE _menu SET aktif='%s' WHERE id_mn='%s'" % ('1', idmn))
            except:
                conn.close()
                msg = 'Data gagal diaktifkan !'
                return jsonify({'status':0, 'msg':msg})
            else:
                conn.commit()
                conn.close()
                msg = 'Data berhasil diaktifkan.'
                return jsonify({'status':1, 'msg':msg})

    @staticmethod
    def simpan_submenu():
        idmm = request.form['idmm']
        desmn = request.form['desmn']
        icon = request.form['icon']
        linked = request.form['linked']
        info = request.form['info']

        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur.execute("SELECT id_mn FROM _menu ORDER BY id_mn DESC LIMIT 1")
        dt = cur.fetchone()
        if dt is None:
            idmn = '001'
            cur.close()
        else:
            idmn = str(int(dt[0])+1).zfill(3)
            cur.close()
        
        try:
            cur2 = conn.cursor()
            cur2.execute("INSERT INTO _menu (id_mn,id_mm,des_mn,icon,lnk,aktif,info) \
                        VALUES ('%s','%s','%s','%s','%s','%s','%s')" \
                        % (idmn, idmm, desmn, icon, linked, '1', info))
        except:
            conn.close()
            msg = "Data gagal disimpan !"
            return jsonify({'status':0, 'msg':msg})
        else:
            conn.commit()
            conn.close()
            msg = "Data berhasil disimpan."
            return jsonify({'status':1, 'msg':msg})

    @staticmethod
    def rubah_submenu():
        idmn = request.form['idmn']
        idmm = request.form['idmm']
        desmn = request.form['desmn']
        icon = request.form['icon']
        linked = request.form['linked']
        info = request.form['info']

        conn = _mod_conn.connectdb()
        try:
            cur = conn.cursor()
            cur.execute("UPDATE _menu SET id_mm='%s', des_mn='%s', icon='%s', lnk='%s', info='%s' \
                        WHERE id_mn='%s'" % (idmm, desmn, icon, linked, info, idmn))
        except:
            conn.close()
            msg = "Data gagal diperbaharui !"
            return jsonify({'status':0, 'msg':msg})
        else:
            conn.commit()
            conn.close()
            msg = "Data berhasil diperbaharui."
            return jsonify({'status':1, 'msg':msg})