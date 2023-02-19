var sessionName = "{{session['nama]}}";

//Modal Loading Prosess
var waitingDialog = waitingDialog || (function ($) {
	'use strict';

	var $dialog = $(
		'<div class="modal fade" data-backdrop="static" data-keyboard="false" tabindex="-1" role="dialog" aria-hidden="true">' +
		'<div class="modal-dialog modal-sm">' +
		'<div class="modal-content">' +
		'<div class="modal-header">' +
		'<label></label>' +
		'</div>' +
		'<div class="modal-body">' +
		'<div class="progress progress-striped active" style="margin-bottom:0;">' +
		'<div class="progress-bar" style="width: 100%"></div>' +
		'</div>' +
		'</div>' +
		'</div>' +
		'</div>' +
		'</div>');

	return {
		show: function (message, options) {
			// Assigning defaults
			if (typeof options === 'undefined') {
				options = {};
			}
			if (typeof message === 'undefined') {
				message = '';
			}
			var settings = $.extend({
				dialogSize: 'small',
				progressType: '',
				onHide: null // This callback runs after the dialog was hidden
			}, options);

			// Configuring dialog
			$dialog.find('.modal-dialog').attr('class', 'modal-dialog').addClass('modal-' + settings.dialogSize);
			$dialog.find('.progress-bar').attr('class', 'progress-bar');
			if (settings.progressType) {
				$dialog.find('.progress-bar').addClass('progress-bar-' + settings.progressType);
			}
			$dialog.find('label').text(message);
			// Adding callbacks
			if (typeof settings.onHide === 'function') {
				$dialog.off('hidden.bs.modal').on('hidden.bs.modal', function (e) {
					settings.onHide.call($dialog);
				});
			}
			// Opening dialog
			$dialog.modal();
		},
		/**
		 * Closes dialog
		 */
		hide: function () {
			$dialog.modal('hide');
		}
	};

})(jQuery);

// =================================================================================================================================
// Object
// =================================================================================================================================

// Event Key
// function enterKey(element, obj2){
// 	$(element).keydown(function(e) {
// 		var event = e || window.event;
// 		if (event.keyCode === 222 || event.keyCode === 220){
// 			return false;
// 		}else if (event.which == 13) {
// 			$(obj2).attr('disabled', false).focus();
// 		}
// 	});
// };

function enKey(element, next_focus_element, null_element, msg) {
	$(element).keydown(function (e) {
		var event = e || window.event;
		if (event.keyCode === 222 || event.keyCode === 220) {
			return false;
		} else if (event.which == 13) {
			if (null_element == false || null_element == null) {
				if ($(element).val() == '') {
					if (msg == '' || msg == null) {
						msg_alert_warning(null, element);
					} else {
						msg_alert_warning(msg, element);
					}
				} else {
					$(next_focus_element).attr('disabled', false).focus();
				}
			} else if (null_element == true) {
				$(next_focus_element).attr('disabled', false).focus();
			}
		}
	});
};

function enKeyCombo(element, next_focus_element, null_element, msg) {
	if ($(window).width() <= 768) {

		$(element).on('change', function () {
			if (null_element == false || null_element == null) {
				if (this.value == '') {
					if (msg == '' || msg == null) {
						msg_alert_warning(null, element);
					} else {
						msg_alert_warning(msg, element);
					}
				} else {
					$(next_focus_element).attr('disabled', false).focus();
				}
			} else if (null_element == true) {
				$(next_focus_element).attr('disabled', false).focus();
			}
		});

	} else {

		$(element).keydown(function (e) {
			var event = e || window.event;
			if (event.keyCode === 222 || event.keyCode === 220) {
				return false;
			} else if (event.which == 13) {
				if (null_element == false || null_element == null) {
					if (this.value == '') {
						if (msg == '' || msg == null) {
							msg_alert_warning(null, element);
						} else {
							msg_alert_warning(msg, element);
						}
					} else {
						$(next_focus_element).attr('disabled', false).focus();
					}
				} else if (null_element == true) {
					$(next_focus_element).attr('disabled', false).focus();
				}
			}
		});

	}
};

