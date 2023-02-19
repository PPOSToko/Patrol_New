// User Level
function list_level(obj_target, value_selected){
   $(obj_target).empty();
   $(obj_target).append("<option value=''></option>");
   $.post("/getlistlevel", function (response) {
      for (var i = 0; i < response.data.length; i++) {
         if (response.data[i]['idlevel'] == value_selected) {
            $(obj_target).append("<option value='" + response.data[i]['idlevel'] + "' selected>" + response.data[i]['level'] + "</option>");
         } else {
            $(obj_target).append("<option value='" + response.data[i]['idlevel'] + "'>" + response.data[i]['level'] + "</option>");
         }
      }
   })
   .fail(function (jqxhr, settings, ex) {
      msg_server_reloading();
   });
};
// User Grouup

function list_group(obj_target, value_selected){
   $(obj_target).empty();
   $(obj_target).append("<option value=''></option>");
   $.post("/getlistgroup", function (response) {
      for (var i = 0; i < response.data.length; i++) {
         if (response.data[i]['idlevel'] == value_selected) {
            $(obj_target).append("<option value='" + response.data[i]['kdgroup'] + "' selected>" + response.data[i]['nm_group'] + "</option>");
         } else {
            $(obj_target).append("<option value='" + response.data[i]['kdgroup'] + "'>" + response.data[i]['nm_group'] + "</option>");
         }
      }
   })
   .fail(function (jqxhr, settings, ex) {
      msg_server_reloading();
   });
};

// Ponint Pertanyaan
function list_point(obj_target, value_selected,id_induk){
   $(obj_target).empty();
   $(obj_target).append("<option value=''></option>");
   $.post("/getlistpoint", function (response) {
      for (var i = 0; i < response.data.length; i++) {
         if(response.data[i]['id_induk'] == id_induk){
            if (response.data[i]['kode'] == value_selected) {
               $(obj_target).append("<option value='" + response.data[i]['kode'] + "' selected>" + response.data[i]['nama'] + "</option>");
            } else {
               $(obj_target).append("<option value='" + response.data[i]['kode'] + "'>" + response.data[i]['nama'] + "</option>");
            }
   
         }
      }
   })
   .fail(function (jqxhr, settings, ex) {
      msg_server_reloading();
   });
};

// Pasien
function cari_pop_pasien(param, divtemp, obj_focus){
   $.post("/openpoppasien", param, function(response){
      if (response.status == "1"){
         if (param.key == 'Pasien-From-Daftar-Poli') {
            $('#norm').val(response.norm);
            $('#jnsidentitas').attr('disabled', false).val(response.jnsidentitas);
            $('#nik').attr('disabled', false).val(response.noidentitas);
            $('#nama').attr('disabled', false).val(response.nama);
            $('#tmplhr').attr('disabled', false).val(response.tmplhr);
            $('#tgllhr').attr('disabled', false).val(response.tgllhr);
            $('#umur').val(uTahun(response.tgllhr));
            $('#usia').val(hitUsia(response.tgllhr));
            $('#jk').attr('disabled', false).val(response.jk);
            $('#goldrh').attr('disabled', false).val(response.goldrh);
            $('#kawin').attr('disabled', false).val(response.kawin);
            $('#agama').attr('disabled', false).val(response.agama);
            $('#kerja').attr('disabled', false).val(response.kerja);
            $('#almt').attr('disabled', false).val(response.almt);
            $('#kota').attr('disabled', false).val(response.kota);
            $('#tlp').attr('disabled', false).val(response.tlp);
            $('#rubahidentitas').attr('disabled', false);
         }
         $(obj_focus).attr('disabled', false).focus();        
      }else{
         waitingDialog.show("Memuat...", {dialogSize:'sm'});
         waitingDialog.hide();
         var myDiv = $(divtemp);
         myDiv.empty();
         myDiv.html(response);
      }
   })
   .fail(function (jqxhr, settings, ex) {
      msg_server_reloading();
   });
};

// Dokter
function cari_pop_dokter(param, divtemp, obj_focus){
   $.post("/openpopdokter", param, function(response){
      if (response.status == "1"){
         if(param.key == 'Dokter-From-User'){
            $('#id').val(response.kddok);
            $('#nama').val(response.nmdok);
         }else{
            $('#kddok').val(response.kddok);
            $('#nmdok').val(response.nmdok);
         }
            oEvent(obj_focus, false);
      }else{
         waitingDialog.show("Memuat...", {dialogSize:'sm'});
         waitingDialog.hide();
         var myDiv = $(divtemp);
         myDiv.empty();
         myDiv.html(response);
      }
   })
   .fail(function (jqxhr, settings, ex) {
      msg_server_reloading();
   });
};

// ICD

function cari_pop_icd(obj_id, obj_value, param, divtemp, obj_focus){
   $.post("/openpopicd", param)
   .done(function(response){
      if (response.status == "1"){
         $(obj_id).val(response.icd);
         $(obj_value).val(response.penyakit);
         $('#btnproses').attr('disabled', false);
         $(obj_focus).attr('disabled', false);
         // cek_kasus();
      }else{
         waitingDialog.show("Memuat...", {dialogSize:'sm'});
         waitingDialog.hide();
         var myDiv = $(divtemp);
         myDiv.html('');
         myDiv.html(response);
      }
   })
   .fail(function(jqxhr, settings, ex) {
      msg_server_reloading();
   });
};

