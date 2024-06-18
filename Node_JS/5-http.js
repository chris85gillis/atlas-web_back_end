// This is a simple HTTP server that responds to two URLs


const http = require('http');

const countStudents = require('./3-read_file_async');

const dbName = process.argv.slice(2)[0];
const PORT = 1245;

const app = http.createServer(async (req, res) => {
  const { url } = req;

  res.writeHead(200, { 'Content-Type': 'text/plain' });

  if (url === '/') {
    res.write('Hello Holberton School!');
    res.end();
  } else if (url === '/students') {
    res.write('This is the list of our students\n');
    try {
      const text = await countStudents(dbName);
      text.forEach((line, index) => {
        res.write(line);
        if (index < text.length - 1) {
          res.write('\n');
        }
      });
      res.end();
    } catch (error) {
      res.end(error.message);
    }
  }
  res.statusCode = 404;
  res.end();
});

app.listen(PORT, () => {});

module.export = app;
