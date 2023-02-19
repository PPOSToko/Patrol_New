import calendar
import time
from datetime import datetime, timedelta

class cls_date_times:
    @staticmethod
    def cur_time():
        a=time.localtime()
        hr=a.tm_hour
        mn=a.tm_min
        sc=a.tm_sec
        return ('{}:{}:{}'.format(hr,mn,sc))

    @staticmethod
    def cur_time2():
        a=time.localtime()
        hr=a.tm_hour
        mn=a.tm_min
        # sc=a.tm_sec
        return ('{}:{}'.format(hr,mn))

    @staticmethod
    def iDate(param):
        # 0000-00-00 > 00/00/0000
        # 0123456789
        # 1234567890
        """
        Convert Date From yyyy-mm-dd To dd/mm/yyyy
        """
        d = param[8:10]
        m = param[5:7]
        y = param[0:4]
        tgl = d+'/'+m+'/'+y
        return tgl

    @staticmethod
    def mDate(param):
        # 00/00/0000 > 0000-00-00
        # 0123456789
        # 1234567890
        """
        Convert Date From dd/mm/yyyy To yyyy-mm-dd
        """
        d = param[0:2]
        m = param[3:5]
        y = param[6:10]
        tgl = y+'-'+m+'-'+d
        return tgl

    @staticmethod
    def iRupiah(param):
        return "${:,.2f}".format(param)

    @staticmethod
    def usia_thn(tgl_lhr, bln_lhr, thn_lhr):
        tgllhr = tgl_lhr+'/'+bln_lhr+'/'+thn_lhr
        tlahir = datetime.strptime(tgllhr, '%d/%m/%Y')
        lahir = tlahir.day + (tlahir.month * 30) + (tlahir.year * 365)

        now = datetime.now()
        tgl_now = now.day
        bln_now = now.month
        thn_now = now.year
        aktual = tgl_now + (bln_now * 30) + (thn_now * 365)

        tahun = (aktual - lahir) / 365
        return str(tahun)

    @staticmethod
    def usia_bln(tgl_lhr, bln_lhr, thn_lhr):
        tgllhr = tgl_lhr+'/'+bln_lhr+'/'+thn_lhr
        tlahir = datetime.strptime(tgllhr, '%d/%m/%Y')
        lahir = tlahir.day + (tlahir.month * 30) + (tlahir.year * 365)

        now = datetime.now()
        tgl_now = now.day
        bln_now = now.month
        thn_now = now.year
        aktual = tgl_now + (bln_now * 30) + (thn_now * 365)

        bulan = ((aktual - lahir) % 365) / 30
        return str(bulan)

    @staticmethod
    def usia_tgl(tgl_lhr, bln_lhr, thn_lhr):
        tgllhr = tgl_lhr+'/'+bln_lhr+'/'+thn_lhr
        tlahir = datetime.strptime(tgllhr, '%d/%m/%Y')
        lahir = tlahir.day + (tlahir.month * 30) + (tlahir.year * 365)

        now = datetime.now()
        tgl_now = now.day
        bln_now = now.month
        thn_now = now.year
        aktual = tgl_now + (bln_now * 30) + (thn_now * 365)

        hari = ((aktual - lahir) % 365) % 30
        return str(hari)

    @staticmethod
    def usia(tgl_lhr, bln_lhr, thn_lhr):
        tgllhr = tgl_lhr+'/'+bln_lhr+'/'+thn_lhr
        tlahir = datetime.strptime(tgllhr, '%d/%m/%Y')
        lahir = tlahir.day + (tlahir.month * 30) + (tlahir.year * 365)

        now = datetime.now()
        tgl_now = now.day
        bln_now = now.month
        thn_now = now.year

        aktual = tgl_now + (bln_now * 30) + (thn_now * 365)
        
        tahun = (aktual - lahir) / 365
        bulan = ((aktual - lahir) % 365) / 30
        hari = ((aktual - lahir) % 365) % 30

        umur = str(round(tahun, 0))+" Thn, "+str(bulan)+" Bln, "+str(hari)+" Hr"
        return str(umur)
    
    @staticmethod
    def hitHari(d1, d2):
        """
        d1 = Tanggal pertama, d2 = Tanggal berikutnya
        """
        tgl1 = datetime.strptime(d1, '%d/%m/%Y')
        tgl2 = datetime.strptime(d2, '%d/%m/%Y')
        per1 = tgl1.day + (tgl1.month * 30) + (tgl1.year * 365)
        per2 = tgl2.day + (tgl2.month * 30) + (tgl2.year * 365)
        hari = (((per2 - per1) % 365) % 30)+1
        return str(hari)

    @staticmethod
    def hitHari2(d1, d2):
        """
        d1 = Tanggal pertama, d2 = Tanggal berikutnya
        """
        tgl1 = datetime.strptime(d1, '%d/%m/%Y')
        tgl2 = datetime.strptime(d2, '%d/%m/%Y')
        per1 = tgl1.day + (tgl1.month * 30) + (tgl1.year * 365)
        per2 = tgl2.day + (tgl2.month * 30) + (tgl2.year * 365)
        # hari = (((per2 - per1) % 365) % 30)
        hari = (per2 - per1) / (1000 * 60 * 60 * 24)
        return str(hari)

    @staticmethod
    def curNameDay(tglsekarang):
        """
        Mencari nama hari berdasarkan tanggal sekarang format = "%Y-%m-%d" 
        """
        day = datetime.strptime(tglsekarang, '%Y-%m-%d').strftime('%w')
        hari = ""
        if int(day) == 0:
            hari = "Minggu"
        elif int(day) == 1:
            hari = "Senin"
        elif int(day) == 2:
            hari = "Selasa"
        elif int(day) == 3:
            hari = "Rabu"
        elif int(day) == 4:
            hari = "Kamis"
        elif int(day) == 5:
            hari = "Jumaat"
        elif int(day) == 6:
            hari = "Sabtu"
        else:
            hari = ""
        return hari
    
    @staticmethod
    def srcNameDay(tanggal):
        """
        Menentukan nama hari berdasarkan tanggal, Format = "%d/%m/%Y"
        """
        d = tanggal[0:2]
        m = tanggal[3:5]
        y = tanggal[6:10]
        dt = y+'-'+m+'-'+d
        getDay = datetime.strptime(dt, '%Y-%m-%d').strftime('%w')
        hari = ""
        if getDay == '0':
            hari = "Minggu"
        elif getDay == '1' :
            hari = "Senin"
        elif getDay == '2' :
            hari = "Selasa"
        elif getDay == '3' :
            hari = "Rabu"
        elif getDay == '4' :
            hari = "Kamis"
        elif getDay == '5' :
            hari = "Jumaat"
        elif getDay == '6' :
            hari = "Sabtu"
        else:
            hari = ""
        return hari

    @staticmethod
    def days_in_month(dt):
        return calendar.monthrange(dt.year, dt.month)[1]

    @staticmethod
    def monthly_range(dt_start, dt_end):
        forward = dt_end >= dt_start
        finish = False
        dt = dt_start

        while not finish:
            yield dt.date()
            if forward:
                days = cls_date_times.days_in_month(dt)
                dt = dt + timedelta(days=days)            
                finish = dt > dt_end
            else:
                _tmp_dt = dt.replace(day=1) - timedelta(days=1)
                dt = (_tmp_dt.replace(day=dt.day))
                finish = dt < dt_end