//pelanggan
function cari_pop_pelanggan(param, divtemp, obj_focus){
   $.post("/openpoppelanggan", param, function(response){
      if (response.status == "1"){
         
         $('#kdsp').val(response.kdsp);
         $('#nmsp').val(response.nmsp);
         $('#apoteker').val(response.apoteker);
         $('#tglijin').val(response.tglijin);
         $('#plafon').val(response.flapon);
         $('#tempo').val(response.tempo);
         $('#kdklasifikasiplg').val(response.kdklasifikasi);
         $('#Klasifikasiplg').val(response.nmklasifikasi);
         $('#carabayar').val(response.carabayar);
         $('#nmsales').val(response.sales);
         $('#typepelanggan').val(response.typeclient);
         $('#nosik').val(response.sik);
         $('#nmwp').val(response.nmwp);
         $('#nonpwp').val(response.nonpwp);
         $('#kdsuplier').val(response.kdsuplier);
         $(obj_focus).attr('disabled', false);
         if (param.key == 'Data-From-Pelanggangd') {
            show_data_pesanangd();
            load_page('/detilpesanan', {'link':'/_pesanan/ftrspesanangd.html', 'com':'create','kdklasifikasi':response.kdklasifikasi,'kdsp':response.kdsp}, '#loadform');
   
         }else{
            show_data_pesangd();
            load_page('/detilpesanan', {'link':'/_pesanan/ftrspesanan.html', 'com':'create','kdklasifikasi':response.kdklasifikasi,'kdsp':response.kdsp}, '#loadform');
   
         }


//         load_page('/openform', {'link':'/_pesanan/ftrspesanan.html', 'com':'create','kdklasifikasi':response.kdklasifikasi}, '#loadform');
      }else{
         waitingDialog.show("Memuat...", {dialogSize:'sm'});
         waitingDialog.hide();
         var myDiv = $(divtemp);
         myDiv.html('');
         myDiv.html(response);
      }
   });
};
function cari_pop_spgd(param, divtemp, obj_focus){
   $.post("/openpopspgd", param, function(response){
     if (response.status == "1"){
         $('#nosp').val(response.nosp);
         $('#tanggal').val(response.tglsp);
         $(obj_focus).attr('disabled', false);
         show_data_penjualangd();
     } else if(response.status == "0"){
         msg_alert(response.msg, '#nosp');
     } else {
         waitingDialog.show("Memuat...", {dialogSize:'sm'});
         waitingDialog.hide();
         var myDiv = $(divtemp);
         myDiv.html('');
         myDiv.html(response);
     }
   });
};
function cari_pop_jualpelanggangd(param,divtemp,obj_focus){
   $.post("/openpopjualpelanggangd", param, function(response){
      if (response.status == "1"){
         $('#kdsp').val(response.kdsp);
         $('#nmsp').val(response.nmsp);
         $('#typepelanggan').val(response.typeclient);
         $('#alamat').val(response.alamat);
         $('#carabayar').val(response.carabayar);
         $('#nmsales').val(response.sales);
         $('#tempo').val(response.tempo);
         $('#margin').val(response.margin);
         $('#telp').val(response.telp);
         $('#nosp').focus();

      }else{
         waitingDialog.show("Memuat...", {dialogSize:'sm'});
         waitingDialog.hide();
         var myDiv = $(divtemp);
         myDiv.html('');
         myDiv.html(response);
      }

   });
}
function cari_pop_pelanggangd(param, divtemp, obj_focus){
   $.post("/openpoppelanggangd", param, function(response){
      if (response.status == "1"){

         if (param.key == 'Data-From-Pelanggangd') {
            // Convert string to date in javascript
            var tglskr = Date.now()
            var tahun =   response.tglijin.substring(6, 10);
            var tgl =   response.tglijin.substring(0, 2);
            var bln=   response.tglijin.substring(3, 5);
            var mydate = new Date(tahun + '-' + bln + '-' + tgl);
            // alert(mydate)
            if (response.tglijin == "" || response.tglijin == null || mydate <= tglskr){
               msg_alert_warning('Tanggal Ijin usaha belum diisi / Kedaluwarsa !', '#kdsp');
            }else{
               $('#kdsp').val(response.kdsp);
               $('#nmsp').val(response.nmsp);
               $('#apoteker').val(response.apoteker);
               $('#tglijin').val(response.tglijin);
               $('#plafon').val(response.flapon);
               $('#tempo').val(response.tempo);
               $('#kdklasifikasiplg').val(response.kdklasifikasi);
               $('#Klasifikasiplg').val(response.nmklasifikasi);
               $('#carabayar').val(response.carabayar);
               $('#nmsales').val(response.sales);
               $('#typepelanggan').val(response.typeclient);
               $('#nosik').val(response.sik);
               $('#nmwp').val(response.nmwp);
               $('#nonpwp').val(response.nonpwp);
               $('#kdsuplier').val(response.kdsuplier);
               $('#komisi').val(response.komisi);
               $('#ijinsarana').val(response.ijinsarana);
               $('#tglsarana').val(response.tglsarana);
               $('#regional').val(response.regional);
               $('#terpakai').val(response.terpakai);
               $(obj_focus).attr('disabled', false);
               show_data_pesanangd();
               load_page('/detilpesanan', {'link':'/_pesanan/ftrspesanangd.html', 'com':'create','kdklasifikasi':response.kdklasifikasi,'kdsp':response.kdsp}, '#loadform');
   
            }
         } else if(param.key =="Data-From-Pelanggangd-jual"){
            $('#kdsp').val(response.kdsp);
            $('#nmsp').val(response.nmsp);
            $('#typepelanggan').val(response.typeclient);
            $('#alamat').val(response.alamat);
            $('#carabayar').val(response.carabayar);
            $('#nmsales').val(response.sales);
            $('#tempo').val(response.tempo);
            $('#margin').val(response.margin);
            $('#nosp').focus();

         }else{
            
            load_page('/detilpesanan', {'link':'/_pesanan/ftrspesanan.html', 'com':'create','kdklasifikasi':response.kdklasifikasi,'kdsp':response.kdsp}, '#loadform');
   
         }


//         load_page('/openform', {'link':'/_pesanan/ftrspesanan.html', 'com':'create','kdklasifikasi':response.kdklasifikasi}, '#loadform');
      }else{
         waitingDialog.show("Memuat...", {dialogSize:'sm'});
         waitingDialog.hide();
         var myDiv = $(divtemp);
         myDiv.html('');
         myDiv.html(response);
      }
   });
};
function caripelanggangd(param, divtemp, obj_focus){
   $.post("/openpoppelanggangd", param, function(response){
      if (response.status == "1"){
         if (param.key == 'Data-From-Pelanggangd') {
            // Convert string to date in javascript
            var tglskr = Date.now();
            var tahun =   response.tglijin.substring(6, 10);
            var tgl =   response.tglijin.substring(0, 2);
            var bln=   response.tglijin.substring(3, 5);
            var mydate = new Date(tahun + '-' + bln + '-' + tgl);
            // alert(mydate)
            if (response.tglijin == "" || response.tglijin == null || mydate <= tglskr){
               msg_alert_warning('Tanggal Ijin usaha belum diisi / Kedaluwarsa !', '#kdsp');
            }else{
               $('#kdsp').val(response.kdsp);
               $('#nmsp').val(response.nmsp);
               $('#apoteker').val(response.apoteker);
               $('#tglijin').val(response.tglijin);
               $('#plafon').val(response.flapon);
               $('#tempo').val(response.tempo);
               $('#kdklasifikasiplg').val(response.kdklasifikasi);
               $('#Klasifikasiplg').val(response.nmklasifikasi);
               $('#carabayar').val(response.carabayar);
               $('#nmsales').val(response.sales);
               $('#typepelanggan').val(response.typeclient);
               $('#nosik').val(response.sik);
               $('#nmwp').val(response.nmwp);
               $('#nonpwp').val(response.nonpwp);
               $('#kdsuplier').val(response.kdsuplier);
               $('#komisi').val(response.komisi);
               $('#ijinsarana').val(response.ijinsarana);
               $('#tglsarana').val(response.tglsarana);
               $('#regional').val(response.regional);
               $('#terpakai').val(0);
               $(obj_focus).attr('disabled', false);
    
               show_data_pesanangd();
               load_page('/detilpesanan', {'link':'/_pesanan/ftrspesanangd.html', 'com':'create','kdklasifikasi':response.kdklasifikasi,'kdsp':response.kdsp}, '#loadform');
   
            }
         } else if(param.key =="Data-From-Pelanggangd-jual"){
            $('#kdsp').val(response.kdsp);
            $('#nmsp').val(response.nmsp);
            $('#typepelanggan').val(response.typeclient);
            $('#alamat').val(response.alamat);
            $('#carabayar').val(response.carabayar);
            $('#nmsales').val(response.sales);
            $('#tempo').val(response.tempo);
            $('#margin').val(response.margin);
            $('#nosp').focus();

         }else{
            
            load_page('/detilpesanan', {'link':'/_pesanan/ftrspesanan.html', 'com':'create','kdklasifikasi':response.kdklasifikasi,'kdsp':response.kdsp}, '#loadform');
   
         }


//         load_page('/openform', {'link':'/_pesanan/ftrspesanan.html', 'com':'create','kdklasifikasi':response.kdklasifikasi}, '#loadform');
      }
   });
};