// // String Key
// function strKey(e, decimal) {
// 	var key;
// 	var keychar;
// 	if (window.event) {
// 		key = window.event.keyCode;
// 	} else if (e) {
// 		key = e.which;
// 	} else {
// 		return true;
// 	}

// 	keychar = String.fromCharCode(key);
// 	if ((key == null) || (key == 0) || (key == 8) || (key == 9) || (key == 27)) {
// 		return true;
// 	} else if ((("0123456789-").indexOf(keychar) > -1)) {
// 		return true;
// 	} else if (decimal && (keychar == ".")) {
// 		return true;
// 	} else {
// 		return false;
// 	}
// };

// // Number Key
// function numbKey(e, decimal) {
// 	var key;
// 	var keychar;
// 	if (window.event) {
// 		key = window.event.keyCode;
// 	} else if (e) {
// 		key = e.which;
// 	} else {
// 		return true;
// 	}

// 	keychar = String.fromCharCode(key);
// 	if ((key == null) || (key == 0) || (key == 8) || (key == 9) || (key == 27)) {
// 		return true;
// 	} else if ((("0123456789").indexOf(keychar) > -1)) {
// 		return true;
// 	} else if (decimal && (keychar == ".")) {
// 		return true;
// 	} else {
// 		return false;
// 	}
// };

// function numberKey(element, next_focus_element, minLength, xzero, msg) {
// 	$(element).keydown(function (e) {
// 		var event = e || window.event;
// 		if (event.keyCode === 222 || event.keyCode === 220) {
// 			return false;
// 		} else if (event.which == 13) {
// 			// Jika 0 = true
// 			// Jika tidak 0 = false
// 			if (xzero == true) {
// 				if ($(element).val().length <= minLength || $(element).val() == '0') {
// 					if (msg == '' || msg == null) {
// 						msg_alert_warning('Data harus diisi !', element);
// 					} else {
// 						msg_alert_warning(msg, element);
// 					}
// 				} else {
// 					$(next_focus_element).attr('disabled', false).focus();
// 				}

// 				// Jika Nilai kurang dari
// 			} else {
// 				if ($(element).val().length <= minLength) {
// 					if (msg == '') {
// 						msg_alert_warning('Data harus diisi !', element);
// 					} else {
// 						msg_alert_warning(msg, element);
// 					}
// 				} else {
// 					$(next_focus_element).attr('disabled', false).focus();
// 				}
// 			}
// 		}
// 	});
// };

// // Desimal Key
// function desKey(e, decimal) {
// 	var key;
// 	var keychar;
// 	if (window.event) {
// 		key = window.event.keyCode;
// 	} else if (e) {
// 		key = e.which;
// 	} else {
// 		return true;
// 	}

// 	keychar = String.fromCharCode(key);
// 	if ((key == null) || (key == 0) || (key == 8) || (key == 9) || (key == 27)) {
// 		return true;
// 	} else if ((("0123456789").indexOf(keychar) > -1)) {
// 		return true;
// 	} else if (decimal && (keychar == ".")) {
// 		return true;
// 	} else {
// 		return false;
// 	}
// };

// ReadOnly Object
// function roKey(element, next_focus_element) {
// 	$(element).keydown(function (e) {
// 		var event = e || window.event;
// 		if (event.keyCode === 222 || event.keyCode === 220) {
// 			return false;
// 		} else if (event.which == 13) {
// 			if ($(element).val() == '') {
// 				msg_alert('Data harus diisi !', element);
// 			} else {
// 				$(next_focus_element).attr('disabled', false);
// 				$(next_focus_element).css({ 'background': '#fff' });
// 				$(next_focus_element).attr('readonly', true).focus();
// 			}
// 		}
// 	});

// };

// // Enabled & ReadOnly Object
// function end_ro(element) {
// 	$(element).attr('disabled', false);
// 	$(element).attr('readonly', true);
// };

function oEvent(element, disabled) {
	if (disabled == true) {
		$(element).attr('disabled', disabled);
	} else if (disabled == false) {
		$(element).attr('disabled', disabled).focus();
	}
};

