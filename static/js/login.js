$(document).ready(function(){
    $("#login-form").submit(function (event) {
        var userFilled = !!$("#user-input").val().trim()
        var passwordFilled = !!$("#password-input").val().trim()
        if (!userFilled || !passwordFilled) {          
          toastr.error('Por favor preencha todos os dados para seguir com o login!')
          event.preventDefault()
          event.stopPropagation()
        }
        //sessionStorage.setItem('sucessRegister', 'Usuário registrado com sucesso!')
    });
});