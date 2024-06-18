// This file exports a function `countStudents` that takes a path to a csv file as input.


const fs = require('fs');

function countStudents(path) {
    try {
        const data = fs.readFileSync(path, 'utf8');
        const lines = data.split('\n').filter(line => line.trim() !== '');
        
        if (lines.length === 0) {
            throw new Error('Cannot load the database');
        }

        const students = [];
        const fields = {};

        lines.forEach((line, index) => {
            if (index > 0) {
                const [firstname, lastname, age, field] = line.split(',');
                if (firstname && lastname && age && field) {
                    students.push({ firstname, field });
                    if (!fields[field]) {
                        fields[field] = [];
                    }
                    fields[field].push(firstname);
                }
            }
        });

        console.log(`Number of students: ${students.length}`);
        for (const field in fields) {
            if (Object.hasOwnProperty.call(fields, field)) {
                console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
            }
        }
    } catch (err) {
        throw new Error('Cannot load the database');
    }
}

module.exports = countStudents;
