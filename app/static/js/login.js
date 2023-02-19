$(document).ready(function(){
    $('#username').focus();
    $('#username').keydown(function(e) {
		var event = e || window.event;
		if (event.keyCode === 222 || event.keyCode === 220){
			return false;
		}else if (event.which == 13) {
            $('#password').focus();
		}
    });
    
    $('#password').keydown(function(e) {
        var event = e || window.event;
		if (event.keyCode === 222 || event.keyCode === 220){
			return false;
		}else if (event.which == 13) {
            $('#login').focus();
		}
    });
    
    $("#login").click(function(e) {
        var usrname = $('#username').val(),
            passusr = $('#password').val();
        if(usrname==''){ msg_alert_warning("Username tidak boleh kosong !");
        }else if(passusr==''){ alert("Kata sandi tidak boleh kosong");
        }else{
            var xdata = 'username='+usrname+'&password='+$.md5(passusr);
            $.ajax({
                type: "POST",
                url: '/login',
                dataType: 'json',
                data: xdata,
                success: function(response){
                    if(response.status==0){
                        msg_alert_warning(response.msg, '#username');
                    }else{
                        waitingDialog.show('Memuat..',{dialogSize:'sm'});
                        setTimeout(function(){
                            waitingDialog.hide();
                            if (passusr == "1234567890"){
                                msg_alert_warning("Silahkan lakukan perubahan password !!");
                                window.location = "/rubahpassword";
                            }else{
                                window.location = response.url;
                            }
                            
                            // window.location = "/home";
                        }, 100);
                    }
        
                },
                error: function(error) {
                    console.log(error);
                }
            });
        }
    });
});