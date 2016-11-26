/**
 * Created by ayoub on 31/10/16.
 */

var express = require('express');
var EventSearch = require("facebook-events-by-location-core");
var request = require('request');
var cheerio = require('cheerio');

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
app.get('/eventFormHandler',function(req, res){
     
    res.render('eventSubmitter.html');
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

//get the most used words  on the website
app.get('/getWordList', function(req, res){

//it was so complicated to parse the web site since there are ads
// and html tags and for now this solution is much better
//note to self:u found a way to save the day but yi have to do
    //it on ur free time
    var url=req.query['url'];
   // var numberOfKeyWords=parseInt(req.query['numberOfKeyWords']);
   // console.log(numberOfKeyWords)


    request.post({
        headers: {'content-type' : 'application/x-www-form-urlencoded'},
        url:     'http://www.seowebpageanalyzer.com/',
        body:    "url="+url
    }, function(error, response, html){
        var wordList=[]
        var $ = cheerio.load(html);
        var table= $('table').first();
        // console.log(table);
        ///  var tb=[1,2,3,3,3];
        table.find("tr").each( function (i,element) {
            var children = $(this).children();
            var row = {
                "keyword" : $(children[0]).text(),
                "frequency" : $(children[1]).text()
            };

            wordList.push(row);
            // console.log(i)
        });
        //send ony the number required by the user
        /*var slicedWordList=wordList.slice(0, numberOfKeyWords+1);
        pathArray = url.split( '/' );
        targetWebSite = pathArray[2];
//        fs.writeFile(targetWebSite+" key words",util.inspect(slicedWordList), function (err) {
        fs.writeFile(targetWebSite+" key words",JSON.stringify(slicedWordList), function (err) {

            if (err) throw err;

            console.log('It\'s saved! in the app folder');

        });*/
        res.json(wordList);
//console.log(wordList);



    });





});


app.set('port', (process.env.PORT || 8082));

app.listen(app.get('port'), function() {
    console.log('Node app is running on port', app.get('port'));
});