// Date Object
function enDate(e, element, next_focus_element) {
	var evt = e || window.event;
	if ($(element).is(":focus")) {
		$(next_focus_element).attr('disabled', true);
		if (evt.keyCode === 222 || evt.keyCode === 220) {
			return false;
		} else if (evt.keyCode === 13) {
			$(next_focus_element).attr('disabled', false).focus();
		}
	}
};

// function disabled_element(element) {
// 	$(element).css({ 'background': '#fff' });
// };

// function readonly_element(element) {
// 	$(element).css({ 'background': '#fff' });
// };

function enDateAgeManual(element, next_focus_element, value_age_element, msg) {
	$(element).keydown(function (e) {
		var event = e || window.event;
		if (event.keyCode === 222 || event.keyCode === 220) {
			return false;
		} else if (event.which == 13) {
			var tgl = this.value;
			if (this.value == '' || this.value == '__/__/____') {
				if (msg == '' || msg == null) {
					msg_alert_warning(null, element);
				} else {
					msg_alert_warning(msg, element);
				}
			} else if (tgl.substring(0, 2) > 31) {
				msg_alert_warning('Format tanggal salah !', element);
			} else if (tgl.substring(3, 5) > 12) {
				msg_alert_warning('Format bulan salah !', element);
			} else {
				$(value_age_element).val(hitUsia(this.value));
				$(next_focus_element).attr('disabled', false).focus();
			}
		}
	});

	$(element).blur(function () {
		if (this.value == '' || this.value == '__/__/____') {
			$(value_age_element).val('');
		} else {
			$(value_age_element).val(hitUsia(this.value));
		}
	});
};

function enDateManual(element, next_focus_element, null_element, msg) {
	$(element).keydown(function (e) {
		var event = e || window.event;
		if (event.keyCode === 222 || event.keyCode === 220) {
			return false;
		} else if (event.which == 13) {
			var tgl = this.value;
			if (null_element == true) {
				$(next_focus_element).attr('disabled', false).focus();

			} else if (null_element == false || null_element == null) {
				if (this.value == '' || this.value == '__/__/____') {
					if (msg == '' || msg == null) {
						msg_alert_warning(null, element);
					} else {
						msg_alert_warning(msg, element);
					}
				} else if (tgl.substring(0, 2) > 31) {
					msg_alert_warning('Format tanggal salah !', element);
				} else if (tgl.substring(3, 5) > 12) {
					msg_alert_warning('Format bulan salah !', element);
				} else {
					$(next_focus_element).attr('disabled', false).focus();
				}
			}
		}
	});
};

function setModalMaxHeight(element) {
	this.$element = $(element);
	this.$content = this.$element.find('.modal-content');
	var borderWidth = this.$content.outerHeight() - this.$content.innerHeight();
	var dialogMargin = $(window).width() < 768 ? 20 : 60;
	var contentHeight = $(window).height() - (dialogMargin + borderWidth);
	var headerHeight = this.$element.find('.modal-header').outerHeight() || 0;
	var footerHeight = this.$element.find('.modal-footer').outerHeight() || 0;
	var maxHeight = contentHeight - (headerHeight + footerHeight);

	this.$content.css({
		'overflow': 'hidden'
	});

	this.$element
		.find('.modal-body').css({
			'max-height': maxHeight,
			'overflow-y': 'auto'
		});
};

function dishome() {
	$('#left-panel').css({
		'background': 'grey',
		'-webkit-transition': 'background-color 1000ms linear',
		'-moz-transition': 'background-color 1000ms linear',
		'-o-transition': 'background-color 1000ms linear',
		'-ms-transition': 'background-color 1000ms linear',
		'transition': 'background-color 1000ms linear',
		'-webkit-animation-direction': 'alternate',
		'animation-direction': 'alternate',
		'-webkit-animation-iteration-count': 2,
		'animation-iteration-count': 2
	});
	$('#left-panel nav ul li').css({ 'cursor': 'not-allowed' });
	$('#left-panel nav ul li a').css({ 'pointer-events': 'none' });
	$('#mobile-profile-img').css({ 'opacity': '0.5', 'pointer-events': 'none' })
};

