// utils.js

const Utils = {
	calculateNumber(type, a, b) {
	  const round = num => Math.round(num);
  
		switch (type) {
		  case 'SUM':
			return round(a) + round(b);
		  case 'SUBTRACT':
			return round(a) - round(b);
		  case 'DIVIDE':
			const roundB = round(b);
			if (roundB === 0) {
			  return 'Error';
			}
			return round(a) / roundB;
		  default:
			throw new Error('Invalid type');
		}
	  }
  }
  
  module.exports = Utils;