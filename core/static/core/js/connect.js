document.getElementById('jQueryLoad').addEventListener('load', function () {
    const authentication_token = $("#auth_token").val();
    const editorExtensionId = "bjemlddlpahnmmjidgpobkbpkdackejp";

    $("#connectForm").submit(function (event) {
        event.preventDefault();

        // Make a simple request:
        chrome.runtime.sendMessage(editorExtensionId, { token: authentication_token },
            function (response) {
                if (!response.success)
                    handleError(authentication_token);
            });
    });
});