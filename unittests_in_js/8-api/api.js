// This file contains a module that sends a payment request to the API

const express = require('express');

const app = express();
app.get('/', (req, res) => {
	res.send('Welcome to the payment system');
})
app.listen(7865, () => {
  console.log('API available on localhost port 7865');
});

module.exports = app;
