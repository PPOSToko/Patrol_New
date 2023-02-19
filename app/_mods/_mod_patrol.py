from flask import session, request, jsonify,render_template,url_for
from app import _mod_conn
from datetime import datetime, timedelta
import random
class cls_mst_patrol:
    @staticmethod
    def trx_patrol():
        # lnk = request.form['link']
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur2 = conn.cursor()
        sql = "select idpatrol from _settupdata"
        cur.execute(sql)
        dt = cur.fetchone()
        if dt is not None:
            idpatrol = dt[0] + 1
            cur2.execute("update _settupdata set idpatrol = '" + str(dt[0] + 1) + "'")
            conn.commit()
        petugas = session['username']
        lnk = "/_patrol/start.html"
        return render_template(lnk,idpatrol=idpatrol,petugas=petugas)
    @staticmethod
    def list_unfinish():
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur2 = conn.cursor()
        lnk = "/_patrol/listunfinish.html"
        petugas = session['username']
        return render_template(lnk,petugas=petugas)
    @staticmethod
    def simpan_patrol():
            #  'nminduk':nminduk,'nmleader':nmleader,'idpatrol':idpatrol,'operator':operator
        idinduk = request.form['nminduk']
        idleader = request.form['nmleader']
        idpatrol = request.form['idpatrol']
        idoperator = request.form['operator']
        idpetugas = session['username']
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur2 = conn.cursor()
        tglskr = datetime.now()
        # Cek Pertanyaan
        sql = "select count(*) as jml from pertanyaan where id_induk = '" + idinduk + "'"
        cur.execute(sql)
        dt = cur.fetchone()
        if dt[0] > 1:
            cur.execute("select id_patrol,id_petugas from patrol_header where id_patrol = '" + idinduk + "'")
            dt = cur.fetchone()
            if dt is None:
                sql2 = "insert into patrol_header set id_petugas = '" + idpetugas + "', id_patrol = '" + idpatrol + "',id_korlap = '" + idleader + "',id_induk = '"\
                        + idinduk + "',id_karyawan = '" + idoperator + "',star_date = '" + str(tglskr) + "'"
                cur2.execute(sql2)
                conn.commit()
            return jsonify({'status':1})   
        else:
            msg = "Master pertanyaan kurang dari 2, Patrol tidak bisa dimulai"
            return jsonify({'status':0,'msg':msg}) 
    @staticmethod
    def detil_viewpatrol():
        idpatrol = request.args.get('idpatrol', None)
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        sql = "SELECT a.id_pertanyaan,b.pertanyaan,b.std_jawaban,a.score,a.remark FROM patrol_line a INNER JOIN pertanyaan b ON a.id_pertanyaan = b.id_pertanyaan where id_patrol = '" + idpatrol + "' and flag_jawab = 'V'"
        cur.execute(sql)
        dt = cur.fetchall()
        dtlist = []
        i = 0
        for id_pertanyaan,pertanyaan,std_jawaban,score,remark in dt:
            i = i +1
            if score == 1:
                hasil = "Sesuai"
            else:
                hasil = "Tidak Sesuai"
            remark = remark
            dtlist.append({'nourut':i,'id_pertanyaan':id_pertanyaan,'pertanyaan':pertanyaan,'std_jawaban':std_jawaban,'hasil':hasil,'remark':remark})
        conn.close()
        return jsonify({'data':dtlist})

    @staticmethod
    def detil_editviewpatrol():
        idpatrol = request.args.get('idpatrol', None)
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        sql = "SELECT a.id_pertanyaan,b.pertanyaan,b.std_jawaban,a.score,a.remark FROM patrol_line a INNER JOIN pertanyaan b ON a.id_pertanyaan = b.id_pertanyaan where id_patrol = '" + idpatrol + "' and flag_jawab = 'V'"
        cur.execute(sql)
        dt = cur.fetchall()
        dtlist = []
        i = 0
        for id_pertanyaan,pertanyaan,std_jawaban,score,remark in dt:
            i = i +1
            if score == "1":
                hasil = "Sesuai"
            else:
                hasil = "Tidak Sesuai"
            remark = remark
            dtlist.append({'nourut':i,'id_pertanyaan':id_pertanyaan,'pertanyaan':pertanyaan,'std_jawaban':std_jawaban,'hasil':hasil,'remark':remark})
        conn.close()
        return jsonify({'data':dtlist})


    @staticmethod
    def view_patrol():
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        petugas = session['username']
        lnk = "/_patrol/view_patrol.html"
        level = session['level']
        print(level)
        return render_template(lnk,petugas=petugas,level=level)

    @staticmethod
    def stop_hasilpatrol():
        status = request.form['status']
        idpatrol = request.form['idpatrol']        
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        # 1. Finish , 0. Unfinish
        tglskr = datetime.now()
        if status == "Unfinish":
            xstatus = 0
        else:
            xstatus = 1
        if xstatus == 1 :
            sql = "update patrol_header set status = '" + str(xstatus) + "',stop_date = '" + str(tglskr) + "',finishdate = '" + str(tglskr) + "' where id_patrol = '" + idpatrol + "'"
            print(sql)
            cur.execute(sql)    
        else:
            sql = "update patrol_header set status = '" + str(xstatus) + "',stop_date = '" + str(tglskr) + "' where id_patrol = '" + idpatrol + "'"
            print(sql)
            cur.execute(sql)
        conn.commit()
        return jsonify({'status':1}) 

    @staticmethod
    def simpan_hasilpatrol():
        hasil = request.form['hasil']
        if hasil == "Sesuai":
            xscore = 1
            xhasil = 1
        else:
            xscore = 0
            xhasil = 0
        idpatrol = request.form['idpatrol']
        idpertanyaan = request.form['idpertanyaan']
        remark = request.form['remark']
        tglskr = datetime.now()
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur.execute("update patrol_line set flag_jawab = 'V',status = '" + str(xhasil) + "',remark = '" + remark + "',score = '"+ str(xscore) + "',answer_date = '" + str(tglskr) + "' where id_patrol = '" + str(idpatrol) + "' and id_pertanyaan = '"+ str(idpertanyaan) + "'")
        conn.commit()
        msg="Sukses"
        return jsonify({'status':1,'msg':msg}) 
    @staticmethod
    def edit_hasilpatrol():
        idpatrol= request.form['idpatrol']
        idpertanyaan = request.form['idpertanyaan']
        hasil = request.form['hasil']
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur.execute("UPDATE patrol_line set score = '" + str(hasil) + "'where id_patrol = '" + str(idpatrol) + "' and id_pertanyaan = '"+ str(idpertanyaan) + "'")
        conn.commit()
        msg="Sukses"
        return jsonify({'status':1,'msg':msg}) 
    @staticmethod
    def edit_remarkpatrol():
        idpatrol= request.form['idpatrol']
        idpertanyaan = request.form['idpertanyaan']
        remark = request.form['remark']
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur.execute("UPDATE patrol_line set remark = '" + str(remark) + "'where id_patrol = '" + str(idpatrol) + "' and id_pertanyaan = '"+ str(idpertanyaan) + "'")
        conn.commit()
        msg="Sukses"
        return jsonify({'status':1,'msg':msg}) 

    @staticmethod
    def edit_historypatrol():
        idpatrol= request.args.get('idpatrol', None)
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur2 = conn.cursor()
        dtlist=[]
        sql = "select id_patrol,id_korlap,id_karyawan,id_petugas,star_date,status,id_induk from patrol_header where id_patrol = '" + idpatrol + "'"
        cur.execute(sql)
        dt = cur.fetchone()
        if dt is not None:
            idpatrol=dt[0]
            cur2.execute("select id_induk,description from induk where id_induk = '" + str(dt[6]) + "'")
            dt2 = cur2.fetchone()
            if dt2 is not None:
                nminduk = dt2[1]
            else:
                nminduk = ""
            cur2.execute("select id_karyawan,nama from petugas where id_karyawan = '" + dt[1] + "' and jabatan = '1'")
            dt2 = cur2.fetchone()
            if dt2 is not None:
                korlap = dt2[1]
            cur2.execute("select id_karyawan,nama from petugas where id_karyawan = '" + dt[2] + "' and jabatan = '0'")
            dt2 = cur2.fetchone()
            if dt2 is not None:
                operator = dt2[1]
            else:
                operator = "-"
            petugas = dt[3]
            star_date=dt[4]
            sql2 = "select count(*) as jawab from patrol_line where id_patrol = '" + str(dt[0]) + "' and flag_jawab = 'V'"
            cur2.execute(sql2)
            dt2 = cur2.fetchone()
            if dt2 is not None:
                totaltanya = dt2[0]
            else:
                totaltanya = 0

            sql2 = "select count(*) as jawab from patrol_line where id_patrol = '" + str(dt[0]) + "' and  flag_jawab = 'V' and score = 1"
            cur2.execute(sql2)
            dt2 = cur2.fetchone()
            if dt2 is not None:
                jmljawab = dt2[0]
            else:
                jmljawab = 0
            if totaltanya == 0:
                score = 0
            else:
                score = str(round((jmljawab /totaltanya) * 100)) + "%"
            if dt[5] == 1:
                xstatus = "Finished"
            else:
                xstatus = "Unfinished"

        lnk = "/_patrol/update_patrol.html"
        return render_template(lnk,idpatrol=idpatrol,korlap=korlap,operator=operator,petugas=petugas,score=score,status=xstatus,nminduk=nminduk,
                               star_date=star_date)

    @staticmethod
    def detil_historypatrol():
        idpatrol= request.args.get('idpatrol', None)
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur2 = conn.cursor()
        dtlist=[]
        #               0         1         2         3           4           5        6       7
        sql = "select id_patrol,id_korlap,id_karyawan,id_petugas,star_date,status,id_induk from patrol_header where id_patrol = '" + idpatrol + "'"
        cur.execute(sql)
        dt = cur.fetchone()
        if dt is not None:
            idpatrol=dt[0]
            cur2.execute("select id_induk,description from induk where id_induk = '" + str(dt[6]) + "'")
            dt2 = cur2.fetchone()
            if dt2 is not None:
                nminduk = dt2[1]
            else:
                nminduk = ""
            cur2.execute("select id_karyawan,nama from petugas where id_karyawan = '" + dt[1] + "' and jabatan = '1'")
            dt2 = cur2.fetchone()
            if dt2 is not None:
                korlap = dt2[1]
            cur2.execute("select id_karyawan,nama from petugas where id_karyawan = '" + dt[2] + "' and jabatan = '0'")
            dt2 = cur2.fetchone()
            if dt2 is not None:
                operator = dt2[1]
            else:
                operator = "-"
            petugas = dt[3]
            star_date=dt[4]
            sql2 = "select count(*) as jawab from patrol_line where id_patrol = '" + str(dt[0]) + "' and flag_jawab = 'V'"
            cur2.execute(sql2)
            dt2 = cur2.fetchone()
            if dt2 is not None:
                totaltanya = dt2[0]
            else:
                totaltanya = 0

            sql2 = "select count(*) as jawab from patrol_line where id_patrol = '" + str(dt[0]) + "' and  flag_jawab = 'V' and score = 1"
            cur2.execute(sql2)
            dt2 = cur2.fetchone()
            if dt2 is not None:
                jmljawab = dt2[0]
            else:
                jmljawab = 0
            if totaltanya == 0:
                score = 0
            else:
                score = str(round((jmljawab /totaltanya) * 100)) + "%"
            if dt[5] == 1:
                xstatus = "Finished"
            else:
                xstatus = "Unfinished"
            
        lnk = "/_patrol/view_detail.html"
        return render_template(lnk,idpatrol=idpatrol,korlap=korlap,operator=operator,petugas=petugas,score=score,status=xstatus,xnminduk=nminduk,star_date=star_date)

    @staticmethod
    def view_historypatrol():
        idleader= request.args.get('idleader', None)
        idinduk = request.args.get('idinduk', None)
        # d.idleader = idleader,d.idinduk= idinduk,d.idopr=idopr,d.start_from=start_from,d.start_to=start_to,d.status=status;
        # idinduk = request.form['idinduk'] 
        # idopr = request.form['idopr']
        # status = request.form['status']
        # start_from = request.form['start_from']
        # start_to = request.form['start_to']
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur2 = conn.cursor()
        # Isi Score
        dtlist=[]
        if idleader == "" and idinduk == "":
            sql = "select id_patrol,id_petugas,id_induk,star_date,status,total_score,id_korlap,id_karyawan from patrol_header where id_petugas = '" + session['username'] + "'"    
        elif idinduk == "":
            sql = "select id_patrol,id_petugas,id_induk,star_date,status,total_score,id_korlap,id_karyawan from patrol_header where id_petugas = '" + session['username'] + "' and id_korlap = '" + idleader + "'"    
        else:    
            sql = "select id_patrol,id_petugas,id_induk,star_date,status,total_score,id_korlap,id_karyawan from patrol_header where id_petugas = '" + session['username'] + "' and id_korlap = '" + idleader + "' and id_induk = '" + idinduk + "'"
        cur.execute(sql)
        dt = cur.fetchall()
        for id_patrol,id_petugas,id_induk,star_date,status,total_score,id_korlap,id_karyawan in dt:
            sql2 = "select id_karyawan,nama from petugas where id_karyawan = '" + id_korlap + "'"
            cur2.execute(sql2)
            dt2 = cur2.fetchone()
            if dt2 is not None:
                nmkorlap = dt2[1]
            else:
                nmkorlap = ""    
            sql2 = "select id_karyawan,nama from petugas where id_karyawan = '" + id_karyawan + "'"
            cur2.execute(sql2)
            dt2 = cur2.fetchone()
            if dt2 is not None:
                nmoperator = dt2[1]
            else:
                nmoperator = ""    

            sql2 = "select count(*) as jawab from patrol_line where id_patrol = '" + str(id_patrol) + "' and flag_jawab = 'V'"
            cur2.execute(sql2)
            dt2 = cur2.fetchone()
            if dt2 is not None:
                totaltanya = dt2[0]
            else:
                totaltanya = 0
            sql2 = "select id_induk,description from induk where id_induk = '" + str(id_induk) + "'"
            cur2.execute(sql2)
            dt2 = cur2.fetchone()
            if dt2 is not None:
                nminduk = dt2[1]
            else:
                nminduk = ""
            sql2 = "select count(*) as jawab from patrol_line where id_patrol = '" + str(id_patrol) + "' and  flag_jawab = 'V' and score = 1"
            cur2.execute(sql2)
            dt2 = cur2.fetchone()
            if dt2 is not None:
                jmljawab = dt2[0]
            else:
                jmljawab = 0
            if totaltanya == 0:
                score = 0
            else:
                score = str(round((jmljawab /totaltanya) * 100)) + "%"
            if status == 1:
                xstatus = "Finished"
            else:
                xstatus = "Unfinished"
            dtlist.append({'id_patrol':id_patrol,'nminduk':nminduk,'petugas':id_petugas,'start_date':star_date,'status':xstatus,'score':score,'nmkorlap':nmkorlap,'nmoperator':nmoperator})
            
        return jsonify({'data':dtlist})
        # return render_template(lnk,nminduk=nminduk,operator=operator,leader=leader)

    @staticmethod
    def mulaipatrol():
        idpatrol = request.args.get('idpatrol',None)
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur2 = conn.cursor()
        cur3 = conn.cursor()
        cur4 = conn.cursor()
        cur5 = conn.cursor()
        cur.execute("select id_induk,id_korlap,id_karyawan from patrol_header where id_patrol ='" + idpatrol + "'")
        dt = cur.fetchone()
        if dt is not None:
            operator =  session['username']
            idinduk = str(dt[0])
        # Cek point yg ada dipertanyaan
        cur.execute("select id_point,id_pertanyaan from pertanyaan where id_induk = '" + idinduk + "' GROUP BY id_point")
        dt = cur.fetchall()
        i = 0
        tanya1 = []
        tanya2 = []
        tanya3 = []
        tanya4 = []
        tanya5 = []

        for id_point,id_pertanyaan in dt:
            i = i +1
            cur2.execute("select id_point,id_pertanyaan from pertanyaan where id_induk = '" + str(idinduk) + "' and id_point = '" + str(id_point) +"'" )
            dt2 = cur2.fetchall()
            for id_point,id_pertanyaan in dt2:
                if i == 1 :
                    tanya1.append(str(id_pertanyaan))
                elif i == 2:
                    tanya2.append(str(id_pertanyaan))
                elif i == 3:
                    tanya3.append(str(id_pertanyaan))
                elif i == 4:
                    tanya4.append(str(id_pertanyaan))
                elif i == 5:
                    tanya5.append(str(id_pertanyaan))
        sect1 =[tanya1,tanya2,tanya3,tanya4,tanya5]
        #diberi nilai awal = true
        cek = True
        result_list = []
        #loop while yg running terus selama variabel cek = true
        while cek == True:
            #loop for utk memproses semua major point, 1 per 1
            for mp in range(len(sect1)):
                mp_list = sect1[mp]
                
                #cek anggota major point, apakah anggota >= 2
                if len(mp_list) >= 2:
                    #jika >= 2, ambil 2 anggota scr random
                    #2 anggota yg ter-ambil, dihapus dari major point
                    a = random.choice(mp_list)
                    mp_list.remove(a)
                    b = random.choice(mp_list)
                    mp_list.remove(b)
                    
                    #masukkan 2 anggota terambil ke list hasil
                    result_list.append(a)
                    result_list.append(b)
                
                elif len(mp_list) == 1:
                    #jika anggota tinggal 1, ambil 1 anggota tsb
                    #hapus anggota terambil dari major point
                    a = mp_list[0]
                    mp_list.remove(a)
                    
                    #masukkan anggota terambil ke list hasil
                    result_list.append(a)
                
                #jika anggota < 2, major point di-skip
                else:
                    continue
                
                #timpa major point dgn kondisi baru setelah 2 anggota dihapus
                sect1[mp] = mp_list
            
            #update value variabel cek, apakah masih true
            for mp_list in sect1:
                #jika ada 1 saja major point yg masih ada anggota nya, cek masih true
                if len(mp_list) > 0:
                    cek = True
                    break
                #jika semua major point anggota nya habis, cek menjadi false
                else:
                    cek = False
        # print("hasil shuffle :")
        result_str = ""         
        for s in range(len(result_list)):
            # SImpan hasil ke database
            sql = "select id_pertanyaan,id_point from pertanyaan where id_pertanyaan = '" + result_list[s] + "'"
            cur.execute(sql)
            dt = cur.fetchone()
            if dt is not None:
                sql2 = "select id_patrol,id_pertanyaan from patrol_line where id_patrol = '" + idpatrol + "'and id_pertanyaan = '" + str(dt[0]) + "'"
                cur2.execute(sql2)
                dt2 = cur2.fetchone()
                if dt2 is None:
                    sql3 = "insert into patrol_line set id_patrol = '" + idpatrol + "',id_pertanyaan = '" + str(dt[0]) + "',id_point = '" +str(dt[1])  + "'" 
                    cur3.execute( sql3)
                    conn.commit()
        
        
        
        # print(tanya)
        cur.execute("select id_induk,description from induk where id_induk = '" + idinduk + "'")
        dt = cur.fetchone()
        if dt is not None:
            nminduk = dt[1]
        # Total Pertanyaan
        cur.execute("select count(*) as total from patrol_line  where id_patrol = '" + idpatrol + "'")
        dt = cur.fetchone()
        if dt is not None:
            totaltanya = dt[0]
        else:
            totaltanya = 1
        # cur.execute("select count(*) as total from patrol_line  where id_patrol = '" + idpatrol + "' and flag_jawab = 'V'")
        # dt = cur.fetchone()
        # if dt is not None:
        #     mulai = dt[0] + 1
        # else:
        #     mulai=1
        xsesuai = 0
        xtdksesuai = 0
        mulai = 0
        mulai2 = 0
        cur.execute("select score,status from patrol_line  where id_patrol = '" + idpatrol + "' and flag_jawab = 'V'")
        dt = cur.fetchall()
        for score,status in dt:
            if score == 1:
                xsesuai = xsesuai + 1
            else:
                xtdksesuai = xtdksesuai + 1
            mulai = mulai + 1
        if mulai == 0:
            mulai = 1
        mulai2 = mulai + 1

        cur4.execute("select id_pertanyaan,id_point from patrol_line where flag_jawab = 'X' and id_patrol = '" + idpatrol + "' order by id_line limit 1")    
        dt4 = cur4.fetchall()
        idtanya1=""
        pertanyaan1 = ""
        stdjwb1 = ""
        nmpoint = ""
        xurut = 0
        for id_pertanyaan,id_point in dt4:
            xurut = xurut + 1
            cur5.execute("select id_point,pertanyaan,std_jawaban from pertanyaan where id_pertanyaan = '" + str(id_pertanyaan) + "'")
            dt5 = cur5.fetchone()
            if dt5 is not None:
                if xurut == 1 :
                    idtanya1 = id_pertanyaan
                    pertanyaan1 = dt5[1]
                    stdjwb1 = dt5[2]
                else:
                    idtanya2 = id_pertanyaan
                    pertanyaan2 = dt5[1]
                    stdjwb2 = dt5[2]
            cur5.execute("select id_point,description from point where id_point = '" + str(id_point) + "'") 
            dt5 = cur5.fetchone()
            if dt5 is not None:
                nmpoint = dt5[1]
            else:
                nmpoint = "-"
        psesuai = round((xsesuai / totaltanya) * 100)
        ptdksesuai =round((xtdksesuai / totaltanya) * 100)
        lnk = "/_patrol/patrol.html"
        return render_template(lnk,nminduk=nminduk,operator=operator,idpertanyaan=idtanya1,idpatrol=idpatrol,pertanyaan1=pertanyaan1,stdjwb1=stdjwb1,mulai=mulai,selesai=totaltanya,nmpoint=nmpoint,sesuai =xsesuai,tdksesuai=xtdksesuai,mulai2=mulai2,psesuai=psesuai,ptdksesuai=ptdksesuai)
