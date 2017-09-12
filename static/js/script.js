
    $("header .navbar ").on("click", function() {
      $("header .navbar-default .navbar-nav .active a").removeClass("active");
      $(this).addClass("active");
    });