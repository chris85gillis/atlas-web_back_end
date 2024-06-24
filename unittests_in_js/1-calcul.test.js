/**
 * Unit tests for the calculateNumber function.
 */

const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function() {
  describe('SUM', function() {
    it('should return 6 when inputs are 1.4 and 4.5', function() {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });

    it('should return 0 when inputs are -1.4 and 1.4', function() {
      assert.strictEqual(calculateNumber('SUM', -1.4, 1.4), 0);
    });
  });

  describe('SUBTRACT', function() {
    it('should return -4 when inputs are 1.4 and 4.5', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });

    it('should return 4 when inputs are 5.7 and 2.4', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', 5.7, 2.4), 4);
    });
  });

  describe('DIVIDE', function() {
    it('should return 0.2 when inputs are 1.4 and 4.5', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });

    it('should return "Error" when dividing by 0', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });

    it('should return "Error" when rounded b is 0', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0.4), 'Error');
    });
  });

  it('should throw an error for invalid operation type', function() {
    assert.throws(() => calculateNumber('MULTIPLY', 1.4, 4.5), /Invalid operation type/);
  });
});