// Satuan
function list_satuan(obj_target, value_selected, opt){
   $(obj_target).empty();
   if(opt == null || opt == ''){
      $(obj_target).append("<option value=''></option>");
   }else{
      $(obj_target).append("<option value='' disabled selected>"+opt+"</option>");
   }
   
   $.post("/getlistsatuan", function (response) {
      for (var i = 0; i < response.data.length; i++) {
         if (response.data[i]['kdsatuan'] == value_selected) {
            $(obj_target).append("<option value='" + response.data[i]['kdsatuan'] + "' selected>" + response.data[i]['nmsatuan'] + "</option>");
         } else {
            $(obj_target).append("<option value='" + response.data[i]['kdsatuan'] + "'>" + response.data[i]['nmsatuan'] + "</option>");
         }
      }
   })
   .fail(function (jqxhr, settings, ex) {
      msg_server_reloading();
   });
}
function cari_pop_regional(param, divtemp, obj_focus,obj_kode,obj_nama){
   $.post("/openpopregional", param, function(response){
      if (response.status == "1"){
            $(obj_kode).val(response.kode);
            $(obj_nama).val(response.nama);
            oEvent(obj_focus, false);
     }else{
         waitingDialog.show("Memuat...", {dialogSize:'sm'});
         waitingDialog.hide();
         var myDiv = $(divtemp);
         myDiv.empty();
         myDiv.html(response);
      }
   })
   .fail(function(jqxhr, settings, ex) {
      msg_server_reloading();
   });
};


function cari_pop_satuan(param, divtemp, obj_focus,obj_kode,obj_nama){
   $.post("/openpopsatuan", param, function(response){
      if (response.status == "1"){
            $(obj_kode).val(response.kode);
            $(obj_nama).val(response.nama);
            oEvent(obj_focus, false);
     }else{
         waitingDialog.show("Memuat...", {dialogSize:'sm'});
         waitingDialog.hide();
         var myDiv = $(divtemp);
         myDiv.empty();
         myDiv.html(response);
      }
   })
   .fail(function(jqxhr, settings, ex) {
      msg_server_reloading();
   });
};

function cari_pop_satuanisi(param, divtemp, obj_focus,obj_kode,obj_nama){
   $.post("/openpopsatuanisi", param, function(response){
      if (response.status == "1"){
            $(obj_kode).val(response.kode);
            $(obj_nama).val(response.nama);
            oEvent(obj_focus, false);
     }else{
         waitingDialog.show("Memuat...", {dialogSize:'sm'});
         waitingDialog.hide();
         var myDiv = $(divtemp);
         myDiv.empty();
         myDiv.html(response);
      }
   })
   .fail(function(jqxhr, settings, ex) {
      msg_server_reloading();
   });
};

function cari_pop_golterapi(param, divtemp, obj_focus,obj_kode,obj_nama,kdgenerik,nmgenerik){
   $.post("/openpopgolterapi", param, function(response){
      if (response.status == "1"){
            $(obj_kode).val(response.kdgol);
            $(obj_nama).val(response.nmgol);
            $('#kdklasterapi').val(response.kdterapi);
            $('#nmklasterapi').val(response.nmterapi);
            simpan_dataprodukbaru();
            // oEvent(obj_focus, false);
     }else{
         waitingDialog.show("Memuat...", {dialogSize:'sm'});
         waitingDialog.hide();
         var myDiv = $(divtemp);
         myDiv.empty();
         myDiv.html(response);
      }
   })
   .fail(function(jqxhr, settings, ex) {
      msg_server_reloading();
   });
};

// Generik
function cari_pop_generik(param, divtemp, obj_focus,obj_kode,obj_nama){
   $.post("/openpopgenerik", param, function(response){
      if (response.status == "1"){
            $(obj_kode).val(response.kode);
            $(obj_nama).val(response.nama);
            oEvent(obj_focus, false);
     }else{
         waitingDialog.show("Memuat...", {dialogSize:'sm'});
         waitingDialog.hide();
         var myDiv = $(divtemp);
         myDiv.empty();
         myDiv.html(response);
      }
   })
   .fail(function(jqxhr, settings, ex) {
      msg_server_reloading();
   });
};