function enhome() {
	$('#left-panel').css({ 'background': '#5ba0a3' });
	$('#left-panel nav ul li').css({ 'cursor': 'default' });
	$('#left-panel nav ul li a').css({ 'pointer-events': 'auto' });
	$('#mobile-profile-img').css({ 'opacity': '1', 'pointer-events': 'auto' })
};

function load_proses() {
	waitingDialog.show();
};

// =================================================================================================================================
// End Object
// =================================================================================================================================

// =================================================================================================================================
// Messages
// =================================================================================================================================

// Modal Message
function msg_alert(mPesan, mObj){
	var msg = "<h5><i class='fa fa-info-circle text-primary'></i>&nbsp;" + mPesan + "</h5>";
	var box = bootbox.alert(msg);
	box.on('hidden.bs.modal', function () {
		$(mObj).focus();
	});
};

function msg_alert_warning(mPesan, mObj) {
	if(mPesan=='' || mPesan==null){
		var msg = "<h6><i class='fa fa-warning text-danger'></i>&nbsp; Data harus diisi !</h6>";
	}else{
		var msg = "<h6><i class='fa fa-warning text-danger'></i>&nbsp;" + mPesan + "</h6>";
	}
	var box = bootbox.alert(msg);
	box.on('hidden.bs.modal', function () {
		oEvent(mObj, false);
	});
};

function loading_show(content) {
	$(content).prepend('<div class="overlay text-center" style="padding:10px;"><i class="fa fa-spinner fa-spin"  style="font-size:22px;"></i></div>');
};

function loading_hide() {
	$('.overlay').remove();
};

function msg_server_reloading() {
	var msg = "<h6><i class='fa fa-warning text-danger'></i>&nbsp;Server Reloading...!</h6>";
	var box = bootbox.alert(msg);
	box.on('hidden.bs.modal', function () {
		location.reload();
	});
};

// =================================================================================================================================
// End Messages
// =================================================================================================================================

// =================================================================================================================================
// Links
// =================================================================================================================================

function load_menu(routepage, xdata, content) {
	var myDiv = $(content);
	myDiv.html('');
	loading_show(content);
	// waitingDialog.show('Memuat...', { dialogSize: 'sm' });
	$.post(routepage, xdata)
		.done(function (response) {
			// waitingDialog.hide();
			myDiv.html(response);
			loading_hide();
		})
		.fail(function (response) {
			msg_server_reloading();
		})
};

function load_page(routepage, xdata, content) {
	// dishome();
	var myDiv = $(content);
	myDiv.html('');
	loading_show(content);
	$.post(routepage, xdata)
		.done(function (response) {
			myDiv.html(response);
			loading_hide();
		})
		.fail(function (response) {
			msg_server_reloading();
		})
};

function goto_home() {
	enhome();
	var myDiv = $('#content');
	myDiv.html('');
	loading_show('#content');
	$.post('/loadpage', { 'link': 'loadhome.html' })
		.done(function (response) {
			myDiv.html(response);
			loading_hide();
		})
		.fail(function (response) {
			msg_server_reloading();
		})
};

function goto_menu() {
	var lnk = $('#lnk').val();
	var idmenu = $('#idmenu').val();
	var desmenu = $('#title').val();
	enhome();
	var myDiv = $('#content');
	myDiv.html('');
	loading_show('#content');
	$.post('/gridmenu', { 'link': lnk, 'idmenu': idmenu, 'desmenu': desmenu })
		.done(function (response) {
			myDiv.html(response);
			loading_hide();
		})
		.fail(function (response) {
			msg_server_reloading();
		})
};

function open_popup_win(url, title, w, h) {
	var tops = Number((screen.height / 2) - (h / 2));
	var left = Number((screen.width / 2) - (w / 2));
	if (w == '' && h == '') {
		var win = window.open(url, title, "dialog=yes");
	} else {
		var win = window.open(url, title, "dialog=yes, width=" + w + ", height=" + h + ", top=" + tops + ", left=" + left);
	}
	win.focus();
	window.onmousedown = focusPopup;
	window.onkeyup = focusPopup;
	window.onmousemove = focusPopup;

	function focusPopup() {
		if (win && !win.closed) {
			win.focus();
		}
	}
};

