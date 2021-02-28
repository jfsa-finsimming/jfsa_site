$(function(){
  $('.navi__btn').on('click',function(){
    var rightVal = 0;
    if($(this).hasClass('hb-open')){
      rightVal = -300;
      $(this).removeClass('hb-open');
    }else{
      $(this).addClass('hb-open');
    }

    $('.navi__global').stop().animate({
      right: rightVal
    }, 200);
  });
});
