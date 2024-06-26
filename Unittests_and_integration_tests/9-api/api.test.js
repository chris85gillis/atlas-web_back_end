// test the API

const request = require('request');
const { expect } = require('chai');

describe('Index page', () => {
    it('returns status 200', (done) => {
      request('http://localhost:7865', (err, res) => {
        expect(res.statusCode).to.equal(200);
        done();
      });
    });
  
    it('returns correct result', (done) => {
      request('http://localhost:7865', (err, res, body) => {
        expect(body).to.equal('Welcome to the payment system');
        done();
      });
    });
});
describe('Cart Page', () => {
  it('Correct status code when id is provided and is a number', (done) => {
    request('http://localhost:7865/cart/12', (err, res) => {
      expect(res.statusCode).to.equal(200);
      done();
    });
  });
  it('Correct message when id is a number', (done) => {
    request('http://localhost:7865/cart/12', (err, res, body) => {
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });
  it('Correct status code when id is not a number', (done) => {
    request('http://localhost:7865/cart/ab', (err, res) => {
      expect(res.statusCode).to.equal(404);
      done();
    });
  });
  it('Correct status code when id is not provided', (done) => {
    request('http://localhost:7865/cart/', (err, res) => {
      expect(res.statusCode).to.equal(404);
      done();
    });
  });
});
