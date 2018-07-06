const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const mysql = require('mysql');
 
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
    extended: true
}));
 
// connection configurations
const mc = mysql.createConnection({
    host: 'bidfta-prod.cac4i5blias7.us-east-1.rds.amazonaws.com',
    user: 'upwork',
    password: 'mCwcr6UzcF5xw1I',
    database: 'products'
});
 
// connect to database
mc.connect();
 
// default route
app.get('/', function (req, res) {
    return res.send({ error: true, message: 'hello' })
});
 
// Retrieve all todos 
app.get('/all', function (req, res) {
    mc.query('SELECT * FROM Products5', function (error, results, fields) {
        if (error) throw error;
        return res.send({ error: false, data: results, message: 'All list.' });
    });
});
 
// Search for todos with ‘bug’ in their name
app.get('/all/search/:keyword/', function (req, res) {
    let field = req.params.keyword;
    console.log("Field is ", field);
    mc.query("SELECT * FROM Products5  WHERE UPC=?", field , function (error, results, fields) {
        if (error) throw error;
        return res.send({ error: false, data: results, message: 'Todos search list.' });
    });
});
 
// Retrieve todo with id 
app.get('/all/:ASIN', function (req, res) {
 
    let ASIN = req.params.ASIN;
 
    mc.query('SELECT * FROM Products5 where ASIN=?', ASIN, function (error, results, fields) {
        if (error) throw error;
        return res.send({ error: false, data: results[0], message: 'Todos list.' });
    });
 
});
 
// Add a new todo  
app.post('/todo', function (req, res) {
 
    let task = req.body.task;
    let data = req.body
    console.log("Data is", data)
    if (!data) { 
        return res.status(400).send({ error:true, message: 'Please provide task' });
    }
 
    mc.query("INSERT INTO Products5 SET ? ", data, function (error, results, fields) {
        if (error) throw error;
        return res.send({ error: false, data: results, message: 'New task has been created successfully.' });
    });
});
 
//  Update todo with id
app.put('/todo', function (req, res) {
 
    let task_id = req.body.task_id;
    let task = req.body.value;
    let column = req.body.column 
    if (!task_id || !task) {
        return res.status(400).send({ error: task, message: 'Please provide task and task_id' });
    }
 
    mc.query("UPDATE Products5 SET " + column + " = ? WHERE ASIN = ?", [task, task_id], function (error, results, fields) {
        if (error) throw error;
        return res.send({ error: false, data: results, message: 'Task has been updated successfully.' });
    });
});
 
//  Delete todo
app.delete('/todo/:id', function (req, res) {
 
    let task_id = req.params.id;
 
    mc.query('DELETE FROM Products5 WHERE ASIN = ?', [task_id], function (error, results, fields) {
        if (error) throw error;
        return res.send({ error: false, data: results, message: 'Task has been updated successfully.' });
    });
 
});
 
// all other requests redirect to 404
app.all("*", function (req, res, next) {
    return res.send('page not found');
    next();
});
 
// port must be set to 8080 because incoming http requests are routed from port 80 to port 8080
app.listen(8080, function () {
    console.log('Node app is running on port 8080');
});
 
// allows "grunt dev" to create a development server with livereload
module.exports = app;

