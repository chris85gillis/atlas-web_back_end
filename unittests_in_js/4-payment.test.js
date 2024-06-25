// This file contains unit tests for the 4-payment.js file

const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestAPI', function() {
	let calculateNumStub;
	let consoleSpy;

	beforeEach(function() {
		calculateNumStub = sinon.stub(Utils, 'calculateNumber').returns(10);
		consoleSpy = sinon.spy(console, 'log');
	});

  afterEach(function() {
    calculateNumStub.restore();
		consoleSpy.restore();
  });

  it('calls the CalculateNumber with correct args SUM whole', () => {
		sendPaymentRequestToApi(100, 20);
		sinon.assert.calledOnce(calculateNumStub);
		sinon.assert.calledOnceWithExactly(calculateNumStub, 'SUM', 100, 20);
	});

	it('Displays the console message', () => {
		sendPaymentRequestToApi(100, 20);
		sinon.assert.calledOnce(consoleSpy);
		sinon.assert.calledOnceWithExactly(consoleSpy, 'The total is: 10');
	});
});
