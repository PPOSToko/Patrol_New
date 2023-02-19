from flask import session, request, jsonify,render_template
from app import _mod_conn
from datetime import datetime, timedelta
class cls_mst_question:
    @staticmethod
    def mst_question():
        # lnk = request.form['link']
        lnk = "/_mst_question/create.html"
        return render_template(lnk)
    @staticmethod 
    def mst_induk():        
        # lnk = "/_mst_question/new_induk.html"
        lnk = "/_mst_question/listinduk.html"
        return render_template(lnk)
    @staticmethod 
    def mst_induk_point():        
        lnk = "/_mst_question/new_induk.html"
        return render_template(lnk)

    @staticmethod 
    def view_point():
        idinduk = request.args.get('kdinduk', None)
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        dtlist=[]
        sql = "select id_point,description from point where id_induk = '" + idinduk + "'"
        cur.execute(sql)
        dt = cur.fetchall()
        for id_point,description in dt:
            dtlist.append({'id_point':id_point,'description':description})            
        conn.close()
        return jsonify({'data':dtlist})
    @staticmethod
    def view_induk():
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        dtlist=[]
        sql = "select id_induk,description,status from induk order by id_induk "
        cur.execute(sql)
        dt = cur.fetchall()
        for id_point,description,status in dt:
            if status == "1":
                xstatus = "Aktif"
            else:
                xstatus = "Non Aktif"
            dtlist.append({'id_induk':id_point,'description':description,'status':xstatus})            
        conn.close()
        return jsonify({'data':dtlist})

    @staticmethod
    def viewunfinishpatrol():
        userpatrol = session['username']
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur2 = conn.cursor()
        dtlist=[]
        # Stop yang sudah melewati batas hari 
        tglskr = datetime.today() - timedelta(days=1)
        tglskr = tglskr.strftime('%Y-%m-%d')
        jamskr = datetime.today().strftime('%H:%M:%S')
        print(jamskr)
        sql = "update patrol_header set status = 1,finishdate = stop_date where STR_TO_DATE(star_date,'%Y-%m-%d') <= STR_TO_DATE('" + tglskr + "','%Y-%m-%d')"
        cur.execute(sql)
        conn.commit()
        # Untuk yg lebih dari 90 Menit
        sql = "select a.id_patrol,b.description,a.star_date,a.stop_date from patrol_header a INNER JOIN induk b ON a.id_induk = b.id_induk where a.id_petugas = '" + userpatrol + "' and a.status = 0"
        cur.execute(sql)
        dt = cur.fetchall()
        for id_patrol,nm_induk,star_date,stop_date in dt:
            jamstop = star_date.strftime('%H:%M:%S')
            t1 = datetime.strptime(jamskr, "%H:%M:%S")
            t2 = datetime.strptime(jamstop, "%H:%M:%S")
            jamselisih = t1 - t2
            if (jamselisih.total_seconds()/60) > 90:
                sql2 = "update patrol_header set status = 1,finishdate = stop_date where id_patrol = '" + str(id_patrol) + "'"
                cur2.execute(sql2)
                conn.commit()
        sql = "select a.id_patrol,b.description,a.star_date,a.stop_date from patrol_header a INNER JOIN induk b ON a.id_induk = b.id_induk where a.id_petugas = '" + userpatrol + "' and a.status = 0"
        cur.execute(sql)
        dt = cur.fetchall()
        for id_patrol,nm_induk,star_date,stop_date in dt:
            sql2 = "select count(*) as jawab from patrol_line where id_patrol = '" + str(id_patrol) + "' and flag_jawab = 'V'"
            cur2.execute(sql2)
            dt2 = cur2.fetchone()
            if dt2 is not None:
                totaltanya = dt2[0]
            else:
                totaltanya = 0

            sql2 = "select count(*) as jawab from patrol_line where id_patrol = '" + str(id_patrol) + "' and  flag_jawab = 'V' and score = 1"
            cur2.execute(sql2)
            dt2 = cur2.fetchone()
            if dt2 is not None:
                jmljawab = dt2[0]
            else:
                jmljawab = 0
            if totaltanya == 0:
                progress = 0
            else:
                progress = str(round((jmljawab /totaltanya) * 100)) + "%"

            jammulai = star_date.strftime('%d %b %Y %H:%M:%S')
            dtlist.append({'id_patrol':id_patrol,'nminduk':nm_induk,'star_date':jammulai,'stop_date':stop_date,'dijawab':jmljawab,'progress':progress})            
        conn.close()
        return jsonify({'data':dtlist})
    @staticmethod
    def simpan_induk():
        nminduk = request.form['nminduk']
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur2 = conn.cursor()
        cur2.execute("select description from induk where description = '" + nminduk + "'")
        dt2 = cur2.fetchone()
        if dt2 is None:
            cur.execute("insert into induk set description = '" + nminduk + "',status = '1'")
            conn.commit()
            conn.close()
            msg = 'Data berhasil disimpan.'
            return jsonify({'status':1, 'msg':msg})
        else:
            conn.close()
            msg = 'Nama Induk tidak boleh sama'
            return jsonify({'status':0, 'msg':msg})

    @staticmethod
    def edit_induk():
        # 'nminduk':enminduk,'idinduk':eidinduk,'status':estatus
        idinduk = request.form['idinduk']
        nminduk = request.form['nminduk']
        status = request.form['status']
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur.execute("update induk set description = '" + nminduk + "',status = '" + status + "' where id_induk = '" + idinduk + "'")
        conn.commit()
        conn.close()
        msg = 'Data berhasil diedit.'
        return jsonify({'status':1, 'msg':msg})

    @staticmethod
    def simpan_point():
        nminduk = request.form['nminduk']
        nmpoint = request.form['nmpoint']
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur.execute("insert into point set description = '" + nmpoint + "',id_induk = '" + nminduk + "'")
        conn.commit()
        conn.close()
        msg = 'Data berhasil disimpan.'
        return jsonify({'status':1, 'msg':msg})
    @staticmethod
    def edit_point():
        idinduk = request.form['idinduk']
        nmpoint = request.form['nmpoint']
        idpoint = request.form['idpoint']
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur.execute("update point set description = '" + nmpoint + "' where id_point = '" + idpoint + "'")
        conn.commit()
        conn.close()
        msg = 'Data berhasil diedit.'
        return jsonify({'status':1, 'msg':msg})

    @staticmethod
    def viewpertanyaan():
        induk = request.args.get('induk', None)
        point = request.args.get('point', None)
        xpertanyaan=request.args.get('pertanyaan', None)
        xjawaban=request.args.get('stdjawaban', None)
        if xjawaban == None:
            xjawaban = ""
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur2 = conn.cursor()
        dtlist=[]
        if induk == "" and point == "" and xpertanyaan == "" and xjawaban == "":
            sql = "select id_pertanyaan,pertanyaan,std_jawaban,eff_from,eff_to,id_point,id_induk from pertanyaan order by id_induk"    
        elif induk == "" and point == "" and xpertanyaan != "" and xjawaban == "":                        
            sql = "select id_pertanyaan,pertanyaan,std_jawaban,eff_from,eff_to,id_point,id_induk from pertanyaan where  pertanyaan like '%" + xpertanyaan + "%'"    
        elif induk == "" and point == "" and xpertanyaan == "" and xjawaban != "":                        
            sql = "select id_pertanyaan,pertanyaan,std_jawaban,eff_from,eff_to,id_point,id_induk from pertanyaan where  std_jawaban like '%" + xjawaban+ "%'"    
        elif induk == "" and point == "" and xpertanyaan != "" and xjawaban != "":                        
            sql = "select id_pertanyaan,pertanyaan,std_jawaban,eff_from,eff_to,id_point,id_induk from pertanyaan where  std_jawaban like '%" + xjawaban+ "%' and pertanyaan like '%" + xpertanyaan + "%'"    
        elif induk == "" and point != "" and xpertanyaan != "" and xjawaban != "":                        
            sql = "select id_pertanyaan,pertanyaan,std_jawaban,eff_from,eff_to,id_point,id_induk from pertanyaan where  id_point = '" + point + "' and std_jawaban like '%" + xjawaban+ "%' and pertanyaan like '%" + xpertanyaan + "%'"    
        elif induk !="" and point == "" and xpertanyaan == "" and xjawaban == "":
            sql = "select id_pertanyaan,pertanyaan,std_jawaban,eff_from,eff_to,id_point,id_induk from pertanyaan where id_induk = '" + induk + "'"        
        elif induk !="" and point != "" and xpertanyaan == "" and xjawaban == "":
            sql = "select id_pertanyaan,pertanyaan,std_jawaban,eff_from,eff_to,id_point,id_induk from pertanyaan where id_induk = '" + induk + "'and id_point = '" + point + "' "        

        else:            
            if point =="":
                sql = "select id_pertanyaan,pertanyaan,std_jawaban,eff_from,eff_to,id_point,id_induk from pertanyaan where id_induk = '" + induk + "'  or pertanyaan like '%" + xpertanyaan + "%' or std_jawaban like '%" + xjawaban + "%'"
            else:
                sql = "select id_pertanyaan,pertanyaan,std_jawaban,eff_from,eff_to,id_point,id_induk from pertanyaan where id_induk = '" + induk + "' and id_point = '" + point + "' and pertanyaan like '%" + xpertanyaan + "%' and std_jawaban like '%" + xjawaban + "%'"
        
        cur.execute(sql)
        dt = cur.fetchall()
        for id_pertanyaan,pertanyaan,std_jawaban,eff_from,eff_to,id_point,id_induk in dt:
            sql2 = "select id_induk,description from induk where id_induk = '" + str(id_induk) + "'"
            cur2.execute(sql2)
            dt2 = cur2.fetchone()
            if dt2 is None:
                nminduk = "-"
            else:
                nminduk = dt2[1]

            now = eff_from
            sql2 = "select id_point,description from point where id_point = '" + str(id_point) + "'"
            cur2.execute(sql2)
            dt2 = cur2.fetchone()
            if dt2 is None:
                nmpoint = "-"
            else:
                nmpoint = dt2[1]

            if now == "0000-00-00":
                tgl = "00"
                bln= "00"
                thn = "0000"
                efffrom = "00/00/0000"
            else:
                tgl = now.day
                bln = now.month
                thn = now.year
                efffrom = str(tgl) + "/" + str(bln) + "/" + str(thn)
            now2 = eff_to
            if now2 == "0000-00-00":
                effto = "00/00/0000"
            else:
                tgl2 = now2.day
                bln2 = now2.month
                thn2 = now2.year
                effto = str(tgl2) + "/" + str(bln2) + "/" + str(thn2)
            dtlist.append({'id_pertanyaan':id_pertanyaan,'nminduk':nminduk,'nmpoint':nmpoint,'pertanyaan':pertanyaan,'std_jawaban':std_jawaban,'eff_from':efffrom,'eff_to':effto})
        conn.close()
        return jsonify({'data':dtlist})

    @staticmethod
    def detil_pertanyaan():
      lnk = request.form['link']
      com = request.form['com']
      return render_template(lnk, com=com)
