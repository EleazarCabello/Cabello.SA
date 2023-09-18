const yaml = require('yaml');
const fs = require('fs');

const path = require('path');

//path es para que identifique en que carpeta se ubica
const archivoObj = fs.readFileSync(path.join(__dirname,'./objeto.yml'), 'utf8')
const valorObj = yaml.parse(archivoObj);
console.table(valorObj);

const archivoArray = fs.readFileSync(path.join(__dirname,'./array.yml'), 'utf8')
const valorArray = yaml.parse(archivoArray);
console.table(valorArray);

const archivoObjArray = fs.readFileSync(path.join(__dirname,'./objetoArray.yml'), 'utf8')
const valorObjArray = yaml.parse(archivoObjArray);
console.table(valorObjArray);

const archivoArrayObj = fs.readFileSync(path.join(__dirname,'./arrayObjetos.yml'), 'utf8')
const valorArrayObj = yaml.parse(archivoArrayObj);
console.table(valorArrayObj);