function search_list(element, element_id, next_focus_element, url_root, min_length, msg, vdata, null_element, appendObj) {
	
	$(element).keydown(function (e) {
		var evt = e || window.event;
		if (evt.keyCode === 222 || evt.keyCode === 220) {
			return false;
		} else if (evt.keyCode === 13 || evt.Keycode == 9) {
			// Jika Obejek diperbolehkan Null/Kosong 'true'
			if (null_element == true) {
				// Fokus ke object berikutnya
				if (this.value == '' && $(element_id).val() == '') { $(next_focus_element).attr('disabled', false).focus();
				}
			} else if (null_element == false) {
				// Jika Obejek tidak diperbolehkan Null/Kosong 'false'
				if (this.value == '') {
					if (msg == '' || msg==null) {
                  msg_alert_warning(null, element);
					} else {
                  msg_alert_warning(msg, element); }
				} else if ($(element_id).val() != '' && this.value !='') {
               $(next_focus_element).attr('disabled', false).focus();
            }
			}
		} else {
			$(element_id).val('');
			
			$(element).autocomplete({
				source: function (request, response) {
					// $.post(url_root, {'cari': request.term, 'param1':param1, 'param2':param2, 'param3':param3, 'param4':param4, 'param5':param5}, function(data){
					var xdata = $.extend({}, { 'cari': request.term }, vdata);
					
					$.ajax({
						type: "post",
						url: url_root,
						dataType: 'json',
						data: xdata,
						success: function (data) {
							response($.map(data, function (item) {
								return {
									id: item.id,
									value: item.value,
									label: function () {
										if (!item.label) {
											return item.id + " - " + item.value
										} else {
											return item.id + " - " + item.value + ' - ' + item.label
										}
									}
								};
							}));
						}
					});
				},
				minLength: min_length,
				autoFocus: true,
				response: function (event, ui) {
					if (!ui.content.length) {
						var noResult = { id: "", value: "", label: "Data Tidak Diketemukan !" };
						ui.content.push(noResult);
					}
				},
				keydown: function (event, ui) {
					var evt = event || window.event;
					if (evt.Keycode == 13 || evt.Keycode == 9 ) {
						if (ui.item.value != '') {
							$(this).val(ui.item.value);
							$(element_id).val(ui.item.id);
							$(next_focus_element).attr('disabled', false).focus();
						}
					}
				},
				select: function (event, ui) {
					if (ui.item.value != '') {
						$(this).val(ui.item.value);
						$(element_id).val(ui.item.id);
						$(next_focus_element).attr('disabled', false).focus();
					}
				},
				appendTo: appendObj
			});
		}
	});
};

function confirm_posting(rootpage, param, modal, focus_element, error_callback_msg) {
	var dlg = bootbox.confirm({
		title: "<i class='fa fa-question-circle text-primary'></i>&nbsp;Konfirmasi",
		message: 'Lanjutkan Proses ?',
		buttons: {
			confirm: { label: 'Ya', className: 'btn-primary' },
			cancel: { label: 'Tidak', className: 'btn-danger' }
		},
		callback: function (result) {
			if (result) {
				waitingDialog.show('Proses...', { dialogSize: 'sm' });
				$.ajax({
					type: 'POST',
					url: rootpage,
					dataType: 'json',
					data: param,
					success: function (response) {
						waitingDialog.hide();
						if (response.status == '1') {
							var msg = "<h6><i class='fa fa-info-circle text-primary'></i>&nbsp;" + response.msg + "</h6>";
							var box = bootbox.alert(msg);
							box.on('hidden.bs.modal', function () {
								$(modal).modal('hide');
							});
						} else {
							msg_alert_warning(response.msg, focus_element);
						}
					},
					error: function (error) {
						console.log(error);
						waitingDialog.hide();
						if (error.status == 403) {
							msg_server_reloading();
						} else {
							if (error_callback_msg == '' || error_callback_msg == null) {
								msg_alert_warning('Data gagal diproses !', focus_element);
							} else {
								msg_alert_warning(error_callback_msg, focus_element);
							}
						}
					}
				});
			}
		}
	});
	dlg.on('hidden.bs.modal', function () {
		$(focus_element).focus();
	});
};

