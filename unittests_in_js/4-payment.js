// This module sends a payment request to the API

const Utils = require('./utils');

function sendPaymentRequestToApi(totalAmount, totalShipping) {
	const result = Utils.calculateNumber('SUM', totalAmount, totalShipping);
	console.log(`The total is: ${result}`);
}

module.exports = sendPaymentRequestToApi;