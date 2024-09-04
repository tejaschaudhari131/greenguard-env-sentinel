let map;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: 40.7128, lng: -74.0060 },
        zoom: 8,
    });
}

// Handling pollution detection event
document.getElementById('detect-pollution').addEventListener('click', async function() {
    const imageFile = document.getElementById('satellite-image').files[0];
    if (!imageFile) {
        alert('Please upload a satellite image.');
        return;
    }

    const base64String = await getBase64(imageFile);

    // Send the image data to the backend for pollution detection
    const response = await fetch('/api/detect_pollution', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ image_data: base64String.split(',')[1] }),
    });

    const result = await response.json();
    if (result.error) {
        document.getElementById('pollution-result').innerText = `Error: ${result.error}`;
    } else {
        document.getElementById('pollution-result').innerText = `Pollution Level: ${result.pollution_level.toFixed(2)}`;
    }
});

// Function to convert image to base64
function getBase64(file) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onload = () => resolve(reader.result);
        reader.onerror = error => reject(error);
        reader.readAsDataURL(file);
    });
}
