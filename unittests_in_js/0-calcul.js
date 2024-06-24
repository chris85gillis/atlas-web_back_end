// This module exports a function that calculates the sum of two integers
// and returns the result rounded to the nearest integer.


function calculateNumber(a, b) {
	const roundedA = Math.round(a);
	const roundedB = Math.round(b);
	const sum = roundedA + roundedB;
	
	// Convert -0 to 0
	return sum === 0 ? 0 : sum;
  }
  
  module.exports = calculateNumber;
  