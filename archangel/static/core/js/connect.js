document.getElementById('jQueryLoad').addEventListener('load', function () {
    const authentication_token = $("#auth_token").val();

    $("#connectForm").submit(function (event) {
        event.preventDefault();
        console.log('Existing token', window.localStorage.getItem('keep-extension-token'));
        window.localStorage.setItem('keep-extension-token', authentication_token);
    });
});