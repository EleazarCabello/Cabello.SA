const express = require('express');
const mysql = require('mysql2/promise')
const app = express();
const cors = require('cors')
const swaggerUI = require('swagger-ui-express');
const swaggerJsDoc = require('swagger-jsdoc');
const path = require('path');
const fs = require('fs');

let ContenidoReadme = fs.readFileSync(path.join(__dirname)+'/README.md',{encoding:'utf8',flag:'r'})
let apidef_string = fs.readFileSync(path.join(__dirname)+'/APIdef.json',{encoding:'utf8',flag:'r'})
let apidef_objeto = JSON.parse(apidef_string)
apidef_objeto.info.description=ContenidoReadme;
//console.log(ContenidoReadme)

app.use(express.json())
app.use(express.text())
app.use(cors())

const swaggerOptions = {
    definition: apidef_objeto,
    apis: [`${path.join(__dirname,"./index.js")}`],
    };

/**
 * @swagger
 * 
 * components:
 *   schemas:
 *     usuario: 
 *       type: object
 *       properties:
 *         Id:
 *           type: smallint
 *           description: Identificador del usuario    
 *           example: 2 
 *         Usuario:
 *           type: string
 *           description: Nombre del usuario
 *           example: Eleazar    
 *         Edad:
 *           type: int
 *           description: Edad del usuario   
 *           example: 24 
 */


  /**
 * @swagger
 * /usuario:
 *  get:
 *    tags:
 *      - usuario
 *    summary: Consultar todos los usuarios
 *    description: Petición Get a la ruta de Usuarios
 *    responses:
 *      200:
 *        description: Regresa un Json con todos los usuarios registrados.
 */
app.get('/usuario',async(req,res)=>{
  const connection = await mysql.createConnection({host:'localhost', user: 'root', database: 'world'});
  const [rows, fields] = await connection.execute('SELECT * FROM mundo');

  res.json(rows);
})

/**
 * @swagger
 * /id/:id:
 *  get:
 *    tags:
 *      - usuario
 *    summary: Consultar un usuario en especifico por su ID
 *    description: Petición Get a un solo usuario especifico por su id de la base de datos
 *    parameters:
 *      - name: id
 *        in: path
 *        description: ID del usuario a consultar
 *        required: true
 *        schema:
 *          type: integer
 *          format: int64  
 *    responses:
 *      200:
 *        description: Regresa un Json con del usuario en especifico del cual se le solicito su ID.
 *      400:
 *        description: No se encontro usuario.
 */
app.get('/id/:id',async(req,res)=>{

    const connection = await mysql.createConnection({host:'localhost', user: 'root', database: 'world'});
    const [rows, fields] = await connection.execute('SELECT * FROM mundo WHERE id = ?',[req.params.id]);

    if(rows.length == 0){
        res.json({registros:"No se encontro usuario"});
    }else{
        res.json(rows);
    }
})

  /**
 * @swagger
 * /id:
 *   post:
 *     tags:
 *       - usuario
 *     summary: Registrar un usuario
 *     description: Petición Post a la ruta de Usuarios para ingresar un nuevo registro
 *     requestBody:
 *       description: Crea un nuevo usuario
 *       content:
 *           application/json:
 *             schema:
 *               $ref: '#/components/schemas/usuario'
 *     responses:
 *       200:
 *         description: Insercion realizada con exito
 */
app.post('/id',async(req,res)=>{
    let sentenciaSql = `insert into mundo values(${req.body.Id},'${req.body.Usuario}','${req.body.Edad}')`;
    const connection = await mysql.createConnection({host:'localhost', user: 'root', database: 'world'});
    const [rows, fields] = await connection.execute(sentenciaSql);

    
    if(rows.affectedRows == 1){
        res.status(200).send("Insercion realizada con exito");
    }
})

/**
 * @swagger
 * /id/id:
 *   delete:
 *     tags:
 *       - usuario
 *     summary: Se borra un usuario
 *     description: Petición Delete a la ruta de Usuarios para borrar un usuario por medio de un id.
 *     parameters:
 *       - name: id
 *         in: path
 *         description: ID del usuario a ELIMINAR
 *         required: true
 *         schema:
 *          type: integer
 *          format: int64  
 *     responses:
 *       200:
 *         description: Registro eliminado.
 */

app.delete('/id/:id',async(req,res)=>{

    const connection = await mysql.createConnection({host:'localhost', user: 'root', database: 'world'});
    const [rows, fields] = await connection.execute('DELETE FROM mundo WHERE Id = ? ',[req.params.id]);

    res.json(rows)
    if(rows.affectedRows == 1){
        res.json({status:"Registro eliminado"});
    }
})

/**
 * @swagger
 * /id/:id:
 *  patch:
 *    tags:
 *      - usuario
 *    summary: Actualizar usuario
 *    description: Petición Patch a la ruta de Usuarios
 *    requestBody:
 *       description: Crea un nuevo usuario
 *       content:
 *           application/json:
 *             schema:
 *               $ref: '#/components/schemas/usuario'
 *       required: true
 *    responses:
 *      200:
 *        description: UPDATE realizada con exito.
 */
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
app.get("/docs.json",(req,res)=>{
    res.json(swaggerDocs);
})

app.use((req,res)=>{
    res.status(404).json({estado:"Pagina no encontrada"})
})

app.listen(8082,()=>{
    console.log("Servidor Express corriendo y escuchando en el puerto 8082")
})