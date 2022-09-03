$(window).on("load", function () {
  $("#search").on("keyup", function () {
    const url = $("#search-url").val();
    let value = $(this).val().toLowerCase();

    $.ajax({
      url: url,
      type: "GET",
      data: {
        query: value,
      },
      success: function (response) {
        $("#bookmarks-view").html(response);
      },
      error: function (error) {
        console.log(error);
      },
    });
  });
});
