from flask import request, render_template, jsonify
from werkzeug.utils import secure_filename
import os, shutil
from app import _mod_conn
import datetime
import pathlib

now = datetime.datetime.now()
tgl = now.strftime('%Y-%m-%d')

# Image Format Uploads
UPLOAD_FOLDER = 'static/uploads/'
STORE_UPLOAD = 'static/img/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class cls_instansi:
    @staticmethod
    def get_dt_instansi():
        lnk = request.form['link']
        conn = _mod_conn.connectdb()
        cur = conn.cursor()
        cur.execute("SELECT kd_instansi, nm_instansi, no_izin, almt, kdpos, kota, tlp, fax, email, logo FROM _data_instansi")
        dt = cur.fetchone()
        if dt is None:
            com = 'create'
            conn.close()
            return render_template(lnk, com=com)
        else:
            com = 'update'
            kdinstansi = dt[0]
            nminstansi = dt[1]
            if dt[2] is None:
                noizin = ''
            else:
                noizin = dt[2]
            almt = dt[3]
            kdpos = dt[4]
            kota = dt[5]
            tlp = dt[6]
            fax = dt[7]
            email = dt[8]
            logo = dt[9]
            conn.close()
            return render_template(lnk, com=com, kdinstansi=kdinstansi, nminstansi=nminstansi, noizin=noizin, almt=almt, kdpos=kdpos,\
                                    kota=kota, tlp=tlp, fax=fax, email=email, logo=logo)
    
    @staticmethod
    def get_logo():
        file = request.files['file']
        if file and allowed_file(file.filename) :
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER,filename))
            msg = 'File berhasil diunggah.'
            img = file.filename
            return jsonify({'status':1, 'msg':msg, 'img':img})

    @staticmethod
    def simpan_dt_instansi():
        kdinstansi = request.form['kdinstansi']
        nminstansi = request.form['nminstansi']
        noizin = request.form['noizin']
        almt = request.form['almt']
        kdpos = request.form['kdpos']
        kota = request.form['kota']
        tlp = request.form['tlp']
        fax = request.form['fax']
        email = request.form['email']
        logo = request.form['logo']

        conn = _mod_conn.connectdb()
        try:
            cur = conn.cursor()
            cur.execute("INSERT INTO _data_instansi (kd_instansi, nm_instansi, no_izin, almt, kdpos, kota, tlp, fax, email, logo)\
                        VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (kdinstansi, nminstansi, noizin, almt, kdpos,\
                        kota, tlp, fax, email, logo))
        except:
            conn.close()
            msg = 'Data gagal disimpan !'
            return jsonify({'status':0, 'msg':msg})
        else:
            conn.commit()
            conn.close()
            msg = 'Data berhasil disimpan.'
            return jsonify({'status':1, 'msg':msg})

    @staticmethod
    def rubah_dt_instansi():
        kdinstansi = request.form['kdinstansi']
        nminstansi = request.form['nminstansi']
        noizin = request.form['noizin']
        almt = request.form['almt']
        kdpos = request.form['kdpos']
        kota = request.form['kota']
        tlp = request.form['tlp']
        fax = request.form['fax']
        email = request.form['email']
        logo = request.form['logo']

        conn = _mod_conn.connectdb()
        try:
            cur = conn.cursor()
            cur.execute("UPDATE _data_instansi SET nm_instansi='%s', no_izin='%s', almt='%s', kdpos='%s', kota='%s', tlp='%s', fax='%s', email='%s', logo='%s' \
                        WHERE kd_instansi='%s'" % (nminstansi, noizin, almt, kdpos, kota, tlp, fax, email, logo, kdinstansi))
        
            # if logo != 'None':
            #     shutil.move(UPLOAD_FOLDER+logo, STORE_UPLOAD+logo)
            file = pathlib.Path(UPLOAD_FOLDER+logo)
            if file.exists():
                shutil.move(UPLOAD_FOLDER+logo, STORE_UPLOAD+logo)

        except:
            conn.close()
            msg = 'Data gagal diperbaharui !'
            return jsonify({'status':0, 'msg':msg})
        else:
            conn.commit()
            # conn.close()
            # if logo != 'None':
            #     shutil.move(UPLOAD_FOLDER+logo, STORE_UPLOAD+logo)
            msg = 'Data berhasil diperbaharui.'
            return jsonify({'status':1, 'msg':msg})