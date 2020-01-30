$(document).on('mousemove', function(e) {
  e.preventDefault();
  if (this.time && (Date.now() - this.time) < 16) return;
  this.time = Date.now();
  let trail_character = '•';
  let mouse_x = e.originalEvent.x || e.originalEvent.layerX || 0;
  let mouse_y = e.originalEvent.y || e.originalEvent.layerY || 0;
  mouse_x = mouse_x + 20;
  mouse_y = mouse_y + 26;

  $('#cursor-trail').append(
    '<span class="cursor-trail--item" style="left:' +
    mouse_x +
    'px;top:' +
    mouse_y +
    'px;">' +
    trail_character +
    '</span>'
  );
  $('.cursor-trail--item').each(function() {
    let item = $(this);
    setTimeout(function() {
      $(item).remove();
    }, 900);
  });
});