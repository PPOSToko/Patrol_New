from flask import session, request, jsonify, render_template, json
import datetime
import time
from app import _mod_conn
class cls_actemployee:
    @staticmethod
    def employee():
        lnk = "/_employe/employee.html"
        return render_template(lnk)
    @staticmethod
    def view_employee():
        # d.idempolyee = id_employee,d.nama_employee = nama_employee,d.jabatan_employee=jabatan_employee;
        idemploye = request.args.get('idemployee', None)
        nmemployee = request.args.get('nama_employee', None)
        status_employee =request.args.get('status_employee', None) 
        jabatan_employee = request.args.get('jabatan_employee', None) 
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        dtlist=[]
        if status_employee == "" and jabatan_employee == "":
            cur.execute("select id_karyawan,nama,jabatan,status from petugas where nama like '%" + nmemployee + "%'  order by id_karyawan")
        elif status_employee == "" and jabatan_employee != "":
            cur.execute("select id_karyawan,nama,jabatan,status from petugas where nama like '%" + nmemployee + "%'  and jabatan = '" + jabatan_employee + "' order by id_karyawan")
        elif status_employee != "" and jabatan_employee != "":
            cur.execute("select id_karyawan,nama,jabatan,status from petugas where nama like '%" + nmemployee + "%'  and jabatan = '" + jabatan_employee + "'  and status = '" + status_employee + "' order by id_karyawan")
        else:    
            cur.execute("select id_karyawan,nama,jabatan,status from petugas where nama like '%" + nmemployee + "%' and status = '" + status_employee + "' order by id_karyawan")
        dt = cur.fetchall()
        for id_karyawan,nama,jabatan,status in dt:
            if jabatan == "1":
                xjabatan = "Leader"
            else:
                xjabatan = "Operator"
            if status == "1":
                xstatus = "Aktif"
            else:
                xstatus = "Non Aktif"    
            dtlist.append({'id_karyawan':id_karyawan,'nama':nama,'jabatan':xjabatan,'status':xstatus})
        conn.close()
        return jsonify({'data':dtlist})
    @staticmethod
    def simpan_employee():
        nama_employee = request.form['nama_employee']
        jabatan_employee = request.form['jabatan_employee']
        status_employee = request.form['status_employee']
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur2 = conn.cursor()
        sql = "select id_karyawan,nama from petugas where nama = '" + nama_employee + "'"
        cur.execute(sql)
        dt = cur.fetchone()
        if dt is None:
            sql2 = "insert into petugas set nama = '" + nama_employee + "',jabatan = '" + str(jabatan_employee ) + "',status = '" + str(status_employee) + "'"
            cur2.execute(sql2)
            conn.commit()
            msg = "Data sukses disimpan !"
            conn.close()
            return json.dumps({"status":1, "msg":msg})

        else:
            conn.close()
            msg = "Data Sudah Ada"
            return json.dumps({"status":0, "msg":msg})
    @staticmethod
    def edit_employee():
        id_employee = request.form['id_employee']
        nama_employee = request.form['nama_employee']
        jabatan_employee = request.form['jabatan_employee']
        status_employee = request.form['status_employee']
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur2 = conn.cursor()
        sql = "select id_karyawan,nama from petugas where id_karyawan = '" + id_employee + "'"
        cur.execute(sql)
        dt = cur.fetchone()
        if dt is None:
            conn.close()
            msg = "Data tidak Ada"
            return json.dumps({"status":0, "msg":msg})
        else:
            sql2 = "update petugas set nama = '" + nama_employee + "',jabatan = '" + str(jabatan_employee ) + "',status = '" + str(status_employee) + "' where id_karyawan = '" + id_employee + "'"
            cur2.execute(sql2)
            conn.commit()
            msg = "Data sukses disimpan !"
            conn.close()
            return json.dumps({"status":1, "msg":msg})
    