class cls_files:
    @staticmethod
    def read_file(filename):
        with open(filename, 'rb') as f:
            fn = f.read()
        return fn

    @staticmethod
    def write_file(data, filename):
        with open(filename, 'wb') as f:
            f.write(data)
        return f

# class cls_terbilang:
#     @staticmethod
def Terbilang(bil):
    angka=("","Satu","Dua","Tiga","Empat","Lima","Enam","Tujuh","Delapan","Sembilan","Sepuluh","Sebelas")
    Hasil = " "
    n = int(bil)
    if n >= 0 and n <= 11:
        Hasil = Hasil + angka[n]
    elif n < 20:
        Hasil = Terbilang(n % 10) + " belas"
    elif n < 100:
        Hasil = Terbilang(n / 10) + " Puluh" + Terbilang(n % 10)
    elif n < 200:
        Hasil = "Seratus" + Terbilang(n - 100)
    elif n < 1000:
        Hasil = Terbilang(n / 100) + " Ratus" + Terbilang(n %100)
    elif n < 2000:
        Hasil = "Seribu" + Terbilang(n-1000)
    elif n < 1000000:
        Hasil = Terbilang(n / 1000) + " Ribu" + Terbilang(n % 1000)
    elif n < 1000000000:
        Hasil = Terbilang(n/1000000) + " Juta" + Terbilang(n % 1000000)
    else:
        Hasil = Terbilang(n / 1000000000) + " Milyar" + Terbilang(n % 1000000000)
    return Hasil