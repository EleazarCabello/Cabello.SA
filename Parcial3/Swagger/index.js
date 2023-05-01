const express = require('express');
const mysql = require('mysql2/promise')
const app = express();
const cors = require('cors')
const swaggerUI = require('swagger-ui-express');
const swaggerJsDoc = require('swagger-jsdoc');
const path = require('path');


app.use(express.json())
app.use(express.text())
app.use(cors())

const swaggerOptions = {
    definition: {
    openapi: '3.0.0',
    info: {
    title: 'API Usuarios',
    version: '1.0.0',
    },
    servers:[
    {url: "http://localhost:8082"}
    ], 
    },
    apis: [`${path.join(__dirname,"./index.js")}`],
    };
   

    /**
 * @swagger
 * /usuarios:
 *  get:
 *      description: peticion get a la ruta de usuarios!
 *  responses:
 *      200:
 *          description: regresa un json con todos los usuarios.
 */
app.get('/usuario',async(req,res)=>{
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

app.post('/id',async(req,res)=>{
    let sentenciaSql = `insert into mundo values(${req.body.Id},'${req.body.Usuario}','${req.body.Edad}')`;
    const connection = await mysql.createConnection({host:'localhost', user: 'root', database: 'world'});
    const [rows, fields] = await connection.execute(sentenciaSql);

    
    if(rows.affectedRows == 1){
        res.status(200).send("Insercion realizada con exito");
    }
})


app.delete('/id/:id',async(req,res)=>{

    const connection = await mysql.createConnection({host:'localhost', user: 'root', database: 'world'});
    const [rows, fields] = await connection.execute('DELETE FROM mundo WHERE Id = ? ',[req.params.id]);

    res.json(rows)
    if(rows.affectedRows == 1){
        res.json({status:"Registro eliminado"});
    }
})

app.patch('/id/:id',async(req,res)=>{

    const connection = await mysql.createConnection({host:'localhost', user: 'root', database: 'world'});
    const [rows, fields] = await connection.execute(`UPDATE mundo SET Usuario = '${req.body.Usuario}', Edad = ${req.body.Edad} WHERE Id = ? `,[req.params.id]);

    //res.json(rows)
    if(rows.affectedRows == 1){
        res.status(200).send("UPDATE realizada con exito");
    }
})

const swaggerDocs = swaggerJsDoc(swaggerOptions);
app.use("/api-docs",swaggerUI.serve,swaggerUI.setup(swaggerDocs));


app.use((req,res)=>{
    res.status(404).json({estado:"Pagina no encontrada"})
})

app.listen(8082,()=>{
    console.log("Servidor Express corriendo y escuchando en el puerto 8082")
})