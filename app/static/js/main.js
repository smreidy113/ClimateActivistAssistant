document.getElementById('userForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const userInput = document.getElementById('userInput').value;
    const response = await fetch('/api/data', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({input: userInput})
    });
    const data = await response.json();
    document.getElementById('result').innerText = JSON.stringify(data, null, 2);
});
