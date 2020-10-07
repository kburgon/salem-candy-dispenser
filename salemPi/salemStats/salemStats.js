const express = require('express')
const app = express()

app.get('/', function (req, res) {
  res.render('index')
})

app.listen(8888, function () {
  console.log('Example app listening on port 8888!')
})