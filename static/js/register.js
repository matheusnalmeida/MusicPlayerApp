// https://github.com/CodeSeven/toastr

$(document).ready(function(){
    $("#register-user-form").submit(function(event) {
      event.preventDefault()
      event.stopPropagation()      

      var form = $(this);
      var actionUrl = form.attr('action');
      
      var usernameFilled = !!$("#username-input").val().trim()
      var userFilled = !!$("#username-input").val().trim()
      var passwordFilled = !!$("#password-input").val().trim()

      if (!usernameFilled || !userFilled || !passwordFilled) {          
        toastr.error('Por favor preencha todos os dados para seguir com o cadastro!')
        return;
      }

      $.ajax({
          type: "POST",
          url: actionUrl,
          data: form.serialize(),
          success: function(data)
          {
            mensagem = data.message
            if(data.success)
            {
              sessionStorage.setItem('sucessRegister', mensagem)
              window.location.href = data.url
              return;
            }
            toastr.error(mensagem)
          },
          error: function (data) {
            toastr.error('Ocorreu um erro ao tentar registrar um usuário. Contate o administrador!')
        }
      });      
  });
});