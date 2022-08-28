document.getElementById('jQueryLoad').addEventListener('load', function () {
    const authentication_token = $("#auth_token").val();
    const editorExtensionId = "mchcicmnbpcopfmklilbmbjgdmhlkapf";

    $("#connectForm").submit(function (event) {
        event.preventDefault();

        alert("Making request");

        // Make a simple request:
        chrome.runtime.sendMessage(editorExtensionId, { token: authentication_token },
            function (response) {
                console.log(response);
                if (!response.success)
                    handleError(authentication_token);
            });
    });
});