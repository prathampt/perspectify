$(".book-bg").click(function () {
    $(this).addClass("active");
  });
  
  $("#back svg").click(function () {
    event.stopPropagation();
    $(".book-bg").removeClass("active");
  });
  