class cls_cari_pertnyaan:
    # def __init__(self, cari=None):
    #     self.cari = cari
    @staticmethod
    def cari_point():
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        datapoint=[]
        induk = request.form['induk']
        # cur.execute("SELECT id_point, description FROM point \
        #             WHERE id_point like '%s' OR description like '%s' ORDER BY description" \
        #             % ('%'+cari+'%', '%'+cari+'%'))
        sql = "select id_point,description from point where id_induk = '" + induk + "'"
        cur.execute(sql)
        data = cur.fetchall()

        for id_point, description in data:
            datapoint.append({'id':id_point, 'value':description})
        cur.close()
        return jsonify({'data':datapoint})
    @staticmethod
    def cari_induk():
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        datainduk=[]
        sql = "select id_induk,description from induk where status = 1 order by id_induk"
        cur.execute(sql)
        data = cur.fetchall()
        for id_induk, description in data:
            datainduk.append({'id':id_induk, 'value':description})
        cur.close()
        return jsonify({'data':datainduk})
    @staticmethod
    def cari_leader():
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        dataleader=[]
        sql = "select id_karyawan,nama from petugas  where jabatan = 1 and status = 1 order by nama"
        cur.execute(sql)
        data = cur.fetchall()

        for id_karyawan,nama in data:
            dataleader.append({'id':id_karyawan, 'value':nama})
        cur.close()
        return jsonify({'data':dataleader})
    @staticmethod
    def cari_opr():
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        dataopr=[]
        sql = "select id_karyawan,nama from petugas  where jabatan = 0 and status = 1 order by nama"
        cur.execute(sql)
        data = cur.fetchall()

        for id_karyawan,nama in data:
            dataopr.append({'id':id_karyawan, 'value':nama})
        cur.close()
        return jsonify({'data':dataopr})

