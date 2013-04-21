/* Create the Client with a Capability Token */
Twilio.Device.setup("{{ token }}");

Twilio.Device.ready(function (device) {
  $("#log").text("Ready");
});

Twilio.Device.error(function (error) {
  $("#log").text("Error: " + error.message);
});

Twilio.Device.connect(function (conn) {
  $("#log").text("Successfully established call, have fun! ;)");
});

Twilio.Device.disconnect(function (conn) {
  $("#log").text("Call ended");
});

function call() {
  //get the phone number to connect the call to
  params = {"PhoneNumber1": $("#caller1").val(), "PhoneNumber2": $("#caller2").val(), "PhoneNumber3": $("#hidden3").val(), "PhoneNumber4": $("#hidden4").val(), "PhoneNumber5": $("#hidden5").val(), "State": $("#states").val()};
  Twilio.Device.connect(params);
}

function hangup() {
  Twilio.Device.disconnectAll();
}

var _gaq = _gaq || [];
_gaq.push(['_setaccount', 'ua-40159257-1']);
_gaq.push(['_setdomainname', 'prankroulette.com']);
_gaq.push(['_trackpageview']);

(function() {
  var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
  ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
  var s = document.getElementsByTagName('script')[0]; s.parentnode.insertBefore(ga, s);
})();


