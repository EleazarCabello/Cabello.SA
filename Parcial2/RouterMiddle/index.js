const express = require('express')
const app = express();

app.get('/empleado',(req,resp)=>{
    resp.json({respuesta: "Peticion get a ruta empleado"});

})

app.post('/empleado',(req,resp)=>{
    resp.json({respuesta: "Peticion get a ruta empleado"});

})

app.put('/empleado',(req,resp)=>{
    resp.json({respuesta: "Peticion get a ruta empleado"});

})

app.delete('/empleado',(req,resp)=>{
    resp.json({respuesta: "Peticion get a ruta empleado"});

})

app.listen(8082,(req,resp)=>{
    console.log("Servidor escuchando")
})