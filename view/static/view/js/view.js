function retrievePage() {
  $.ajax({
    url: $("#nodraft-inject").data("url"),
    type: "GET",
    success: function (response) {
      $("#nodraft-inject").html(response);
    },
    error: function (response) {
      console.log("Something went wrong!");
    },
  });
}

function requestPageRetrieval(event) {
  event.preventDefault();

  alert("clicked");
}

$(window).on("load", function () {
  // Initial load
  retrievePage();

  // Bind links for dynamic loading
  $(".nav-link").click(function (event) {
    event.preventDefault();

    const url = $(this).attr("href");
    $("#nodraft-inject").data("url", url);

    retrievePage();
  });
});
