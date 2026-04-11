const fs = require('fs');

function countStudents(path) {
    return new Promise((resolve, reject) => {
        fs.readFile(path, 'utf8', (error, data) => {
            if (error) {
                reject(Error('Cannot load the database'));
                return;
            }

            const lines = data.split('\n');
            const students = lines.filter(line => line.trim() !== '');
            
            // إزالة رأس الجدول
            students.shift();
            
            const numberOfStudents = students.length;
            console.log(`Number of students: ${numberOfStudents}`);
            
            const fields = {};
            
            for (const student of students) {
                const studentData = student.split(',');
                const firstName = studentData[0];
                const field = studentData[3];
                
                if (!fields[field]) {
                    fields[field] = [];
                }
                fields[field].push(firstName);
            }
            
            for (const field in fields) {
                if (fields.hasOwnProperty(field)) {
                    const names = fields[field];
                    console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
                }
            }
            
            resolve();
        });
    });
}

module.exports = countStudents;