function confirm_list_table(rootpage, param, page_link, element_load, confirm_msg, error_callback_msg) {
	if (confirm_msg == '' || confirm_msg == null) {
		var msg = 'Lanjutkan Proses ?';
	} else {
		var msg = confirm_msg;
	};
	var box = bootbox.confirm({
		title: "<i class='fa fa-question-circle text-primary'></i>&nbsp;Konfirmasi",
		message: msg,
		buttons: {
			confirm: { label: 'Ya', className: 'btn-primary' },
			cancel: { label: 'Tidak', className: 'btn-danger' }
		},
		callback: function (result) {
			if (result) {
				waitingDialog.show('Proses...', { dialogSize: 'sm' });
				$.ajax({
					type: 'POST',
					url: rootpage,
					dataType: 'json',
					data: param,
					success: function (response) {
						waitingDialog.hide();
						if (response.status == '1') {
							var msg = "<h6><i class='fa fa-info-circle text-primary'></i>&nbsp;" + response.msg + "</h6>";
							var box = bootbox.alert(msg);
							box.on('hidden.bs.modal', function () {
								load_page('/loadpage', { 'link': page_link }, element_load);
							});
							$('#tbldetilbookingplg').DataTable().ajax.reload();
						} else {
							msg_alert_warning(response.msg);
						}
					},
					error: function (error) {
						console.log(error);
						waitingDialog.hide();
						if (error.status == 403) {
							msg_server_reloading();
						} else {
							if (error_callback_msg == '' || error_callback_msg == null) {
								msg_alert_warning('Data gagal diproses !');
							} else {
								msg_alert_warning(error_callback_msg);
							}
						}
					}
				});
			}
		}
	});
};
function confirm_list_table2(rootpage, param, page_link, element_load, confirm_msg, error_callback_msg) {
	if (confirm_msg == '' || confirm_msg == null) {
		var msg = 'Lanjutkan Proses ?';
	} else {
		var msg = confirm_msg;
	};
	var box = bootbox.confirm({
		title: "<i class='fa fa-question-circle text-primary'></i>&nbsp;Konfirmasi",
		message: msg,
		buttons: {
			confirm: { label: 'Ya', className: 'btn-primary' },
			cancel: { label: 'Tidak', className: 'btn-danger' }
		},
		callback: function (result) {
			if (result) {
				waitingDialog.show('Proses...', { dialogSize: 'sm' });
				$.ajax({
					type: 'POST',
					url: rootpage,
					dataType: 'json',
					data: param,
					success: function (response) {
						waitingDialog.hide();
						if (response.status == '1') {
							var msg = "<h6><i class='fa fa-info-circle text-primary'></i>&nbsp;" + response.msg + "</h6>";
							var box = bootbox.alert(msg);
							box.on('hidden.bs.modal', function () {
								if (param.key == 'Delete-updatehrg-pemasok'){
									load_page('/loadpaged', {'link':'/_hargapemasok/listhargapemasok.html','nosp':param.nosp}, '#showhargapemasok');
								} else if (param.key == 'Delete-updatehrg-prinsipal'){
									load_page('/loadpaged', {'link':'/_hargaprinsip/listhargaprinsipal.html','nosp':param.nosp}, '#showhargaprinsipal');
								}else{
									load_page('/loadpage', { 'link': page_link }, element_load);
								}
							});
						} else {
							msg_alert_warning(response.msg);
						}
					},
					error: function (error) {
						console.log(error);
						waitingDialog.hide();
						if (error.status == 403) {
							msg_server_reloading();
						} else {
							if (error_callback_msg == '' || error_callback_msg == null) {
								msg_alert_warning('Data gagal diproses !');
							} else {
								msg_alert_warning(error_callback_msg);
							}
						}
					}
				});
			}
		}
	});
};

// =================================================================================================================================
// End Links
// =================================================================================================================================

// =================================================================================================================================
// Functions
// =================================================================================================================================

