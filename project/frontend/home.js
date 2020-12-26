function create_wordCloud(event) {
    const Http = new XMLHttpRequest();
    const artist = document.getElementById('artist').value;
    const k = document.getElementById('k').value ;
    //input checking
    if(artist === ""){
        alert("You forgot to insert artist. Try again");
        return;
    }
    if(k>5 || k<=0){
        alert("You have to chose number of songs between 1 to 5. Try again");
        return;
    }
    // server request 
    fetch('http://localhost:5000/wordsCloud?artist='+artist+'&k='+k, {
        method: "GET",
        headers: { "Content-Type": "application/json" }
    }).then(async (res) => {
        console.log("wordCloud: "+res.status);
        if( res.status == 200){
            window.location.replace("wordCloud.html");
        }
        else{ //internal error
            alert("There is a problem, try later.");
        }

        
    })
}

function create_statistics(event) {
    const Http = new XMLHttpRequest();
    const artist = document.getElementById('artist2').value;
    //input checking
    if(artist === ""){
        alert("You forgot to insert artist. Try again");
        return;
    }
    // server request 
    fetch('http://localhost:5000/wordsStatistics?artist='+artist, {
        method: "GET",
        headers: { "Content-Type": "application/json" }
    }).then(async (res) => {
        console.log("statistics: "+res.status);
        if( res.status == 200){
            window.location.replace("statistics.html", res.body);
        }
        else{ //internal error
            alert("There is a problem, try later.");
        }
  
    })
}



