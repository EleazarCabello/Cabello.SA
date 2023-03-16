const express = require('express')
const app = express();
const empleado=require('./empleado.js')

//FUNCION MIDDLEWARE
app.use(express.json())
app.use(express.text())

app.use(function(req,res,next){
    console.log(req.body.usuario);
    if(typeof req.body.usuario === "undefined"){
        
        res.status(401).json({error:"Usuario no Autorizado"})
    }else{
        if(req.body.usuario==="admin"){
            next()
        }else{
            res.status(401).json({error:"Usuario no Autorizado"})
        }
    }
    
    
})

app.use(empleado.router);

app.listen(8082,(req,resp)=>{
    console.log("Servidor escuchando")
})