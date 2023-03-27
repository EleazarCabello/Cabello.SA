const express = require('express')
const jsonwebtoken = require('jsonwebtoken')

let app=express();
app.use(express.json());

app.post('/login',function(req,res,next){
    console.log(req.body)
var token = jsonwebtoken.sign(req.body, 'claveSecreta');
console.log(token)
    res.json({token:token})
})

app.get('/sistema',verificarToken,function(req,res,next){
    res.json({Mensaje:"Acceso concedido a ruta sistema"})
})

app.listen(8083,function(){
    console.log('Servidor express escuchando en puerto 8083')
})

function verificarToken(req,res,next){
    
    let token = req.headers.authorization.substring(7,req.headers.authorization.length)
    
    jsonwebtoken.verify(token, 'claveSecreta',function(err,decoded){
        if(err){
            res.json({Error:"Acceso no concedido"})
        }else{
            next();
        }
    })
}