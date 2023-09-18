const express = require('express');
const mysql = require('mysql2/promise')
const app = express();
const cors = require('cors')
const swaggerUI = require('swagger-ui-express');
const swaggerJsDoc = require('swagger-jsdoc');
const fs = require('fs');
const { SwaggerTheme } = require('swagger-themes');
const redoc = require('redoc-express');
const path = require('path');


//Thema swagger json
const theme = new SwaggerTheme('v3');
const options = {
    explorer: true,
    customCss: theme.getBuffer('dark')
  };
  

let ContenidoReadme = fs.readFileSync(path.join(__dirname)+'/README.md',{encoding:'utf8',flag:'r'})
let apidef_string = fs.readFileSync(path.join(__dirname)+'/APIdef.json',{encoding:'utf8',flag:'r'})
let apidef_objeto = JSON.parse(apidef_string)
apidef_objeto.info.description=ContenidoReadme;

let redocTheme_string = fs.readFileSync(path.join(__dirname)+'/APIdef.json',{encoding:'utf8',flag:'r'})
let redocTheme_objeto = JSON.parse(apidef_string)

app.use(express.json())
app.use(express.text())
app.use(cors())

const swaggerOptions = {
    definition: apidef_objeto,
    apis: [`${path.join(__dirname,"./index.js")}`],
    };

/**
 * @swagger
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
 *     patch: 
 *       type: object
 *       properties: 
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
 *        content:
 *          application/json:
 *            schema:
 *              $ref: '#/components/schemas/usuario'
 */
app.get('/usuario',async(req,res)=>{
  const connection = await mysql.createConnection({host:'localhost', user: 'root', database: 'world'});
  const [rows, fields] = await connection.execute('SELECT * FROM mundo');

  res.json(rows);
})
//AGREGAR PUERTO Y PASSWORD

/**
 * @swagger
 * /usuario/{id}:
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
 *        content:
 *          application/json:
 *            schema:
 *              $ref: '#/components/schemas/usuario'
 *      400:
 *        description: No se encontro usuario.
 */
app.get('/usuario/:id',async(req,res)=>{

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
 * /usuario:
 *   post:
 *     tags:
 *       - usuario
 *     summary: Registrar un usuario
 *     description: Petición Post a la ruta de Usuarios para ingresar un nuevo registro
 *     requestBody:
 *       description: Crea un nuevo usuario
 *       content:
 *         application/json:
 *           schema:
 *               $ref: '#/components/schemas/usuario'
 *     responses:
 *       200:
 *         description: Insercion realizada con exito
 */
app.post('/usuario',async(req,res)=>{
    let sentenciaSql = `insert into mundo values(${req.body.Id},'${req.body.Usuario}','${req.body.Edad}')`;
    const connection = await mysql.createConnection({host:'localhost', user: 'root', database: 'world'});
    const [rows, fields] = await connection.execute(sentenciaSql);

    
    if(rows.affectedRows == 1){
        res.status(200).send("Insercion realizada con exito");
    }
})

/**
 * @swagger
 * /usuario/{id}:
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
 *           type: integer
 *           format: int64
 *     responses:
 *       200:
 *         description: El registro se elimino correctamente.
 */

app.delete('/usuario/:id',async(req,res)=>{

    const connection = await mysql.createConnection({host:'localhost', user: 'root', database: 'world'});
    const [rows, fields] = await connection.execute('DELETE FROM mundo WHERE Id = ? ',[req.params.id]);

    //res.json(rows)
    if(rows.affectedRows == 1){
        res.status(200).send("El registro se elimino correctamente.");
    }
})

/**
 * @swagger
 * /usuario/{id}:
 *   patch:
 *     tags:
 *       - usuario
 *     summary: Actualizar usuario
 *     description: Petición Patch a la ruta de Usuarios
 *     parameters:
 *       - name: id
 *         in: path
 *         description: ID del usuario que desea actualizar
 *         required: true
 *         schema:
 *           type: integer
 *           format: int64
 *     requestBody:
 *       description: Crea un nuevo usuario
 *       content:
 *         application/json:
 *           schema:
 *             $ref: '#/components/schemas/patch'
 *     responses:
 *       200:
 *         description: UPDATE realizada con exito.
 *         content:
 *           application/json:
 *             schema:
 *               $ref: '#/components/schemas/patch'
 */

app.patch('/usuario/:id',async(req,res)=>{

    const connection = await mysql.createConnection({host:'localhost', user: 'root', database: 'world'});
    const [rows, fields] = await connection.execute(`UPDATE mundo SET Usuario = '${req.body.Usuario}', Edad = ${req.body.Edad} WHERE Id = ? `,[req.params.id]);


    if(rows.affectedRows == 1){
        res.status(200).send("UPDATE realizada con exito");
    }
})

const swaggerDocs = swaggerJsDoc(swaggerOptions);
app.use("/api-docs",swaggerUI.serve,swaggerUI.setup(swaggerDocs,options));
app.get("/docs.json",(req,res)=>{
    res.json(swaggerDocs);
})

app.get(
    '/redocs',
    redoc({
      title: 'API Docs',
      specUrl: '/docs.json',
      nonce: '', // <= it is optional,we can omit this key and value
      // we are now start supporting the redocOptions object
      // you can omit the options object if you don't need it
      // https://redocly.com/docs/api-reference-docs/configuration/functionality/
      redocOptions: {
        theme: redocTheme_objeto
      }
    })
  );

app.use((req,res)=>{
    res.status(404).json({estado:"Pagina no encontrada"})
})

app.listen(8082,()=>{
    console.log("Servidor Express corriendo y escuchando en el puerto 8082")
})