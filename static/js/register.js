// https://github.com/CodeSeven/toastr

$(document).ready(function(){
    $("#register-user-form").submit(function (event) {
        var usernameFilled = !!$("#username-input").val().trim()
        var userFilled = !!$("#username-input").val().trim()
        var passwordFilled = !!$("#password-input").val().trim()
        if (!usernameFilled || !userFilled || !passwordFilled) {          
          toastr.error('Por favor preencha todos os dados para seguir com o cadastro!')
          event.preventDefault()
          event.stopPropagation()
        }
        sessionStorage.setItem('sucessRegister', 'Usuário registrado com sucesso!')
    });
});