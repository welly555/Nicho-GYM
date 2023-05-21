setTimeout(function(){ 
    var msg = document.getElementsByClassName("message");
    while(msg.length > 0){
        msg[0].parentNode.removeChild(msg[0]);
    }
}, 5000);