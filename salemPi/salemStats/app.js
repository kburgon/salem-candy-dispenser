const express = require('express');
const app = express();
const port = 3000;
const path = require('path');
const router = express.Router();
const sql = require('sqlite3').verbose();

router.get('/', (req, res) => {
    res.sendFile('index.html', { root: __dirname + '/views' });
});

router.get('/logs', (req, res) => {
    let db = new sql.Database(__dirname + '/DB/log.db', (err) => {
        if (err) {
            return console.error(err.message);
        }

        console.log('Connected to Database');
    });

    let query = 'SELECT loggedAt FROM trigger_log;';
    db.all(query, (err, rows) => {
        if (err) {
            return console.error(err.message);
        }

        console.log('Getting results');
        var results = new Array();
        rows.forEach((row) => {
            console.log('Result: ' + row.loggedAt);
            results.push(row.loggedAt);
        });
        res.send({
            data: results
        });
    });

    db.close((err) => {
        if (err) {
            return console.error(err.message);
        }
    });
    // res.send({
    //     data: results
    // });
})

app.use('/', router);
app.use('/logs', router);
app.listen(process.env.port || port);
console.log("Running on port " + port);