function iDate(param) {
	// 0000-00-00 > 00/00/0000
	var d, m, y, tgl
	d = param.substr(8, 10);
	m = param.substr(5, 6);
	y = param.substr(0, 4);
	tgl = d + '/' + m + '/' + y;
	return tgl
};

function mDate(param) {
	// 00/00/0000 > 0000-00-00
	var d, m, y, tgl
	d = param.substr(0, 2);
	m = param.substr(3, 4);
	y = param.substr(6, 10);
	tgl = y + '-' + m + '-' + d;
	return tgl
};

function hitUsia(tgllhr) {
	var usia = "";
	var tanggal = parseInt(tgllhr.substring(0, 2), 10);
	var bulan = parseInt(tgllhr.substring(3, 5), 10);
	var tahun = parseInt(tgllhr.substring(6, 10), 10);

	var tglsekarang = new Date();
	var ultah = new Date(tahun, bulan - 1, tanggal);
	var differenceInMilisecond = tglsekarang.valueOf() - ultah.valueOf();
	var uHr = Math.floor((differenceInMilisecond % 31536000000) / 86400000);
	var uBln = Math.floor(uHr / 30);
	var uThn = Math.floor(differenceInMilisecond / 31536000000);
	uHr = uHr % 30;

	// Hitung Umur Hari
	if (uThn == 0 && uBln == 0 && uHr != 0) {
		usia = uHr + " Hr";

		// Hitung Umur Bulan
	} else if (uThn == 0 && uBln != 0 && uHr == 0) {
		usia = uBln + " Bln";

		// Hitung Umur Tahun
	} else if (uThn != 0 && uBln == 0 && uHr == 0) {
		usia = uThn + " Thn";

		// Hitung Umur Tahun, Bulan
	} else if (uThn != 0 && uBln != 0 && uHr == 0) {
		usia = uThn + " Thn, " + uBln + " Bln";

		// Hitung Umur Tahun, Hari
	} else if (uThn != 0 && uBln == 0 && uHr != 0) {
		usia = uThn + " Thn, " + uHr + " Hr";

	} else {
		usia = uThn + " Thn, " + uBln + " Bln, " + uHr + " Hr";
	}
	return usia
};

function addZero(i) {
	if (i < 10) {
		i = "0" + i;
	}
	return i;
}

function iCurDateNow(target) {
	var tgl = new Date();
	var dd = addZero(tgl.getDate());
	var mm = addZero(tgl.getMonth() + 1); //January is 0!
	var yyyy = tgl.getFullYear();

	tgl = dd + '/' + mm + '/' + yyyy;
	$(target).val(tgl);
};

function iCurDateNow2() {
	var tgl = new Date();
	var dd = addZero(tgl.getDate());
	var mm = addZero(tgl.getMonth() + 1); //January is 0!
	var yyyy = tgl.getFullYear();

	tgl = dd + '/' + mm + '/' + yyyy;
	return tgl;
};

function mCurDateNow(target) {
	var tgl = new Date();
	var dd = addZero(tgl.getDate());
	var mm = addZero(tgl.getMonth() + 1); //January is 0!
	var yyyy = tgl.getFullYear();

	tgl = yyyy + '/' + mm + '/' + dd;
	$(target).val(tgl);
};

function mCurDateNow2() {
	var tgl = new Date();
	var dd = addZero(tgl.getDate());
	var mm = addZero(tgl.getMonth() + 1); //January is 0!
	var yyyy = tgl.getFullYear();

	tgl = yyyy + '-' + mm + '-' + dd;
	return tgl;
};

function CurTimeNow(target) {
	var tgl = new Date();
	var H = addZero(tgl.getHours());
	var M = addZero(tgl.getMinutes());
	var S = addZero(tgl.getSeconds());

	jam = H + ':' + M + ':' + S;
	$(target).val(jam);
};

function CurTimeNow2(target) {
	var tgl = new Date();
	var H = addZero(tgl.getHours());
	var M = addZero(tgl.getMinutes());
	var S = addZero(tgl.getSeconds());

	jam = H + ':' + M;
	$(target).val(jam);
};

