document.getElementById('jQueryLoad').addEventListener('load', function () {
    const authentication_token = $("#auth_token").val();

    $("#connectForm").submit(function (event) {
        event.preventDefault();
        console.log('Existing token', window.localStorage.getItem('nodraft-extension-token'));
        window.localStorage.setItem('nodraft-extension-token', authentication_token);
    });
});