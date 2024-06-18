// This is a simple express server that listens on port 1245


const express = require('express');
const app = express();
const readFileAsync = require('./3-read_file_async');

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  readFileAsync(req.query.db)
    .then(data => res.send(`This is the list of our students${data}`))
    .catch(err => console.error(err));
});

app.listen(1245, () => console.log('Server listening on port 1245!'));

module.exports = app;
