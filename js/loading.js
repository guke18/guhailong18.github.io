function applyHover() {
  var animatedItemsArr = $.makeArray($('.animated'));
  var animationDuration = 750; //ms
  var animationOffset = 400; //ms
  animatedItemsArr.map(function(item, index) {
    setTimeout(function() {
      $(item).addClass('secondary');
    }, animationDuration + ((index) * animationOffset))
  });
}

// For reloading the animaiton :)
$('.reload-button').on('click', function() {
  $('.secondary').removeClass('secondary');
  $('.animated').removeClass('animated');
  setTimeout(function() {
    $('.stack-illustration__item').addClass('animated');
    applyHover();
  }, 1);
})

$( document ).ready( applyHover );
