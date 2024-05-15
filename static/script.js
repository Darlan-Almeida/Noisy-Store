
var emailInput = document.getElementById("email");

email.onkeyup = function () {
    if (!validarEmail()) {
        emailInput.setCustomValidity("O domínio do e-mail não é permitido.");
    }
    else {
        emailInput.setCustomValidity("");

    }

}

function validarEmail(event) {
    var email = emailInput.value;
    var allowedDomains = ["gmail.com", "outlook.com", "yahoo.com", "icloud.com", "hotmail.com", "aol.com", "protonmail.com", "mail.com", "zoho.com", "fastmail.com"];

    var emailDomain = email.split('@')[1];

    if (allowedDomains.indexOf(emailDomain) === -1) {
        return false; // Impede o envio do formulário
    }

    return true; // Permite o envio do formulário
}