class cls_simpan_pertnyaan:
    @staticmethod
    def simpan_pertanyaan():
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur2 = conn.cursor()
        cur3 = conn.cursor()
        # 'induk':xinduk,'point':xpoint,'pertanyaan':xpertanyaan,'jawaban':xjawaban,'datefrom':xdatefrom,'dateto':xdateto;
        induk = request.form['induk']
        point = request.form['point']
        pertanyaan = request.form['pertanyaan']
        jawaban = request.form['jawaban']
        datefrom= request.form['datefrom']
        dateto=request.form['dateto']
        tglskr = datetime.now()
        sql = "select pertanyaan from pertanyaan where id_induk = '" + induk + "' and id_point = '" + point + "' and pertanyaan = '" + pertanyaan + "'"
        cur.execute(sql)
        dt = cur.fetchone()
        if dt is None:
            sql2 = "insert into pertanyaan set id_induk = '" + induk + "',id_point = '" + point + "',pertanyaan = '" + pertanyaan + "',std_jawaban = '" + \
                   jawaban + "',eff_from = '" + datefrom + "',eff_to = '" + dateto + "',user_input = '" + session['username'] + "',date_input ='" + str(tglskr) + "'"
            cur2.execute(sql2)
            conn.commit()
            conn.close()
            msg = 'Data berhasil disimpan.'
            return jsonify({'status':1, 'msg':msg})
        else:
            conn.close()
            msg = 'Data Sudah Ada.'
            return jsonify({'status':1, 'msg':msg})

    @staticmethod
    def edit_pertanyaan():
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur2 = conn.cursor()
        cur3 = conn.cursor()
        #   'idpertanyaan':xidpertanyaan,'pertanyaan':xpertanyaan,'jawaban':xjawaban,'datefrom':xdatefrom,'dateto':xdateto
        idpertanyaan = request.form['idpertanyaan']
        pertanyaan = request.form['pertanyaan']
        jawaban = request.form['jawaban']
        datefrom= request.form['datefrom']
        dateto=request.form['dateto']
        tglskr = datetime.now()
        sql = "select pertanyaan from pertanyaan where id_pertanyaan = '" + idpertanyaan + "'"
        cur.execute(sql)
        dt = cur.fetchone()
        if dt is not None:
            sql2 = "update pertanyaan set pertanyaan = '" + pertanyaan + "',std_jawaban = '" + \
                   jawaban + "',eff_from = '" + datefrom + "',eff_to = '" + dateto + "',user_input = '" + \
                   session['username'] + "',date_input ='" + str(tglskr) + "' where id_pertanyaan = '" + idpertanyaan + "'"
            cur2.execute(sql2)
            conn.commit()
            conn.close()
            msg = 'Data berhasil diupdate.'
            return jsonify({'status':1, 'msg':msg})
        else:
            conn.close()
            msg = 'Data Sudah Tidak Ada.'
            return jsonify({'status':1, 'msg':msg})

        
        
