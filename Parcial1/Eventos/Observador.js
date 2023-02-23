let fs = require('fs');
let path = require('path');

let archivoobs = path.join(__dirname,'Observador.txt')
console.log(archivoobs);

obs = fs.watch(archivoobs,function(evento,archivo){
    console.log('Sucedio el evento ${evento} en el archivo ${archivo}');
});

obs.on('change',function(){
    console.log('Se cambio el archivo')
})

obs.on('error',function(){
    console.log('Sucedio un error')
})