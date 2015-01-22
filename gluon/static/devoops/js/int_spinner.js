$(document).ready(function () {
  $('.int_spinner .btn:first-of-type').on('click', function() {
    $('.int_spinner input').val( parseInt($('.int_spinner input').val(), 10) + 1);
  });
  $('.int_spinner .btn:last-of-type').on('click', function() {
    $('.int_spinner input').val( parseInt($('.int_spinner input').val(), 10) - 1);
  });
  $('.time_spinner .btn:first-of-type').on('click', function() {
    $('.time_spinner input').val( Math.min( parseInt($('.time_spinner input').val(), 10) + 1, 23));
    $( this ).parent().parent().children('input').trigger('change')
  });
  $('.time_spinner .btn:last-of-type').on('click', function() {
    $('.time_spinner input').val( Math.max( parseInt($('.time_spinner input').val(), 10) - 1, 0));
    $( this ).parent().parent().children('input').trigger('change')
  });
});
