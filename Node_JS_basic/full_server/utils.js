import fs from 'fs';

const readDatabase = (path) => new Promise((resolve, reject) => {
  fs.readFile(path, 'utf8', (error, fileContent) => {
    if (error) {
      reject(error);
      return;
    }

    const lines = fileContent.split('\n').filter((line) => line.trim() !== '');
    const students = lines.slice(1);
    const studentsByField = {};

    students.forEach((student) => {
      const [firstname, , , field] = student.split(',');

      if (!studentsByField[field]) {
        studentsByField[field] = [];
      }

      studentsByField[field].push(firstname);
    });

    resolve(studentsByField);
  });
});

export default readDatabase;
