export const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title: 'React POST Request Example' })
};
fetch('http://127.0.0.1:5000/api/posts', requestOptions)
    .then(response => response.json())
    .then(data => { });