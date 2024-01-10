const $ = window.$
$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data, testStatus) {
  $('DIV#hello').text(data.hello);
});