function iCurDateTimeNow() {
	var n = new Date(),
      dd = addZero(n.getDate()),
      mm = addZero(n.getMonth() + 1),
      yyyy = n.getFullYear(),
      h = addZero(n.getHours()),
      m = addZero(n.getMinutes()),
      s = addZero(n.getSeconds());
			
	return dd+'/'+mm+'/'+yyyy+' '+h+':'+m+':'+s;
};

function insertAtCaret(areaId, text) {
	var txtarea = document.getElementById(areaId);
	var scrollPos = txtarea.scrollTop;
	var strPos = 0;
	var br = ((txtarea.selectionStart || txtarea.selectionStart == '0') ?
		"ff" : (document.selection ? "ie" : false));
	if (br == "ie") {
		txtarea.focus();
		var range = document.selection.createRange();
		range.moveStart('character', -txtarea.value.length);
		strPos = range.text.length;
	}
	else if (br == "ff") strPos = txtarea.selectionStart;

	var front = (txtarea.value).substring(0, strPos);
	var back = (txtarea.value).substring(strPos, txtarea.value.length);
	txtarea.value = front + text + back;
	strPos = strPos + text.length;
	if (br == "ie") {
		txtarea.focus();
		var range = document.selection.createRange();
		range.moveStart('character', -txtarea.value.length);
		range.moveStart('character', strPos);
		range.moveEnd('character', 0);
		range.select();
	} else if (br == "ff") {
		txtarea.selectionStart = strPos;
		txtarea.selectionEnd = strPos;
		txtarea.focus();
	}
	txtarea.scrollTop = scrollPos;
};

function uHari(tgllhr) {
	var tanggal = parseInt(tgllhr.substring(0, 2), 10);
	var bulan = parseInt(tgllhr.substring(3, 4), 10);
	var tahun = parseInt(tgllhr.substring(6, 10), 10);

	var tglsekarang = new Date();
	var ultah = new Date(tahun, bulan - 1, tanggal);
	var differenceInMilisecond = tglsekarang.valueOf() - ultah.valueOf();
	var uHr = Math.floor((differenceInMilisecond % 31536000000) / 86400000);
	uHr = uHr % 30;

	return uHr
};

function uBulan(tgllhr) {
	var tanggal = parseInt(tgllhr.substring(0, 2), 10);
	var bulan = parseInt(tgllhr.substring(3, 5), 10);
	var tahun = parseInt(tgllhr.substring(6, 10), 10);

	var tglsekarang = new Date();
	var ultah = new Date(tahun, bulan - 1, tanggal);
	var differenceInMilisecond = tglsekarang.valueOf() - ultah.valueOf();
	var uHr = Math.floor((differenceInMilisecond % 31536000000) / 86400000);
	var uBln = Math.floor(uHr / 30);

	return uBln
};

function uTahun(tgllhr) {
	var tanggal = parseInt(tgllhr.substring(0, 2), 10);
	var bulan = parseInt(tgllhr.substring(3, 5), 10);
	var tahun = parseInt(tgllhr.substring(6, 10), 10);

	var tglsekarang = new Date();
	var ultah = new Date(tahun, bulan - 1, tanggal);
	var differenceInMilisecond = tglsekarang.valueOf() - ultah.valueOf();
	var uHr = Math.floor((differenceInMilisecond % 31536000000) / 86400000);
	var uBln = Math.floor(uHr / 30);
	var uThn = Math.floor(differenceInMilisecond / 31536000000);

	return uThn
};

function auto_height_table(element_load_table){
   var h_window = window.innerHeight,
      h_header = $('#header').height(),
      h_left_panel = $('#left-panel').height(),
      t_left_panel = $('#left-panel').offset().top,
      h_footer = $('#pagefooter').height(),
      t_load_table = $(element_load_table).offset().top;
   
   if($(window).width() > 1024){
      h = String(h_window - (h_header + h_left_panel + h_footer + t_load_table) - 37);
   }else{
      h = String(h_window - (h_header + h_footer + t_load_table) - 105);
   }
   
   return h;
};

function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}
// =================================================================================================================================
// End Functions
// =================================================================================================================================
