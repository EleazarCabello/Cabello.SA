const express = require('express')
const app = express();
const router = express.Router();

router.get('/empleado',(req,resp)=>{
    resp.status(200).json({respuesta: "Peticion get a ruta empleado"});

    }).post('/empleado',(req,resp)=>{
        resp.status(200).json({respuesta: "Peticion post a ruta empleado"});

    }).put('/empleado',(req,resp)=>{
        resp.status(200).json({respuesta: "Peticion put a ruta empleado"});

    }).delete('/empleado',(req,resp)=>{
        resp.status(200).json({respuesta: "Peticion delete a ruta empleado"});

})

app.use(router);

app.listen(8082,(req,resp)=>{
    console.log("Servidor escuchando")
})