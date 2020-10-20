const express = require('express');
const app = express();
const port = 3000;
const path = require('path');
const router = express.Router();

router.get('/', (req, res) => {
    res.sendFile('index.html', { root: __dirname + '/views' });
});

app.use('/', router);
app.listen(process.env.port || port);
console.log("Running on port " + port);