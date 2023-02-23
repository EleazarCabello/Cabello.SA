// get the client
const mysql = require('mysql2');
var json2xls = require('json2xls');
const fs = require('fs');
const path = require('path');

// create the connection to database
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  database: 'test'
});

// simple query
connection.query(
  'SELECT * FROM `table` WHERE `name` = "Page" AND `age` > 45',
  function(err, results, fields) {
    if(err){
        console.table("Ocurrio un error"+err.sqlMessage);
    }else{
        console.log(results); // results contains rows returned by server

        var xls = json2xls(results);
        fs.writeFileSync(path.join(__dirname,'data.xlsx'), xls, 'binary');
    }
  }
);

connection.end();