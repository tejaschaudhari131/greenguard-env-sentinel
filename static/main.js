let map;

// Initialize the Google Map
function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: -34.397, lng: 150.644 },
        zoom: 8,
    });
}

// Event listener for detecting pollution
document.getElementById('detect-pollution').addEventListener('click', function() {
    const imageFile = document.getElementById('satellite-image').files[0];
    
    if (!imageFile) {
        alert('Please upload a satellite image.');
        return;
    }

    // Convert the image to a base64 string to send to the backend
    const reader = new FileReader();
    reader.onloadend = function() {
        const base64String = reader.result.split(',')[1];
        
        fetch('/detect_pollution', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ image_data: base64String }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById('pollution-result').innerText = `Error: ${data.error}`;
            } else {
                document.getElementById('pollution-result').innerText = `Pollution Level: ${data.pollution_level}`;
            }
        });
    };
    
    reader.readAsDataURL(imageFile);
});
