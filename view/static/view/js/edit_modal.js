$(window).on("load", function () {
  $("#editModal").on("shown.bs.modal", function (event) {
    const button = $(event.relatedTarget);
    const bookmarkCard = button.closest(".card");

    const bookmarkURL = bookmarkCard.data("bookmark-show-url");

    $.ajax({
      url: bookmarkURL,
      type: "GET",
      datatype: "json",
      success: function (response) {
        const [model] = JSON.parse(response);

        $("#editModal .modal-title-placeholder").attr("placeholder", model.fields.title);
      },
      error: function (response) {
        console.log("Error:", response);
      },
    });
  });
});
