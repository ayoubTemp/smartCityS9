var map;
var panel;
var initialize;
var calculate;
var direction;

initialize = function(){
 
  // Correspond au coordonnées de Lille
  var latLng = new google.maps.LatLng(56.15659, 10.21353); 

  var myOptions = {
    zoom      : 14, // Zoom par défaut
    center    : latLng, // Coordonnées de départ de la carte de type latLng 
    mapTypeId : google.maps.MapTypeId.ROADMAP, // Type de carte, différentes valeurs possible HYBRID, ROADMAP, SATELLITE, TERRAIN
    maxZoom   : 20
  };

  map      = new google.maps.Map(document.getElementById('map'), myOptions);
  panel    = document.getElementById('panel');

                $.get( '/parking', function( data) {
        
        
        var eventsJson=data;
        
  for (var i = 0; i < eventsJson.length; i++) {
        
    var latLng = new google.maps.LatLng(eventsJson[i].lat,eventsJson[i].long);
  var marker = new google.maps.Marker({
    position : latLng,
    map      : map,
    title    : eventsJson[i].name
    //icon     : "marker_bordeaux.jpg" // Chemin de l'image du marqueur pour surcharger celui par défaut
  });

  var contentMarker = [
      '<div id="containerTabs">',
      '<div id="tabs">',

      '<ul>',
        '<li><a href="#tab-1"><span>'+eventsJson[i].name+'</span></a></li>',
        
      '</ul>',

      '<div id="tab-1">',
         
         '<ul>',
        '<li> adresse:'+eventsJson[i].street +'</li>',
        '<li>nombre de place: '+eventsJson[i].totalspaces+'</li>',
        '<li>nombre de place libre: '+eventsJson[i].availableSpaces+'</li>',
        '  <button onclick="javascript:calculate('+eventsJson[i].lat+','+eventsJson[i].long+')">itinéraire</button>',
      '</ul>',

      '</div>',
    
      '</div>',
      '</div>'
  ].join('');

  var infoWindow = new google.maps.InfoWindow({
    content  : contentMarker,
    position : latLng
  });
  /*
  google.maps.event.addListener(marker, 'click', function() {
    infoWindow.open(map,marker);
  });*/
  // add an event listener for this marker
bindInfoWindow(marker, map, infoWindow); 
  
  google.maps.event.addListener(infoWindow, 'domready', function(){ // infoWindow est biensûr notre info-bulle
    jQuery("#tabs").tabs();
  });
  
  
  direction = new google.maps.DirectionsRenderer({
    map   : map,
    panel : panel // Dom element pour afficher les instructions d'itinéraire
  });
}
  });
};



calculate = function(lat,long){
    //origin      = document.getElementById('origin').value; // Le point départ
    //destination = document.getElementById('destination').value; // Le point d'arrivé
    origin=new google.maps.LatLng(56.15659, 10.21353); 
    destination= new google.maps.LatLng(lat,long);
    if(origin && destination){
        var request = {
            origin      : origin,
            destination : destination,
            travelMode  : google.maps.DirectionsTravelMode.DRIVING // Mode de conduite
        }
        var directionsService = new google.maps.DirectionsService(); // Service de calcul d'itinéraire
        directionsService.route(request, function(response, status){ // Envoie de la requête pour calculer le parcours
            if(status == google.maps.DirectionsStatus.OK){
                direction.setDirections(response); // Trace l'itinéraire sur la carte et les différentes étapes du parcours
            }
        });
    }
};

initialize();
//calculate();
 
   function bindInfoWindow(marker, map, infowindow) {
    marker.addListener('click', function() {
       
        infowindow.open(map, this);
    });
} 
