document.getElementById('alignment-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting normally

    const sequence1 = document.getElementById('sequence1').value;
    const sequence2 = document.getElementById('sequence2').value;

    fetch('/align', {  // Ensure this matches the endpoint defined in app.py
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            sequence1: sequence1,
            sequence2: sequence2
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        const resultDiv = document.getElementById('result');
        resultDiv.innerHTML = `<h2>Alignment Result:</h2><pre>${data.alignment}</pre>`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
