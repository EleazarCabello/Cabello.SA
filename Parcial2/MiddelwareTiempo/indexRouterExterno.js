const express = require('express')
const app = express();
const empleado=require('./empleado.js')

//FUNCION MIDDLEWARE
app.use(express.json())
app.use(express.text())


app.use(function(req,res,next){
let fecha = new Date();

let Ejemplo = fecha.getHours();
console.log(Ejemplo);

if(fecha > '7:00' && fecha < '21:00' ){
    next()
}else{
    res.status(401).json({error:"El servidor solo esta abierto de 7:00 a 21:00."})
}

})

app.use(empleado.router);

app.listen(8082,(req,resp)=>{
    console.log("Servidor escuchando")
})