//Utility functions for the application.


import fs from 'fs';

export function readDatabase(filePath) {
    return new Promise((resolve, reject) => {
        fs.readFile(filePath, 'utf8', (err, data) => {
            if (err) {
                reject(new Error('Cannot load the database'));
                return;
            }

            const lines = data.split('\n').filter(line => line.trim() !== '');
            const fields = {};

            lines.forEach((line, index) => {
                if (index > 0) {
                    const [firstname, lastname, age, field] = line.split(',');
                    if (firstname && lastname && age && field) {
                        if (!fields[field]) {
                            fields[field] = [];
                        }
                        fields[field].push(firstname);
                    }
                }
            });

            resolve(fields);
        });
    });
}
