document.getElementById('jQueryLoad').addEventListener('load', function () {
  console.log("ready");
  const authentication_token = $("#auth_token").val();
  const editorExtensionId = "bjemlddlpahnmmjidgpobkbpkdackejp";

  $("#connectForm").submit(function (event) {
    event.preventDefault();

    console.log("Making request");

    // Make a simple request:
    chrome.runtime.sendMessage(editorExtensionId, { token: authentication_token },
      function (response) {
        console.log(response);
        if (!response.success)
          handleError(authentication_token);
      });
  });
});