$(document).ready(function(){
  $(".child,.child_hover").hide();
  $("body").hide();
  $(".whatuwant ,.work1,.work2,.work3,.work4,.work5").hide();
  $("body").fadeIn(800,function(){
    $(".whatuwant").fadeIn();
  }); 
  $(window).scroll(function () {
    var scrollTop = $(window).scrollTop();
    if(scrollTop>400){
     $(".navbar").css({
      "background-color":"rgba(0,0,0,.5)"
    });
   }
   else{
     $(".navbar").css({
      "background":"transparent"
    });
   }
   if(scrollTop>210){
    $(".work1,.work2").fadeIn();
  }
  if(scrollTop>680){
    $(".work3,.work4,.work5").fadeIn();
  }
  if(scrollTop>=2500){
    $(".carousel-container").fadeIn(1000);
  }
  else{
    $(".carousel-container").fadeOut();
  }
  console.log(scrollTop);
});
  var carousel = $("#carousel").featureCarousel({
          // include options like this:
          // (use quotes only for string values, and no trailing comma after last option)
          // option: value,
          // option: value
        });

  $("#but_prev").click(function () {
    carousel.prev();
  });
  $("#but_pause").click(function () {
    carousel.pause();
  });
  $("#but_start").click(function () {
    carousel.start();
  });
  $("#but_next").click(function () {
    carousel.next();
  });
  $(".modal-image").hover(function(){

  $(".child").toggle(100).hover(function(){
    $(".child_hover").toggle();
  });
});

});