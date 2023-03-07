const express = require('express')
const app = express();
const empleado=require('./empleado.js')

app.use(empleado.router);

app.listen(8082,(req,resp)=>{
    console.log("Servidor escuchando")
})