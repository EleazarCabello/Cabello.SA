const express = require('express');
const mysql = require('mysql2/promise')
const app = express();

app.use(express.json())
app.use(express.text())

app.get('/id/',async(req,res)=>{
  const connection = await mysql.createConnection({host:'localhost', user: 'root', database: 'world'});
  const [rows, fields] = await connection.execute('SELECT * FROM mundo');

  res.json(rows);
})

app.get('/id/:id',async(req,res)=>{

    const connection = await mysql.createConnection({host:'localhost', user: 'root', database: 'world'});
    const [rows, fields] = await connection.execute('SELECT * FROM mundo WHERE id = ?',[req.params.id]);

    if(rows.length == 0){
        res.json({registros:"No se encontro usuario"});
    }else{
        res.json(rows);
    }
  
})


app.use((req,res)=>{
    res.status(404).json({estado:"Pagina no encontrada"})
})

app.listen(8082,()=>{
    console.log("Servidor Express corriendo y escuchando en el puerto 8082")
})