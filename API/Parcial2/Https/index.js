const express = require('express');
const https = require('https');
const fs = require('fs');
const path = require('path');
const { Console } = require('console');

let app=express();

app.get('/',function(req,res){
    res.send("Servidor express contestando a get");
})

let opciones = {
    key: fs.readFileSync(path.join(__dirname,'/ssl/key.pem')),
    cert: fs.readFileSync(path.join(__dirname,'./ssl/cert.pem'))
}

https.createServer(opciones,app).listen(8082,function(){
    console.log("Servidor express funcionanado")
})

