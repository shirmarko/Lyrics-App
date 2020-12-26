var mymap;
var data=[];
var markers=[];
var counter = 0;
function init_map() {
    mymap = L.map('mapid').setView([51.505, -0.09], 4);
    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoieXV2YWxoZXIiLCJhIjoiY2s5bGU2eGdwMDNreTNrcnR3ZWt6MDFxMiJ9.2jCmAPMv8fglHt-5kf-sGg', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1,
        accessToken: 'your.mapbox.access.token'
    }).addTo(mymap);
}

//add places to the map
function add_markers() {
    const Http = new XMLHttpRequest();
    const artist = document.getElementById('artist-name').value;
    const k = document.getElementById('k').value;

    //input checking
    if(artist === ""){
        alert("You forgot to insert artist. Try again");
        return;
    }
    if(k>5 || k<=0){
        alert("You have to chose number of songs between 1 to 5. Try again");
        return;
    }

    var url = 'http://localhost:5000/places?artist='+artist+'&k='+k; 
    Http.open("GET", url);
    Http.send(); //server request
    Http.onreadystatechange = (e) => {
        console.log(Http.respones)
        data= JSON.parse(Http.response);
        if(data.length === 0)
            alert('We coldn\'t find any location, try another artist.') 
        // places found- put them on map
        for (var i = 0; i < data.length; i++) {
            var place = data[i].name+"\n";
            var songs="";
            var songs_link="";
            link="";
            for(var j=0 ; j<data[i].songs.length; j++){
                link=data[i].songs[j].url;
                songs_link += `</b><a href=${link} target="_blank">${data[i].songs[j].song} - ${data[i].songs[j].artist}</a>\n`
            }
            var popup_content= "<b>"+place+" - </b>"+songs_link;
            var icon = chooseIcon();
            markers.push(L.marker([data[i].latitude,data[i].longitude],{icon: icon})
                .addTo(mymap)
                .bindPopup(popup_content).openPopup());
        }
        counter++;
    }
}

document.documentMode = undefined;~~

function ClearMap() {
    data = [];
    for(var i = 0; i < this.markers.length; i++){
        this.mymap.removeLayer(this.markers[i]);
    }
}

function chooseIcon() {
    var colors = [blueIcon, greenIcon , goldIcon, redIcon, violetIcon, orangeIcon, greyIcon, blackIcon, yellowIcon];
    return colors[counter % colors.length];
}
