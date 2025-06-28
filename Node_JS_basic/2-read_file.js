function  countStudents (path) {
    try {
        const fs = require('fs');
        const data = fs.readFile
            (path, 'utf8', (err, content) => {
                if (err) {
                    console.error('Cannot load the database');
                    return;
                }
                const lines = content.split('\n').filter(line => line.trim() !== '');
                const students = lines.slice(1).map(line => line.split(','));
                const studentCount = students.length;
                console.log(`Number of students: ${studentCount}`);
                
                const fields = {};
                students.forEach(student => {
                    const field = student[3];
                    if (!fields[field]) {
                        fields[field] = [];
                    }
                    fields[field].push(student[0]);
                });
                
                for (const [field, names] of Object.entries(fields)) {
                    console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
                }
            });
}