function utilizou_hora_extra(object){
    
    console.log(object)
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
   
    $.ajax(
        {
            type: 'POST',
            url: '/acounts/perfil/',
            data: {csrfmiddlewaretoken: token},
            
            success: function(result){
                console.log("Funcionou")
                $("#mensagem").text(result.mensagem)
            }
        }
    );

}