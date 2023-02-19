 function cariinduk(){
    $("#nminduk").empty();
    $("#cnminduk").empty();
    $("#nminduk").append("<option value=''></option> selected");
    $("#cnminduk").append("<option value=''></option> selected");
    $.ajax({
        type    : 'POST',
        url     : '/cariinduk',
        dataType: 'json',
        success : function(response){
            // alert(response.data.length);
            for ( var i=0; i < response.data.length; i++){
                $("#nminduk").append("<option value='"+response.data[i]['id']+"'>"+ response.data[i]['value'] +"</option>"); 
                $("#cnminduk").append("<option value='"+response.data[i]['id']+"'>"+ response.data[i]['value'] +"</option>"); 
            }
        }
    });

 }
 function carileader(){
    $("#nmleader").empty();
    $("#nmleader").append("<option value=''></option> selected");
    $.ajax({
        type    : 'POST',
        url     : '/carileader',
        dataType: 'json',
        success : function(response){
            // alert(response.data.length);
            for ( var i=0; i < response.data.length; i++){
                $("#nmleader").append("<option value='"+response.data[i]['id']+"'>"+ response.data[i]['value'] +"</option>"); 
            }
        }
    });

 }

 function cariopr(){
    $("#nmopr").empty();
    $("#nmopr").append("<option value=''></option> selected"); 
  
    
    $.ajax({
        type    : 'POST',
        url     : '/cariopr',
        dataType: 'json',
        success : function(response){
            // alert(response.data.length);
            for ( var i=0; i < response.data.length; i++){
                $("#nmopr").append("<option value='"+response.data[i]['id']+"'>"+ response.data[i]['value'] +"</option>"); 
            }
           
        }
    });

 }

 function caripoint(){
    var xinduk = $('#nminduk').val();
    $("#nmpoint").empty();
    $("#nmpoint").append("<option value=''></option>");
    $.ajax({
        type    : 'POST',
        url     : '/caripoint',
        dataType: 'json',
        data    : {'induk':xinduk},
        success : function(response){
            // alert(response.data.length);
            for ( var i=0; i < response.data.length; i++){
                $("#nmpoint").append("<option value='"+response.data[i]['id']+"'>"+ response.data[i]['value'] +"</option>"); 
            }
        }
    });
};
function caripoint2(){
    var xinduk = $('#cnminduk').val();
    $("#cnmpoint").empty();
    $("#cnmpoint").append("<option value=''></option>");
    $.ajax({
        type    : 'POST',
        url     : '/caripoint',
        dataType: 'json',
        data    : {'induk':xinduk},
        success : function(response){
            // alert(response.data.length);
            for ( var i=0; i < response.data.length; i++){
                $("#cnmpoint").append("<option value='"+response.data[i]['id']+"'>"+ response.data[i]['value'] +"</option>"); 
            }
        }
    });
};

