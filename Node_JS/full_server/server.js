// This file is the entry point for the server.


import express from 'express';
import router from './routes/index';

const app = express();
const PORT = 1245;

app.use((req, res, next) => {
    req.path = process.argv[2];
    next();
});

app.use('/', router);

app.listen(PORT, () => {
    console.log(`Server is listening on port ${PORT}`);
});

export default app;