// Gudang
function cari_pop_gudang(param, divtemp, obj_focus){
   $.post("/openpopgudang", param, function(response){
      if (response.status == "1"){
            $('#kdsp').val(response.kdsp);
            $('#nmsp').val(response.nmsp);
            $('#alamat').val(response.alamat);
            oEvent(obj_focus, false);
     }else{
         waitingDialog.show("Memuat...", {dialogSize:'sm'});
         waitingDialog.hide();
         var myDiv = $(divtemp);
         myDiv.empty();
         myDiv.html(response);
      }
   })
   .fail(function(jqxhr, settings, ex) {
      msg_server_reloading();
   });
};
function cari_pop_pemasokkonfgd(param,divtemp,obj_focus){
   $.post("/openpoppemasokkonfgd",param,function(response){
      if (response.status == "1"){
         $('#kdpemasok').val(response.kdsp);
         $('#nmpemasok').val(response.nmsp);
         $('#disc').val(response.discon);
         $('#discrp').val(response.discrp);
         $('#pricelist').val(response.pricelist);
         $('#minorder').val(response.minorder);
         $('#hrgjadi').val(response.hrgjadi);
         $('#satuanbeli').val(response.satuanbeli)
         $('#stok').val(response.stok);
         oEvent(obj_focus, false);
      }else{
         waitingDialog.show("Memuat...", {dialogSize:'sm'});
         waitingDialog.hide();
         var myDiv = $(divtemp);
         myDiv.empty();
         myDiv.html(response);

      }
   });
}

function cari_pop_gudanggd(param, divtemp, obj_focus){
   $.post("/openpopgudanggd", param, function(response){
      if (response.status == "1"){
         if (param.key == "Data-From-updatehargapemasok"){
            $('#kdsp').val(response.kdsp);
            $('#nmsp').val(response.nmsp);
            $('#alamat').val(response.alamat);
            $('#kdregional').val(response.kd_wilayah);
            $('#penanggungjwb').val(response.kontak);
            oEvent(obj_focus, false);
         }else if(param.key == "Data-From-stokadj"){
            $('#kdsp').val(response.kdsp);
            $('#nmsp').val(response.nmsp);
            show_data_stokadjgd();
         }else{
            $('#kdsp').val(response.kdsp);
            $('#nmsp').val(response.nmsp);
            $('#alamat').val(response.alamat);
            $('#penanggungjwb').val(response.kontak);
            oEvent(obj_focus, false);

         }
     }else{
         waitingDialog.show("Memuat...", {dialogSize:'sm'});
         waitingDialog.hide();
         var myDiv = $(divtemp);
         myDiv.empty();
         myDiv.html(response);
      }
   })
   .fail(function(jqxhr, settings, ex) {
      msg_server_reloading();
   });
};
function cari_pop_gudangingd(param, divtemp, obj_focus){
   $.post("/openpopgudangingd", param, function(response){
      if (response.status == "1"){
            $('#kdpemasok').val(response.kdsp);
            $('#nmpemasok').val(response.nmsp);
            oEvent(obj_focus, false);
     }else{
         waitingDialog.show("Memuat...", {dialogSize:'sm'});
         waitingDialog.hide();
         var myDiv = $(divtemp);
         myDiv.empty();
         myDiv.html(response);
      }
   })
   .fail(function(jqxhr, settings, ex) {
      msg_server_reloading();
   });
};
// Rekening
function cari_pop_rekening(param,divtemp, obj_focus){
   $.post("/openpoprekening", param, function(response){
      if (response.status == "0"){
            $('#norekening').val(response.no_rekeing);
            $('#nmbank').val(response.nm_bank);
            $('#kdbank').val(response.kode);
            oEvent(obj_focus, false);

         // oEvent(obj_focus, false);
      }else{
         waitingDialog.show("Memuat...", {dialogSize:'sm'});
         waitingDialog.hide();
         var myDiv = $(divtemp);
         myDiv.empty();
         myDiv.html(response);
      }
   })
   .fail(function(jqxhr, settings, ex) {
      msg_server_reloading();
   });

   };

// Prinsipal
function cari_pop_prinsipal(param,divtemp, obj_focus){
   $.post("/openpopprinsipal", param, function(response){

      if (response.status == "0"){
        if (param.key == "Data-From-updatehrgprinsipal"){
            $('#kdprinsipal').val(response.kode);
            $('#nmprinsipal').val(response.nama);
            load_page('/loadpaged', {'link':'/_hargaprinsip/listhargaprinsipal.html','nosp':response.kode}, '#showhargaprinsipal');
            show_data_hargaprinsipal()

        }else{
            $('#kdprinsipal').val(response.kode);
            $('#nmprinsipal').val(response.nama);
            oEvent(obj_focus, false);

        }
         // oEvent(obj_focus, false);
      }else{
         waitingDialog.show("Memuat...", {dialogSize:'sm'});
         waitingDialog.hide();
         var myDiv = $(divtemp);
         myDiv.empty();
         myDiv.html(response);
      }
   })
   .fail(function(jqxhr, settings, ex) {
      msg_server_reloading();
   });

   };
