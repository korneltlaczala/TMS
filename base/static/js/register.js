document.addEventListener('DOMContentLoaded', function() {

    pulseErrorMessageBox();

    const form = document.querySelector('form');
    const usernameInput = document.getElementById('username');
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');
    const password2Input = document.getElementById('password2');
    const agree = document.getElementById('agree');
    const submitButton = document.querySelector('.submit');

    usernameInput.addEventListener('input', validateUsernameInput);
    emailInput.addEventListener('input', validateEmailInput);
    passwordInput.addEventListener('input', validatePasswordInput);
    password2Input.addEventListener('input', validatePassword2Input);
    agree.addEventListener('change', validateAgree);

    form.addEventListener('input', validateForm);

    function validateUsernameInput() {
        const username = usernameInput.value;
        valid = true;
        if (!/^[a-zA-Z0-9_]+$/.test(username) ||
            username.length < 5 ||
            username.length > 20) {
            valid = false;
        }
        validateInput(usernameInput, valid);
        return valid;
    }

    function validateEmailInput() {
        const email = emailInput.value;
        valid = true;
        if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
            valid = false;
        }
        validateInput(emailInput, valid);
        return valid;
    }

    function validatePasswordInput() {
        const password = passwordInput.value;
        valid = true;
        if (password.length < 8 ||
            !/[A-Z]/.test(password) ||
            !/[a-z]/.test(password) ||
            !/[0-9]/.test(password) ||
            !/[!@#$%^&*(),.?":{}|<>]/.test(password)) {
            valid = false;
        }
        
        validateInput(passwordInput, valid);
        return valid;
    }

    function validatePassword2Input() {
        const password = passwordInput.value;
        const password2 = password2Input.value;
        valid = true;
        if (password !== password2) {
            valid = false;
        }
        validateInput(password2Input, valid);
        return valid;
    }

    function validateAgree() {
        valid = agree.checked;
        validateInput(agree, valid);
        return valid;
    }

    function validateInput(input, valid) {
        if (valid) {
            input.classList.remove('invalid-input');
            input.classList.add('valid-input');
        } else {
            input.classList.remove('valid-input');
            input.classList.add('invalid-input');
        }
    }

    function check_empty() {
        for (const input of [usernameInput, emailInput, passwordInput, password2Input]) {
            if (input.value === '') {
                input.classList.remove('invalid-input');
                input.classList.remove('valid-input');
            }
        }
    }

    function validateForm() {
        valid = validateUsernameInput() &&
                validateEmailInput() &&
                validatePasswordInput() && 
                validatePassword2Input() && 
                validateAgree();
        check_empty();
        submitButton.disabled = !valid;
        return valid;
    }

    function wait(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    function pulseErrorMessageBox() {
        const messageBox = document.querySelector('.error-message-box');
        messageBox.classList.add('pulse');
        wait(500).then(() => {messageBox.classList.remove('pulse');})
    };

});