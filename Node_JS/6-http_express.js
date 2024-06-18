// This file is the main entry point for the express server.


const express = require('express');

const app = express();
const PORT = 1245;

app.get('/', (req, res) => {
    res.send('Hello Holberton School!');
});

app.listen(PORT, () => {
    console.log(`Server is listening on port ${PORT}`);
});

module.exports = app;