// Produk
function cari_pop_obat(param, divtemp, obj_focus){
   $.post("/openpopobat", param, function(response){
      if (response.status == "1"){
         if(param.key == 'Obat-From-Atur-Penjualan'){
            // if(response.stok <= 0){
            //    msg_alert_warning('Persediaan Kosong !', '#nmobat');
            // }else{
               $('#kdobat').val(response.kdobat);
               $('#nmobat').val(response.nmobat);
               $('#prinsipal').val(response.pabrik);
               oEvent(obj_focus, false);
            // }
         }else if(param.key == 'Obat-From-Penjualan'){
            if(response.stok <= 0){
               msg_alert_warning('Persediaan Kosong !', '#nmobat');
            }else{
               $('#kdobat').val(response.kdobat);
               $('#nmobat').val(response.nmobat);
               $('#satuan').val(response.satuan);
               $('#harga').val(response.harga);
               $('#stok').val(response.stok);
               oEvent(obj_focus, false);
            }
         }else if(param.key == 'Obat-From-Stok'){
            $('#kdobat').val(response.kdobat);
            $('#nmobat').val(response.nmobat);
            $('#satuan').val(response.satuan);
            $('#harga').val(response.harga);
            $('#stok').val(response.stok);
            oEvent(obj_focus, false);
         }else if(param.key == 'Obat-From-Booking'){
            $('#kdobat').val(response.kdobat);
            $('#nmobat').val(response.nmobat);
            $('#satuan').val(response.satuan);
            $('#pricelist').val(response.harga);
            $('#prinsipal').val(response.pabrik);
            $('#golongan').val(response.golongan);
            $('#stok').val(response.stok);
            $('#minorder').val(response.minorder);
            $('#hrgjadi').val(response.hrgjadi);
            $('#discon').val(0);
            $('#disconrp').val(0);
            $('#discoff').val(0);
            $('#discoffrp').val(0);
            oEvent(obj_focus, false);

         }else{
            
            // if(response.stok <= 0){
            //    msg_alert_warning('Persediaan Kosong !', '#nmobat');
            // }else{
               $('#kdobat').val(response.kdobat);
               $('#nmobat').val(response.nmobat);
               $('#satuan').val(response.satuan);
               $('#harga').val(response.harga);
               show_data_persamaan()
               // oEvent(obj_focus, false);
            // }
         }
      }else{
         waitingDialog.show("Memuat...", {dialogSize:'sm'});
         waitingDialog.hide();
         var myDiv = $(divtemp);
         myDiv.empty();
         myDiv.html(response);
      }
   })
   .fail(function(jqxhr, settings, ex) {
      msg_server_reloading();
   });
};
function cari_pop_obatpengganti(param,divtemp,obj_focus){
   $.post("/openpopobatpengganti", param, function(response){
      if (response.status == "1"){
         $('#kdobat2').val(response.kdobat);
         oEvent(obj_focus, false);
      }else{
         waitingDialog.show("Memuat...", {dialogSize:'sm'});
         waitingDialog.hide();
         var myDiv = $(divtemp);
         myDiv.empty();
         myDiv.html(response);
       
      }
   });
}
function cari_pop_obatgd(param, divtemp, obj_focus){
   $.post("/openpopobatgd", param, function(response){
      if (response.status == "1"){
         if(param.key == 'Obat-From-Atur-Penjualan'){
            // if(response.stok <= 0){
            //    msg_alert_warning('Persediaan Kosong !', '#nmobat');
            // }else{
               $('#kdobat').val(response.kdobat);
               $('#nmobat').val(response.nmobat);
               $('#prinsipal').val(response.pabrik);
               $('#satuan').val(response.satuan);
               $('#harga').val(response.harga);
               oEvent(obj_focus, false);
            // }
         }else if(param.key == 'Obat-From-Opname'){
            $('#kdobat').val(response.kdobat);
            $('#nmobat').val(response.nmobat);
            $('#prinsipal').val(response.pabrik);
            $('#satuan').val(response.satuan);
            $('#harga').val(response.harga);

            oEvent(obj_focus, false);
         }else if(param.key == 'Obat-From-Quarantine'){
            $('#kdobat').val(response.kdobat);
            $('#nmobat').val(response.nmobat);
            $('#satuan').val(response.satuan);
            $('#stok').val(response.stok);
            oEvent(obj_focus, false);

         }else if(param.key == 'Obat-From-Penjualan'){
            if(response.stok <= 0){
               msg_alert_warning('Persediaan Kosong !', '#nmobat');
            }else{
               $('#kdobat').val(response.kdobat);
               $('#nmobat').val(response.nmobat);
               $('#satuan').val(response.satuan);
               $('#harga').val(response.harga);
               $('#stok').val(response.stok);
               oEvent(obj_focus, false);
            }
         }else if(param.key == 'Obat-From-Stok'){
            $('#kdobat').val(response.kdobat);
            $('#nmobat').val(response.nmobat);
            $('#satuan').val(response.satuan);
            $('#harga').val(response.harga);
            $('#stok').val(response.stok);
            oEvent(obj_focus, false);
         }else if(param.key == 'Obat-From-Bookinggd'){
            $('#kdobat').val(response.kdobat);
            $('#nmobat').val(response.nmobat);
            $('#satuan').val(response.satuan);
            $('#pricelist').val(response.harga);
            $('#prinsipal').val(response.pabrik);
            $('#golongan').val(response.golongan);
            $('#stok').val(response.stok);
            $('#minorder').val(response.minorder);
            $('#hrgjadi').val(response.hrgjadi);
            $('#bolehbeli').val(response.bolehbeli);
            $('#discon').val(response.discon);
            $('#disconrp').val(response.disconrp);
            $('#discoff').val(response.discoff);
            $('#discoffrp').val(response.discoffrp);
            oEvent(obj_focus, false);
         }else if(param.key == 'Obat-From-Bookinggd-int'){            
            $('#kdobat').val(response.kdobat);
            $('#nmobat').val(response.nmobat);
            $('#satuan').val(response.satuan);
            $('#pricelist').val(response.harga);
            $('#prinsipal').val(response.pabrik);
            $('#golongan').val(response.golongan);
            $('#stok').val(response.stok);
            $('#minorder').val(response.minorder);
            $('#hrgjadi').val(response.hrgjadi);
            $('#bolehbeli').val(response.bolehbeli);
            oEvent(obj_focus, false);
         }else if (param.key=="Obat-From-adj"){
            $('#kdobat').val(response.kdobat);
            $('#nmobat').val(response.nmobat);
            $('#satuan').val(response.satuan);
            $('#pricelist').val(response.harga);
            $('#prinsipal').val(response.pabrik);
            $('#golongan').val(response.golongan);
            $('#stok').val(response.stok);
            oEvent(obj_focus, false);

         }else if(param.key == "Obat-From-updateprinsip"){
            $('#kdobat').val(response.kdobat);
            $('#nmobat').val(response.nmobat);
            $('#satuanbeli').val(response.satuanbeli);
            $('#kdsatuanbeli').val(response.kdsatuanbeli);
            $('#satuanjual').val(response.satuanjual);
            $('#kdsatuanjual').val(response.kdsatuanjual);
            $('#isi').val(response.isi);
            oEvent(obj_focus, false);
         }else if(param.key == "Obat-From-updatepemasok"){
            $('#kdobat').val(response.kdobat);
            $('#nmobat').val(response.nmobat);
            $('#satuanbeli').val(response.satuanbeli);
            $('#kdsatuanbeli').val(response.kdsatuanbeli);
            $('#satuanjual').val(response.satuanjual);
            $('#kdsatuanjual').val(response.kdsatuanjual);
            $('#pricelist').val(response.pricelist);
            $('#discon').val(response.discon);
            $('#disconrp').val(response.disconrp);
            $('#discoff').val(response.discoff);
            $('#discoffrp').val(response.discoffrp);
            $('#minorder').val(response.minorder);
            $('#isi').val(response.isi);
            $('#hrgjadi').val(response.hrgjadi);
            $('#selisih').val(response.selisih);
            oEvent(obj_focus, false);
         }else if(param.key == "Obat-From-Aturanbelanjagd"){
            $('#kdobat').val(response.kdobat);
            $('#nmobat').val(response.nmobat);
            $('#satuan').val(response.satuan);
            $('#harga').val(response.harga);
            //$('#tblpersamaan').DataTable().ajax.reload();
            // $('.tblpersamaan').remove();
            // show_data_persamaangd()
         }else if (param.key == "Obat-From-ttbgd"){ 
            $('#kdobat').val(response.kdobat);
            $('#nmobat').val(response.nmobat);
            $('#satuanbeli').val(response.nmsatuanbeli);
            $('#kdsatuanbeli').val(response.kdsatuanbeli);
            $('#kdsatuanjual').val(response.kdsatuanjual);
            $('#kdsatuanjual').val(response.nmsatuanjual);

            cekobat();
          
         }else{
            
            // if(response.stok <= 0){
            //    msg_alert_warning('Persediaan Kosong !', '#nmobat');
            // }else{
               $('#kdobat').val(response.kdobat);
               $('#nmobat').val(response.nmobat);
               $('#satuan').val(response.satuan);
               $('#harga').val(response.harga);
               show_data_persamaangd()
               // oEvent(obj_focus, false);
            // }
         }
      }else if(response.status == "2"){
         msg_alert_warning(response.msg, '#nmobat');
      }else if(response.status == "0"){
         $('#kdpersamaan').val(response.kdpersamaan);
         msg_alert_warning(response.msg, '#nmobat');
      // Tampilkan Persamaan Obat

      }else{
         waitingDialog.show("Memuat...", {dialogSize:'sm'});
         waitingDialog.hide();
         var myDiv = $(divtemp);
         myDiv.empty();
         myDiv.html(response);
      }
   })
   .fail(function(jqxhr, settings, ex) {
      msg_server_reloading();
   });
};
function cariobatgd(param, divtemp, obj_focus){
   $.post("/openpopobatgd", param, function(response){
      if (response.status == "1"){
         if(param.key == 'Obat-From-Atur-Penjualan'){
            // if(response.stok <= 0){
            //    msg_alert_warning('Persediaan Kosong !', '#nmobat');
            // }else{
               $('#kdobat').val(response.kdobat);
               $('#nmobat').val(response.nmobat);
               $('#prinsipal').val(response.pabrik);
               oEvent(obj_focus, false);
            // }
         }else if(param.key == 'Obat-From-Penjualan'){
            if(response.stok <= 0){
               msg_alert_warning('Persediaan Kosong !', '#nmobat');
            }else{
               $('#kdobat').val(response.kdobat);
               $('#nmobat').val(response.nmobat);
               $('#satuan').val(response.satuan);
               $('#harga').val(response.harga);
               $('#stok').val(response.stok);
               oEvent(obj_focus, false);
            }
         }else if(param.key == 'Obat-From-Stok'){
            $('#kdobat').val(response.kdobat);
            $('#nmobat').val(response.nmobat);
            $('#satuan').val(response.satuan);
            $('#harga').val(response.harga);
            $('#stok').val(response.stok);
            oEvent(obj_focus, false);
         }else if(param.key == 'Obat-From-Bookinggd'){
            $('#kdobat').val(response.kdobat);
            $('#nmobat').val(response.nmobat);
            $('#satuan').val(response.satuan);
            $('#pricelist').val(response.harga);
            $('#prinsipal').val(response.pabrik);
            $('#golongan').val(response.golongan);
            $('#stok').val(response.stok);
            $('#minorder').val(response.minorder);
            $('#hrgjadi').val(response.hrgjadi);
            $('#bolehbeli').val(response.bolehbeli);
            $('#discon').val(response.discon);
            $('#disconrp').val(response.disconrp);
            $('#discoff').val(response.discoff);
            $('#discoffrp').val(response.discoffrp);
            oEvent(obj_focus, false);
         }else if(param.key == 'Obat-From-Bookinggd-int'){            
            $('#kdobat').val(response.kdobat);
            $('#nmobat').val(response.nmobat);
            $('#satuan').val(response.satuan);
            $('#pricelist').val(response.harga);
            $('#prinsipal').val(response.pabrik);
            $('#golongan').val(response.golongan);
            $('#stok').val(response.stok);
            $('#minorder').val(response.minorder);
            $('#hrgjadi').val(response.hrgjadi);
            $('#bolehbeli').val(response.bolehbeli);
            oEvent(obj_focus, false);

         }else if(param.key == "Obat-From-updateprinsip"){
            $('#kdobat').val(response.kdobat);
            $('#nmobat').val(response.nmobat);
            $('#satuanbeli').val(response.satuanbeli);
            $('#kdsatuanbeli').val(response.kdsatuanbeli);
            $('#satuanjual').val(response.satuanjual);
            $('#kdsatuanjual').val(response.kdsatuanjual);
            $('#isi').val(response.isi);
            oEvent(obj_focus, false);
         }else if(param.key == "Obat-From-updatepemasok"){
            $('#kdobat').val(response.kdobat);
            $('#nmobat').val(response.nmobat);
            $('#satuanbeli').val(response.satuanbeli);
            $('#kdsatuanbeli').val(response.kdsatuanbeli);
            $('#satuanjual').val(response.satuanjual);
            $('#kdsatuanjual').val(response.kdsatuanjual);
            $('#pricelist').val(response.pricelist);
            $('#discon').val(response.discon);
            $('#disconrp').val(response.disconrp);
            $('#discoff').val(response.discoff);
            $('#discoffrp').val(response.discoffrp);
            $('#minorder').val(response.minorder);
            $('#isi').val(response.isi);
            $('#hrgjadi').val(response.hrgjadi);
            $('#selisih').val(response.selisih);
            oEvent(obj_focus, false);
         }else if(param.key == "Obat-From-Aturanbelanjagd"){
            $('#kdobat').val(response.kdobat);
            $('#nmobat').val(response.nmobat);
            $('#satuan').val(response.satuan);
            $('#harga').val(response.harga);
            show_data_persamaangd()
      
         }else if (param.key == "Obat-From-ttbgd"){ 
            $('#kdobat').val(response.kdobat);
            $('#nmobat').val(response.nmobat);
            oEvent(obj_focus, false);
         }else{
            
            // if(response.stok <= 0){
            //    msg_alert_warning('Persediaan Kosong !', '#nmobat');
            // }else{
               $('#kdobat').val(response.kdobat);
               $('#nmobat').val(response.nmobat);
               $('#satuan').val(response.satuan);
               $('#harga').val(response.harga);
               show_data_persamaangd()
               // oEvent(obj_focus, false);
            // }
         }
      }else if(response.status == "2"){
         msg_alert_warning(response.msg, '#nmobat');
      }else if(response.status == "0"){
         $('#kdpersamaan').val(response.kdpersamaan);
         msg_alert_warning(response.msg, '#nmobat');
      // Tampilkan Persamaan Obat

      }
   })
   .fail(function(jqxhr, settings, ex) {
      msg_server_reloading();
   });
};

