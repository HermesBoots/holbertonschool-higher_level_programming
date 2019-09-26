$(function () {
  $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (body) {
    $('div#hello').text(body.hello);
  });
});
