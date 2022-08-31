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

  setActive();
}

function setActive() {
  const current = $("#nodraft-inject").data("url");

  $(".nodraft-dynamic").each(function () {
    if (current === $(this).attr("href")) {
      $(this).addClass("active");
    } else $(this).removeClass("active");
  });
}

$(window).on("load", function () {
  // Initial load
  retrievePage();

  // Bind links for dynamic loading
  $(".nodraft-dynamic").click(function (event) {
    event.preventDefault();

    const url = $(this).attr("href");
    $("#nodraft-inject").data("url", url).attr("data-url", url);

    retrievePage();
  });
});
