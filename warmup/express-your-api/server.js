const express = require('express');
const fs = require('fs');

const app = express();

const contents = fs.readFileSync('./iHasFlagses.txt').toString().split('\n');

app.get('/', function (req, res) {
    const index = (Math.random() * contents.length) | 0;
    return res.send(contents[index]);
});

app.listen(process.env.PORT || 80);