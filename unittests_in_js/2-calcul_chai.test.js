/**
 * Unit tests for the calculateNumber function.
 */

const chai = require('chai');
const expect = chai.expect;
const calculateNumber = require('./2-calcul_chai.js');

describe('calculateNumber', () => {
  describe('Addition', function() {
    it('SUM two floats', function() {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });
    it('SUM one float', function() {
      expect(calculateNumber('SUM', 1.4, 4)).to.equal(5);
    });
    it('SUM one str argument', function() {
      expect(isNaN(calculateNumber('SUM', 1.4, 'b'))).to.equal(true);
    });
    it('SUM two str arguments', function() {
      expect(isNaN(calculateNumber('SUM', 'a', 'b'))).to.equal(true);
    });
    it('SUM two floats one negative', function() {
      expect(calculateNumber('SUM', 1.4, -4.5)).to.equal(-3);
    });
    it('SUM two floats two negative negative', function() {
      expect(calculateNumber('SUM', -1.4, -4.5)).to.equal(-5);
    });
  })
  describe('Subtraction', function() {
    it('SUB two floats', function() {
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });
    it('SUB one float', function() {
      expect(calculateNumber('SUBTRACT', 1.4, 4)).to.equal(-3);
    });
    it('SUB one str srg', function() {
      expect(isNaN(calculateNumber('SUBTRACT', 1.4, 'b'))).to.equal(true);
    });
    it('SUB two str args', function() {
      expect(isNaN(calculateNumber('SUBTRACT', 'a', 'b'))).to.equal(true);
    });
    it('SUB one negative', function() {
      expect(calculateNumber('SUBTRACT', -1.4, 4.5)).to.equal(-6);
    });
    it('SUB two negative', function() {
      expect(calculateNumber('SUBTRACT', -1.4, -4.5)).to.equal(3);
    });
  })
  describe('Division', function() {
    it('DIV', function() {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    it('DIV by 0', function() {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    })
    });
    it('should return Error if b is equal to 0', function() {
      expect(calculateNumber('DIVIDE', 10.3, 0).toLowerCase()).to.equal('error');
      expect(calculateNumber('DIVIDE', 10.7, 0).toLowerCase()).to.equal('error');
      expect(calculateNumber('DIVIDE', 10.3, 0.3).toLowerCase()).to.equal('error');
      expect(calculateNumber('DIVIDE', 10.7, 0.2).toLowerCase()).to.equal('error');
    });
  });
});