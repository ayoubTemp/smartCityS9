/**
 * Created by ayoub on 31/10/16.
 */
/**
 * Created by ayoub on 13/04/16.
 */
var express = require('express');
var EventSearch = require("facebook-events-by-location-core");


var app     = express();
app.use(express.static(__dirname + '/views'));
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'html');
app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});

app.get('/',function(req, res){
    res.render('service.html');
});
app.get('/eventfullCity',function(req, res){
    res.render('events.html')
});
app.get("/events",  function(req, res) {
   ///check if the user specified the coordinates
    if (!req.query.lat || !req.query.lng) {
        res.status(500).json({message: "Please specify the lat and lng parameters!"});

    }else {
        var options = {};
        options.lat=req.query.lat;
        options.lng=req.query.lng;
        options.distance=req.query.distance;
        options.query=req.query.query;
        options.since=req.query.starts;
        options.until=req.query.ends;
        //select the fields we want in our response
      /*
      options.fields="name,type,description,startTime,endTime,venue";
      //note to self:u betteer edit the node module or rewrite it urself
      //this way u'll fix the problems u noticed with the original node module
       */
       //it's a bad idea to put it here but it' temporary
        //note to self:put all your keys in env variables
        options.accessToken="1725944747730254|f70f4cbc49a91a92a4350b022cca2858";
        //now that everything is set ,we call the eventSearch moduke
        eventsLookup=new EventSearch(options);
        // Search and handle results
        eventsLookup.search().then(function (events) {
            res.json(events);
        }).catch(function (error) {
            res.status(500).json(error);
        });
    }
});
app.set('port', (process.env.PORT || 8082));

app.listen(app.get('port'), function() {
    console.log('Node app is running on port', app.get('port'));
});
