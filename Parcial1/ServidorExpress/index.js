const express = require('express');
const cors = require('cors');
const app = express();
const morgan = require('morgan');
const fs = require('fs')
const path = require('path')



app.use(express.json())
app.use(express.text())
app.use(cors())
app.use(morgan('tiny'))




var accessLogStream = fs.createWriteStream(path.join(__dirname, 'access.log'), { flags: 'a' })
app.use(morgan('combined', { stream: accessLogStream }))



app.get('/alumnos/:carrera',(req,res)=>{
    //console.log(req.params.carrera)
    res.jsonp({alumnos:"Alumnos de la carrera de "+req.params.carrera})
    //res.json({alumnos:"Alumnos de la carrera de "+req.params.carrera})
})

app.get('/maestros',(req,res)=>{
     //console.log(req.params.control)
    res.json({maestro:"Informacion de maestro "+req.query.control})
})

app.get('/administrativos',(req,res)=>{
    //console.log(req.body.nombre)
   res.json({admin:"Informacion personal administrativos "+req.body.nombre})
})

app.use((req,res)=>{
    res.status(404).json({estado:"Pagina no encontrada"})
})

app.listen(8082,()=>{
    console.log("Servidor Express corriendo y escuchando en el puerto 8082")
})