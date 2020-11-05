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

    let query = 'SELECT DISTINCT DATE(loggedAt) AS Date, COUNT(id) AS Logs FROM trigger_log GROUP BY DATE(loggedAt);';
    db.all(query, (err, rows) => {
        if (err) {
            return console.error(err.message);
        }

        console.log('Getting results');
        var results = new Array();
        rows.forEach((row) => {
            console.log('Result: ' + row.Date);
            results.push({
                date: row.Date,
                logs: row.Logs
            });
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
})

app.use('/', router);
app.use('/logs', router);
app.listen(process.env.port || port);
console.log("Running on port " + port);