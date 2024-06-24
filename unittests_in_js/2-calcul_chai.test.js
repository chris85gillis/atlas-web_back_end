/**
 * Unit tests for the calculateNumber function.
 */


const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', function() {
  describe('SUM', function() {
    it('should return 6 when inputs are 1.4 and 4.5', function() {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });

    it('should return 0 when inputs are -1.4 and 1.4', function() {
      expect(calculateNumber('SUM', -1.4, 1.4)).to.equal(0);
    });
  });

  describe('SUBTRACT', function() {
    it('should return -4 when inputs are 1.4 and 4.5', function() {
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });

    it('should return 4 when inputs are 5.7 and 2.4', function() {
      expect(calculateNumber('SUBTRACT', 5.7, 2.4)).to.equal(4);
    });
  });

  describe('DIVIDE', function() {
    it('should return 0.2 when inputs are 1.4 and 4.5', function() {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });

    it('should return "Error" when dividing by 0', function() {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });

    it('should return "Error" when rounded b is 0', function() {
      expect(calculateNumber('DIVIDE', 1.4, 0.4)).to.equal('Error');
    });
  });

  it('should throw an error for invalid operation type', function() {
    expect(() => calculateNumber('MULTIPLY', 1.4, 4.5)).to.throw('Invalid operation type');
  });
});
