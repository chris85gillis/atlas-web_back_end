// This is a simple HTTP server that listens on port 1245 and responds with "Hello Holberton School!"


const http = require('http');

const app = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello Holberton School!');
});

app.listen(1245, () => {
    console.log('Server is listening on port 1245');
});

module.exports = app;
