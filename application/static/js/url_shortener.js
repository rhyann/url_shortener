window.onload = start;

function start () {
$('#blank').hide();
document.getElementById('shorten').onclick = shorten;
if (document.layers){ 
document.captureEvents(Event.KEYPRESS);
document.onkeypress = ExecuteOnEnter;
}
var reg =  /(ftp|http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?/;

function ExecuteOnEnter(e) {
   var keycode;
   if (window.event) {
   keycode = window.event.keyCode
   } else if (e) {keycode = e.which;}
   if (keycode == 13) {
   shorten();
   }
}
	


function shorten() {
$('#blank').hide();
$('#blank').addClass('results');
var longUrl = $('#longurl').val();

if (longUrl == "") {
 	alert("Please enter url");
 } else if (!reg.test(longUrl)) {
	alert("Not a valid url(remember  to add http://)");
}  
else {  
        var url = $SCRIPT_ROOT + '/create?longUrl=' +escape(longUrl);
	$.getJSON(url, function(resp) {
		$('.results').html('<p>Short URL: <a target="_blank" href=' + resp.result.data.url +'>' +resp.result.data.url +'</a></p><p>'
		                      +'Hash: ' +resp.result.data.hash +'</p><p>'
		                      +'Long URL: ' +unescape(resp.result.data.longUrl) +'</p>');
  	});
  	$('.results').fadeIn('slow');
}
}
}
