// This file contains unit tests for the 5-payment.js file

const sinon = require('sinon');
const utils = require('./utils');
const sendPaymentRequestToAPI = require('./5-payment');

describe('sendPaymentRequestAPI', function() {
  let consoleSpy;

	beforeEach(function() {
		consoleSpy = sinon.spy(console, 'log');
	});

	afterEach(function() {
		consoleSpy.restore();
	});

	it('calls the CalculateNumber with 100 and 20', () => {
		sendPaymentRequestToAPI(100, 20);
		sinon.assert.calledOnce(consoleSpy);
		sinon.assert.calledOnceWithExactly(consoleSpy, 'The total is: 120');
	});

	it('calls the CalculateNumber with 10 and 10', () => {
		sendPaymentRequestToAPI(10, 10);
		sinon.assert.calledOnce(consoleSpy);
		sinon.assert.calledOnceWithExactly(consoleSpy, 'The total is: 20');
	});
});
