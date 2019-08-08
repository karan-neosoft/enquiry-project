
$(document).ready(function(){
  $(".submit-btn").click(function(){
    var formdata = $("#enquiry-form").serialize();
    // console.log(formdata);
    // alert("thisis a ")
    $.ajax({
        type:"POST",
        url:'enquiry-submit',
        data:formdata,
        success:function(response){
            console.log(response);
            // data  = response.reverse();
            for(i in response)
                {
                  if (i != 'status')
                  {
                    $("#msg").html(i +" "+response[i]);
                  }
                  else{
                    $("#msg").html(response[i]);
                  }
                }
        }
    })
  });


  $(".edit-btn").click(function(){
    var formdata = $("#enquiry-form-edit").serialize();
    // console.log(formdata);
    // alert("thisis a ")
    $.ajax({
        type:"POST",
        url:'edit-action',
        data:formdata,
        success:function(response){
            console.log(response);
            // data  = response.reverse();
            for(i in response)
                {
                  if (i != 'status')
                  {
                    $("#msg").html(i +" "+response[i]);
                  }
                  else{
                    $("#msg").html(response[i]);
                    setTimeout(2000);
                    window.location.href = "/";
                  }
                }
        }
    })
  });

  
  $(".admin-lg-btn").click(function(){
      var formdata = $("#admin-login-form").serialize();
      $.ajax({
        type:"POST",
        url:'login-action',
        data:formdata,
        success:function(response){
            // console.log(response);
            if (response['flag']==1)
            {
            $("#msg").html(response['status'])
            console.log("sucess");
            window.location.href = "/";
            }
            else{
              $("#msg").html(response['status'])
              console.log("error");
            }
        }
    })

  });


});