function cari_pop_persamaanobatgd(param, divtemp, obj_focus){
   $.post("/openpoppersamaangd", param, function(response){
      if (response.status == "1"){
            $('#kdobat3').val(response.kdobat);
            $('#nmobat3').val(response.nmobat);
            oEvent(obj_focus, false);
         
      }else{
         waitingDialog.show("Memuat...", {dialogSize:'sm'});
         waitingDialog.hide();
         var myDiv = $(divtemp);
         myDiv.empty();
         myDiv.html(response);
      }
   })
   .fail(function(jqxhr, settings, ex) {
      msg_server_reloading();
   });
};
function cari_pop_obatbaru(param,divtemp, obj_focus){
   $.post("/openpopobatbaru", param, function(response){
      if (response.status == "1"){
         $('#kdobat').val(response.kdobat);
         $('#nmobat').val(response.nmobat);
         $('#kdprinsipal').val(response.kdprinsipal);
         $('#nmprinsipal').val(response.nmprinsipal);
         $('#kdsatuanbeli').val(response.kdsatuanbeli);
         $('#kdsatuanjual').val(response.kdsatuanjual);
         $('#nmsatuanbeli').val(response.nmsatuanbeli);
         $('#nmsatuanjual').val(response.nmsatuanjual);
         $('#konversi').val(response.isi);
         $('#nmgenerik').val(response.generik);
         $('#kdklasterapi').val(response.kdterapi);
         $('#nmgolterapi').val(response.nmgolterapi);
         $('#kdgolterapi').val(response.kdgolterapi);
         $('#hnabeli').val(numberWithCommas(response.hna));
         $('#hdabeli').val(numberWithCommas(response.hda));
         $('#hnajual').val(numberWithCommas((response.hna/response.isi)));
         $('#hdajual').val(numberWithCommas(response.hda/response.isi));
         $('#nmgolterapi').val(response.nmgolterapi);
         $('#nmklasterapi').val(response.nmterapi);
         $('#nmgolongan').val(response.jenis);
         show_data_komposisibaru();
         oEvent(obj_focus, false);
         
      }else{
         waitingDialog.show("Memuat...", {dialogSize:'sm'});
         waitingDialog.hide();
         var myDiv = $(divtemp);
         myDiv.empty();
         myDiv.html(response);
      }
   
   })
   // .fail(function(jqxhr, settings, ex) {
   //    msg_server_reloading();
   // });

};
// LAB
function list_jenis_lab(obj){
   $(obj).empty();
   $(obj).append("<option value=''>-- Pilih --</option>");
   $.post("/getlistjnslab", function(response) {
      for(var i=0; i<response.data.length; i++){
            $(obj).append("<option value='"+response.data[i]['kdjns']+"'>"+ response.data[i]['nmjns'] +"</option>");
      }
   })
   .fail(function(jqxhr, settings, ex) {
      msg_server_reloading();
   });
};

