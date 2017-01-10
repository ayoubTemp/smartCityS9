var map;
var panel;
var initialize;
var calculate;
var direction;

initialize = function(){
 
  // Correspond au coordonnées de Lille
  var latLng = new google.maps.LatLng(44.83225043166308, -0.5804085731506348); 

  var myOptions = {
    zoom      : 14, // Zoom par défaut
    center    : latLng, // Coordonnées de départ de la carte de type latLng 
    mapTypeId : google.maps.MapTypeId.ROADMAP, // Type de carte, différentes valeurs possible HYBRID, ROADMAP, SATELLITE, TERRAIN
    maxZoom   : 20
  };

  map      = new google.maps.Map(document.getElementById('map'), myOptions);
  panel    = document.getElementById('panel');

  var marker = new google.maps.Marker({
    position : latLng,
    map      : map,
    title    : "Bordeaux"
    //icon     : "marker_bordeaux.jpg" // Chemin de l'image du marqueur pour surcharger celui par défaut
  });

  var contentMarker = [
      '<div id="containerTabs">',
      '<div id="tabs">',

      '<ul>',
        '<li><a href="#tab-1"><span>Geographie</span></a></li>',
        '<li><a href="#tab-2"><span>Specialite</span></a></li>',
      '</ul>',

      '<div id="tab-1">',
        '<h3>Bordeaux</h3><p>Bordeaux est une commune du Sud-Ouest de la France, préfecture du département de la Gironde et chef-lieu de la région Nouvelle-Aquitaine.Capitale de l\'ancienne Guyenne, Bordeaux, située en bordure des Landes de Gascogne, fait partie de la Gascogne.En 2013, la commune est la neuvième commune de France par sa population avec 243 626 habitants, mais son agglomération est classée septième avec 876 714 habitants1. L\'aire urbaine de Bordeaux compte quant à elle 1 178 335 habitants en 20132, ce qui en fait la cinquième aire urbaine de France après celles de Paris, Lyon, Marseille - Aix et Toulouse et devant Lille, Nice et Nantes. Bordeaux est par ailleurs la principale commune de la métropole « Bordeaux Métropole », qui rassemble 28 communes et 737 492 habitants .</p>',
      '</div>',
      '<div id="tab-2">',
       '<h3>Bordeaux</h3><p>La ville est connue dans le monde entier pour les vins de Bordeaux et les vignobles du Bordelais, surtout depuis le XVIIIe siècle, qui fut un véritable âge d\'or. En 1957, Bordeaux est récompensée du prix de l\'Europe, conjointement avec Turin. En juin 2007, une partie de la ville, le port de la Lune, est inscrite par le Comité du patrimoine mondial, désigné par l\'assemblée générale de l’UNESCO, sur la Liste du patrimoine mondial.</p>',
      '</div>',

      '</div>',
      '</div>'
  ].join('');

  var infoWindow = new google.maps.InfoWindow({
    content  : contentMarker,
    position : latLng
  });
  
  google.maps.event.addListener(marker, 'click', function() {
    infoWindow.open(map,marker);
  });
  
  google.maps.event.addListener(infoWindow, 'domready', function(){ // infoWindow est biensûr notre info-bulle
    jQuery("#tabs").tabs();
  });
  
  
  direction = new google.maps.DirectionsRenderer({
    map   : map,
    panel : panel // Dom element pour afficher les instructions d'itinéraire
  });

};



calculate = function(){
    //origin      = document.getElementById('origin').value; // Le point départ
    //destination = document.getElementById('destination').value; // Le point d'arrivé
    origin="Bordeaux"
    destination="toulouse"
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
calculate();
