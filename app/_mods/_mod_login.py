from flask import session, request, json, redirect,url_for
from app import _mod_conn

class cls_logins:
    @staticmethod
    def user_login():
        username = request.form['username']
        password = request.form['password']
        try:
            conn = _mod_conn.connectdb()
            cur = conn.cursor()
            sql = "SELECT * FROM _users WHERE username=BINARY('%s') AND password='%s'" % (username, password)
            cur.execute("SELECT * FROM _users WHERE username=BINARY('%s') AND password='%s'" % (username, password))
            dt = cur.fetchone() 
            if dt is None:
                cur.close()
                msg = "Nama Pengguna / Kata Sandi Tidak Cocok !"
                return json.dumps({"status":0, "msg":msg})
            else:
                # Aktif
                session['username'] = str(dt[0])
                session['level'] = str(dt[3])
                session['nama'] = str(dt[2])
                url = "/home"
                return json.dumps({"status":1,"url":url})
        finally:
            conn.close()
    
class cls_usermenu:
    def __init__(self, username=None, idmenu=None, nmmenu=None):
        self.username = username
        self.idmenu = idmenu
        self.nmmenu = nmmenu

    def mainmenu(self):
        conn = _mod_conn.connectdb()
        mmenu = []
        cur = conn.cursor()
        cur.execute("SELECT id_mm, des_mm, icon, lnk, aktif FROM _mainmenu")
        dt = cur.fetchall()
        for idmm, desmm, icon, lnk, aktif in dt:
            if session['level'] != '0':
                cur2 = conn.cursor()
                cur2.execute("SELECT id_mm FROM _menuotr \
                            WHERE username = '%s' AND id_mm = '%s' \
                            GROUP BY id_mm" % (self.username, idmm))
                dt2 = cur2.fetchone()
                if dt2 is None:
                    disabled = "disabled"
                    mmenu.append([idmm, desmm, icon, lnk, aktif, disabled])
                    cur2.close
                else:
                    disabled = ""
                    mmenu.append([idmm, desmm, icon, lnk, aktif, disabled])
                    cur2.close
            else:
                disabled = ""
                mmenu.append([idmm, desmm, icon, lnk, aktif, disabled])
        conn.close()
        return mmenu
    
    def menu(self):
        conn = _mod_conn.connectdb()
        menu = []
        cur = conn.cursor()
        if session['level'] != '0':
            cur.execute("SELECT a.id_mm, a.id_mn, b.des_mn, b.icon, b.lnk, b.info \
                        FROM _menuotr AS a \
                        INNER JOIN _menu AS b ON b.id_mn = a.id_mn \
                        WHERE a.username = '%s' AND a.id_mm = '%s'" \
                        % (self.username, self.idmenu))
            dt = cur.fetchall()
            for idmm, idmn, desmn, icon, lnk, info in dt:
                menu.append([idmm, idmn, desmn, icon, lnk, info])
            conn.close()
        else:
            cur.execute("SELECT id_mm,id_mn,des_mn,icon,lnk,info FROM _menu WHERE id_mm='%s'" % self.idmenu)
            dt = cur.fetchall()
            for idmm, idmn, desmn, icon, lnk, info in dt:
                menu.append([idmm, idmn, desmn, icon, lnk, info])
            conn.close()
        return menu