function cari_pop_jenis_lab(obj_id, obj_value, param, divtemp, obj_focus){
   $.post("/openpopjenislab", param, function(response){
      if (response.status == "1"){
         if(param.key=='Jenis-Lab-From-Nilai-Normal'){
            $(obj_id).val(response.kdjenis);
            $(obj_value).val(response.nmjenis);
            oEvent(obj_focus, false);
         }else{
            $(obj_id).val(response.kdjenis);
            $(obj_value).val(response.nmjenis);
            oEvent(obj_focus, false);
         }
      }else{
         waitingDialog.show("Memuat...", {dialogSize:'sm'});
         waitingDialog.hide();
         var myDiv = $(divtemp);
         myDiv.empty();
         myDiv.html(response);
      }
   })
   .fail(function(jqxhr, settings, ex) {
      msg_server_reloading();
   });
};

function cari_pop_tindakan_lab(obj_id, obj_value, param, divtemp, obj_focus) {
   $.post("/openpoptindakanlab", param, function (response) {
      if (response.status == "1") {
         $(obj_id).val(response.kdjenis);
         $(obj_value).val(response.nmjenis);
         oEvent(obj_focus, false);
      } else {
         waitingDialog.show("Memuat...", { dialogSize: 'sm' });
         waitingDialog.hide();
         var myDiv = $(divtemp);
         myDiv.html('');
         myDiv.html(response);
      }
   })
      .fail(function (jqxhr, settings, ex) {
         msg_server_reloading();
      });
};

function cari_pop_tarif_lab(obj_id, obj_value, param, divtemp, obj_focus){
   $.post("/openpoptariflab", param, function(response){
      if (response.status == "1"){
         if(param.key=='Tarif-Lab-From-Trs-Lab'){
            $(obj_id).val(response.kdjenis);
            $(obj_value).val(response.nmjenis);
            oEvent(obj_focus, false);
         }
      }else{
         waitingDialog.show("Memuat...", {dialogSize:'sm'});
         waitingDialog.hide();
         var myDiv = $(divtemp);
         myDiv.html('');
         myDiv.html(response);
      }
   })
   .fail(function(jqxhr, settings, ex) {
      msg_server_reloading();
   });
};

