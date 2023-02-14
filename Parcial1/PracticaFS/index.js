const fsc = require('fs');
const fsp = require('fs').promises;
const path = require('path')

fsc.writeFile(path.join(__dirname,'archivo.txt'),"Archivo creado api callback",(err)=>{
    if (err){
        console.log(err)
    }else{
        console.log('Archivo creado con el api fs callback')
    }
});

(async () => {
    try{
    await fsp.writeFile(path.join(__dirname,'archivo2.txt'),"archivo creado api promesas")
    console.log("Archivo creado con el api fs promises")
    }catch(err){
        console.log(err);
    }
})();

console.log(__dirname)
console.log(__filename)