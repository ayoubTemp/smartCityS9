 var request = require('request'); 
var fs=require('fs');
var http=require('http');
var https=require('https');

    var urlSF='http://api.sfpark.org/sfpark/rest/availabilityservice?lat=37.7749&long=-122.4194&radius=50&uom=mile&response=json'; 
    var urlChicago='https://api.parkwhiz.com/search/?lat=41.8781&lng=-87.6298&key=62d882d8cfe5680004fa849286b6ce20';	
  

 
 var options2 = {
  hostname: 'api.parkwhiz.com'
  ,port: 443
  , path: '/search/?lat=41.8781&lng=-87.6298&key=62d882d8cfe5680004fa849286b6ce20'
  ,method: 'GET'
  ,headers: { 'Content-Type': 'application/json' }
};
 var options1 = {
  hostname: 'api.sfpark.org'
  ,port: 80
  , path: '/sfpark/rest/availabilityservice?lat=37.7749&long=-122.4194&radius=50&uom=mile&response=json'
  ,method: 'GET'
  ,headers: { 'Content-Type': 'application/json' }
};
setInterval(function(){
var req = http.request(options1, function(res) {
  res.setEncoding('utf8');

var buffer=",";
  res.on('data', function (chunck) {
      // console.log(data); // I can't parse it because, it's a string. why?
    buffer+=chunck;
 
});
req.on('error', function(e) {
  console.log('problem with request: ' + e.message);
});
 res.on("end", function (err) {
fs.appendFile('SF',buffer, function (err) {

            if (err) throw err;

            console.log('It\'s saved! in the app folder');

        });

	})
})
req.end();

var req2 = https.request(options2, function(res) {
  res.setEncoding('utf8');

var buffer=",";
  res.on('data', function (chunck) {
      // console.log(data); // I can't parse it because, it's a string. why?
    buffer+=chunck;
 
});
req2.on('error', function(e) {
  console.log('problem with request: ' + e.message);
});
 res.on("end", function (err) {
fs.appendFile('CH',buffer, function (err) {

            if (err) throw err;

            console.log('It\'s saved! in the app folder');

        });

	})
})
req2.end();
}, 300000)

 /* request.post({
      
        url:    urlSF 
    }, function(error, response, data){
        console.log(data); // I can't parse it because, it's a string. why?
      // console.log(response); // I can't parse it because, it's a string. why?
   
//        fs.writeFile(targetWebSite+" key words",util.inspect(slicedWordList), function (err) {
        fs.writeFile('SF',data, function (err) {

            if (err) throw err;

            console.log('It\'s saved! in the app folder');

        });
 
}) */
 
//setInterval(fn,time)
