/**
 * Created by ayoub on 31/10/16.
 */
/**
 * Created by ayoub on 13/04/16.
 */
var express = require('express');



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

app.set('port', (process.env.PORT || 8082));

app.listen(app.get('port'), function() {
    console.log('Node app is running on port', app.get('port'));
});