class cls_actusr:
    @staticmethod
    def create_user():
        lnk = "/_users/create_user.html"
        return render_template(lnk)
    @staticmethod
    def list_user():
        lnk = "/_users/manage_user.html"
        return render_template(lnk)
    @staticmethod
    def nonaktif_user():
        username = request.form['userid']
        status = request.form['status']
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur.execute("update _users set aktif = '" + status + "' where username = '" + username + "'")
        conn.commit()
        conn.close()
        msg = "Kata Sandi sukses direset !"
        return json.dumps({"status":1, "msg":msg})

    @staticmethod
    def reset_password():
        username = request.form['userid']
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur.execute("update _users set password = md5('1234567890') where username = '" + username + "'")
        conn.commit()
        conn.close()
        msg = "Kata Sandi sukses direset !"
        return json.dumps({"status":1, "msg":msg})

    @staticmethod
    def viewlist_user():
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        dtlist=[]
        cur.execute("select username,nama,level,aktif from _users   order by nama")
        dt = cur.fetchall()
        for username,nama,level,aktif in dt:
            if level == "1":
                xlevel = "Inspektor"
            elif level == "2":
                xlevel = "Admin"
            elif level == "3":  
                xlevel = "Developer"              
            if aktif == "1":
                xstatus = "Aktif"
            else:
                xstatus = "Non Aktif"    
            dtlist.append({'username':username,'nama':nama,'level':xlevel,'status':xstatus})
        conn.close()
        return jsonify({'data':dtlist})    

    @staticmethod
    def akses_user():
        lnk = "/_users/akses_user.html"
        return render_template(lnk)
    @staticmethod
    def rubah_password():
        lnk = "/_users/rubah_password.html"
        return render_template(lnk)
    @staticmethod
    def cek_aksesuser():
        xlevel =  request.form['level']
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        mn01 = "X"
        mn02 = "X"
        mn03 = "X"
        mn04 = "X"
        mn05 = "X"
        mn06 = "X"
        mn07 = "X"
        mn08 = "X"
        mn09 = "X"
        mn10 = "X"
        mn11 = "X"
        mn12 = "X"
        mn13 = "X"
        mn14 = "X"

        cur.execute("select mn01,mn02,mn03,mn04,mn05,mn06,mn07,mn08,mn09,mn10,mn11,mn12,mn13,mn14 from _aksesmenu where level = '" + xlevel + "'")
        dt = cur.fetchone()
        if dt is not None:
            mn01 = dt[0]
            mn02 = dt[1]
            mn03 = dt[2]
            mn04 = dt[3]
            mn05 = dt[4]
            mn06 = dt[5]
            mn07 = dt[6]
            mn08 = dt[7]
            mn09 = dt[8]
        conn.close()    
        return json.dumps({"status":1, "mn01":mn01, "mn02":mn02, "mn03":mn03, "mn04":mn04, "mn05":mn05, "mn06":mn06, "mn07":mn07, "mn08":mn08, "mn09":mn09})
    @staticmethod
    def simpan_password():
        lama = request.form['lama']    
        baru1 = request.form['baru1']
        baru2 = request.form['baru2']
        username = session['username']
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur2 = conn.cursor()
        sql = "SELECT * FROM _users WHERE username=BINARY('%s') AND password='%s'" % (username, lama)
        print(sql)
        cur.execute("SELECT * FROM _users WHERE username=BINARY('%s') AND password='%s'" % (username, lama))
        dt = cur.fetchone() 
        if dt is None:
            cur.close()
            conn.close()
            msg = "Kata Sandi lama Tidak Cocok !"
            return json.dumps({"status":0, "msg":msg})
        else:
            cur2.execute("update _users set password = md5('"+baru1+ "') where username = '" + username + "'")
            conn.commit()
            conn.close()
            msg = "Kata Sandi sukses dirubah !"
            return json.dumps({"status":1, "msg":msg})
    @staticmethod 
    def simpan_akses():
        level = request.form['jabatan']
        if request.form['mn01'] == "true":
            mn01 = "V"
        else:
            mn01 = "X"            
        if request.form['mn02'] == "true":
            mn02 = "V"
        else:
            mn02 = "X"            
        if request.form['mn03'] == "true":
            mn03 = "V"
        else:
            mn03 = "X"            
        if request.form['mn04'] == "true":
            mn04 = "V"
        else:
            mn04 = "X"            
        if request.form['mn05'] == "true":
            mn05 = "V"
        else:
            mn05 = "X"            
        if request.form['mn06'] == "true":
            mn06 = "V"
        else:
            mn06 = "X"            
        if request.form['mn07'] == "true":
            mn07 = "V"
        else:
            mn07 = "X"            
        if request.form['mn08'] == "true":
            mn08 = "V"
        else:
            mn08 = "X"            
        if request.form['mn09'] == "true":
            mn09 = "V"
        else:
            mn09 = "X"            
        if request.form['mn10'] == "true":
            mn10 = "V"
        else:
            mn10 = "X"            
        if request.form['mn11'] == "true":
            mn11 = "V"
        else:
            mn11 = "X"            
        if request.form['mn12'] == "true":
            mn12 = "V"
        else:
            mn12 = "X"            
        if request.form['mn13'] == "true":
            mn13 = "V"
        else:
            mn13 = "X"            
        if request.form['mn14'] == "true":
            mn14 = "V"
        else:
            mn14 = "X"            

        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur2 = conn.cursor()
        cur.execute("select level,mn01 from _aksesmenu where level = '" + level + "'")
        dt = cur.fetchone()
        if dt is None:
            sql2 = "insert into _aksesmenu set level = '" + level + "',mn01 = '" + mn01 +"',mn02 = '" + mn02 + "',mn03 = '" +mn03 + "',mn04 = '" + mn04 + "',mn05 = '" \
                +mn05 + "',mn06 = '" + mn06 + "',mn07 = '" + mn07 + "',mn08 = '" + mn08 + "',mn09 = '" + mn09 + "',mn10 = '" + mn10 + "',mn11 = '" + mn11 + "',mn12 = '" \
                + mn12  + "',mn13 ='" + mn13 + "',mn14 = '" + mn14 + "'"
            cur2.execute(sql2)
            conn.commit()
            conn.close()
            msg = "Akses User sukses dibuat"
            return jsonify({'status':1,'msg':msg}) 
        else:
            sql2 = "update _aksesmenu set mn01 = '" + mn01 +"',mn02 = '" + mn02 + "',mn03 = '" +mn03 + "',mn04 = '" + mn04 + "',mn05 = '" \
                +mn05 + "',mn06 = '" + mn06 + "',mn07 = '" + mn07 + "',mn08 = '" + mn08 + "',mn09 = '" + mn09 + "',mn10 = '" + mn10 + "',mn11 = '" + mn11 + "',mn12 = '" \
                + mn12  + "',mn13 ='" + mn13 + "',mn14 = '" + mn14 + "' where level = '" + level + "'"
            cur2.execute(sql2)
            conn.commit()
            conn.close()
            msg = "Akses User sukses diedit"
            return jsonify({'status':1,'msg':msg}) 

    @staticmethod
    def simpan_user():
        iduser = request.form['iduser']
        username = request.form['username']
        jabatan=request.form['jabatan']
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur2 = conn.cursor()
        sql = "select username,nama from _users where username = '" + iduser + "'"
        cur.execute(sql)
        dt = cur.fetchone()
        if dt is None:
            sql2 = "insert into _users set username ='" + iduser + "',nama = '" + username + "',password = md5('1234567890'),level = '"+ jabatan + "'" 
            cur2.execute(sql2)
            conn.commit()
            conn.close()
            msg = "User sukses dibuat"
            return jsonify({'status':1,'msg':msg}) 
        else:
            conn.close()
            msg = "User sudah ada !"
            return jsonify({'status':0,'msg':msg}) 