// RAD
function cari_pop_jenis_rad(obj_id, obj_value, param, divtemp, obj_focus) {
   $.post("/openpopjenisrad", param, function (response) {
      if (response.status == "1") {
         $(obj_id).val(response.kdjenis);
         $(obj_value).val(response.nmjenis);
         oEvent(obj_focus, false);
      } else {
         waitingDialog.show("Memuat...", { dialogSize: 'sm' });
         waitingDialog.hide();
         var myDiv = $(divtemp);
         myDiv.html('');
         myDiv.html(response);
      }
   })
   .fail(function (jqxhr, settings, ex) {
      msg_server_reloading();
   });
};

function cari_pop_tindakan_rad(obj_id, obj_value, param, divtemp, obj_focus){
   $.post("/openpoptindakanrad", param, function (response) {
      if (response.status == "1") {
         $(obj_id).val(response.kdjenis);
         $(obj_value).val(response.nmjenis);
         oEvent(obj_focus, false);
      } else {
         waitingDialog.show("Memuat...", { dialogSize: 'sm' });
         waitingDialog.hide();
         var myDiv = $(divtemp);
         myDiv.html('');
         myDiv.html(response);
      }
   })
   .fail(function (jqxhr, settings, ex) {
      msg_server_reloading();
   });
};

// FISIO
function cari_pop_tindakan_fisio(obj_id, obj_value, param, divtemp, obj_focus){
   $.post("/openpoptindakanfisio", param, function (response) {
      if (response.status == "1") {
         $(obj_id).val(response.kdjenis);
         $(obj_value).val(response.nmjenis);
         oEvent(obj_focus, false);
      } else {
         waitingDialog.show("Memuat...", { dialogSize: 'sm' });
         waitingDialog.hide();
         var myDiv = $(divtemp);
         myDiv.html('');
         myDiv.html(response);
      }
   })
   .fail(function (jqxhr, settings, ex) {
      msg_server_reloading();
   });
};

// Pemasok
function cari_pop_pemasokobattukarfps(param, divtemp, obj_focus){
   $.post("/openpoppemasokobattukarfps", param, function(response){
      if (response.status == "0"){
         if(param.key=='Pemasok-koneksi'){
            $('#kdpemasok').val(response.kdsp);
            $('#nmpemasok').val(response.nmsp);
            $('#almt').val(response.almt);
            $('#almt2').val(response.alamat2);
            $('#kontak').val(response.kontak);
            $('#telp').val(response.telp);
            $('#email').val(response.email);
            $('#tempo').val(response.tempo);
            $('#norek').val(response.rekening);
            $('#bank').val(response.bank);
            $(obj_focus).attr('disabled', false).focus();

         }else{
            $('#kdpemasok').val(response.kdsp);
            $('#nmpemasok').val(response.nmsp);
            show_data_tukarfps();
            $(obj_focus).attr('disabled', false).focus();
   
         }
      }else{
         waitingDialog.show("Memuat...", {dialogSize:'sm'});
         waitingDialog.hide();
         var myDiv = $(divtemp);
         myDiv.html('');
         myDiv.html(response);
         $(obj_focus).attr('disabled', false).focus();
      }
   });
};
function cari_pop_pemasokgd(param, divtemp, obj_focus){
   $.post("/openpoppemasokgd", param, function(response){
      if (response.status == "1"){
         $('#kdsp').val(response.kdsp);
         $('#nmsp').val(response.nmsp);
         
         if(param.key=='Pemasok-Obat'){
            show_data_hargapemasok()
            load_page('/inputhrgpemasok', {'link':'/_hargapemasok/finputhrgpemasok.html', 'com':'create','kdprinsipal':data[0],'nmprinsipal':data[1]}, '#loadform');  
            $(obj_focus).attr('disabled', false).focus();
   
         }
         else{
            $(obj_focus).attr('disabled', false).focus();

         }
      }else{
         waitingDialog.show("Memuat...", {dialogSize:'sm'});
         waitingDialog.hide();
         var myDiv = $(divtemp);
         myDiv.html('');
         myDiv.html(response);
      }
   });
};
function cari_pop_kontakpemasokgd(param, divtemp, obj_focus){
   $.post("/openpopkontakpemasokgd", param, function(response){
      if (response.status == "0"){
         $('#kdpemasok').val(response.kdsp);
         $('#nmpemasok').val(response.nmsp);
         $(obj_focus).attr('disabled', false).focus();
      }else{
         waitingDialog.show("Memuat...", {dialogSize:'sm'});
         waitingDialog.hide();
         var myDiv = $(divtemp);
         myDiv.html('');
         myDiv.html(response);
      }
   });
};

function cari_pop_pemasokintgd(param, divtemp, obj_focus){
   $.post("/openpoppemasokobat", param, function(response){
      if (response.status == "0"){
         $('#kdsp').val(response.kdsp);
         $('#nmsp').val(response.nmsp);
         $(obj_focus).attr('disabled', false).focus();
      }else{
         waitingDialog.show("Memuat...", {dialogSize:'sm'});
         waitingDialog.hide();
         var myDiv = $(divtemp);
         myDiv.html('');
         myDiv.html(response);
         $(obj_focus).attr('disabled', false).focus();
      }
   });
};

function cari_pop_pemasokspgd(param, divtemp, obj_focus){
   $.post("/openpoppemasokspgd", param, function(response){
      if (response.status == "0"){
         if(param.key == 'Pemasok-Obat-Koneksi'){
            $('#kdpemasok').val(response.kdsp);
            $('#nmpemasok').val(response.nmsp);

         }else{
            $('#kdsp').val(response.kdsp);
            $('#nmsp').val(response.nmsp);
            $('#minimal').val(response.minorder);
            $('#pesan').val(response.totalsp);
            $('#kurang').val(response.kurang);
            show_data_pesanangd();
            $(obj_focus).attr('disabled', false).focus();
   
         }
      }else{
         waitingDialog.show("Memuat...", {dialogSize:'sm'});
         waitingDialog.hide();
         var myDiv = $(divtemp);
         myDiv.html('');
         myDiv.html(response);
      }
   });
   
   
};
