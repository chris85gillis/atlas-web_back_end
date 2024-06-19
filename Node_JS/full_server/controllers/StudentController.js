// This file is the controller for the /students endpoint and handles HTTP requests related to students.


import { readDatabase } from '../utils';

class StudentsController {
    static async getAllStudents(req, res) {
        try {
            const { path: filePath } = req;
            const fields = await readDatabase(filePath);
            let response = 'This is the list of our students\n';
            const fieldNames = Object.keys(fields).sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));

            fieldNames.forEach(field => {
                response += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`;
            });

            res.status(200).send(response);
        } catch (error) {
            res.status(500).send('Cannot load the database');
        }
    }

    static async getAllStudentsByMajor(req, res) {
        const { major } = req.params;

        if (major !== 'CS' && major !== 'SWE') {
            res.status(500).send('Major parameter must be CS or SWE');
            return;
        }

        try {
            const { path: filePath } = req;
            const fields = await readDatabase(filePath);
            const students = fields[major] || [];
            const response = `List: ${students.join(', ')}`;

            res.status(200).send(response);
        } catch (error) {
            res.status(500).send('Cannot load the database');
        }
    }
}

export default StudentsController;
