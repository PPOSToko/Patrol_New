
$(document).ready(function () {
	pageSetUp();

	load_menu('/loadhome', { 'link': 'loadhome.html' }, '#content');

	$('aside nav ul li a').click(function () {
		var lnk = $(this).attr('link');
		var idmenu = $(this).attr('id');
		var desmenu = $(this).attr('name');
		document.getElementById('lnk').value = lnk;
		document.getElementById('idmenu').value = idmenu;
		document.getElementById('title').value = desmenu;

		load_menu('/gridmenu', { 'link': lnk, 'idmenu': idmenu, 'desmenu': desmenu }, '#content');
	});

	setInterval(function dt() {
		var months = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'];
		var myDays = ['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu'];
		var date = new Date();
		var day = date.getDate();
		var month = date.getMonth();
		var xmonth = date.getMonth();
		var thisDay = date.getDay(),
			thisDay = myDays[thisDay];
		var yy = date.getYear();
		var year = (yy < 1000) ? yy + 1900 : yy;
		var hours = date.getHours(),
			minutes = date.getMinutes(),
			seconds = date.getSeconds();

		day = day < 10 ? '0' + day : day;
		xmonth = xmonth < 10 ? '0' + month : month;

		hours = hours < 10 ? '0' + hours : hours;
		minutes = minutes < 10 ? '0' + minutes : minutes;
		seconds = seconds < 10 ? '0' + seconds : seconds;

		$('#hari').html(thisDay);
		$('#tgl').html(day + ' ' + months[month] + ' ' + year);
		$('#waktu').html(hours + ':' + minutes + ':' + seconds);
		$('#jam').html(hours);
		$('#date').html(year + '-' + xmonth + '-' + day);
	}, 500);

	// welcome_notif();
});

function userlogout() {
	// var level = $('#level').val();
	// if (level == '4') {
	// 	$.post("/cekkaskasirrj", function(response) {
	// 		if(response.status=='1'){

	// 			var dlg = bootbox.confirm({
	// 				title: "<i class='fa fa-question-circle text-primary'></i>&nbsp;Konfirmasi",
	// 				message: 'Silahkan Tutup Buku Kas Kasir Terlebih Sebelum Anda Keluar ?',
	// 				buttons: {
	// 					confirm: { label: 'Lanjutkan', className: 'btn-primary' },
	// 					cancel: { label: 'Tidak', className: 'btn-danger' }
	// 				},
	// 				callback: function (result) {
	// 					if (result) {
	// 						load_page('/loadpage', { 'link': 'popkaskasirrj.html' }, '#content');
	// 					}
	// 				}
	// 			});

	// 		}else{
	// 			location.href = "/logout";
	// 		}
	// 	})
	// 	.fail(function(jqxhr, settings, ex) {
	// 			msg_server_reloading();
	// 	});
	// } else {
		location.href = "/logout";
	// }
};

function user_info() {
	load_page('/loadpage', { 'link': '/_users/userinfo.html' }, '#content');
};

function loadhome() {
	load_menu('/loadhome', { 'link': 'loadhome.html' }, '#content');
};

function welcome_notif(){
	load_page('/loadpage', {'link':'welcome_notif.html'}, '#notif')
};