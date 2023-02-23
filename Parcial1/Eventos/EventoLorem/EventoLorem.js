const fs = require('fs');
const readStream = fs.createReadStream('./Parcial1/Eventos/EventoLorem/Lorem.txt');

readStream.on('data', (chunk) => {
  console.log(`Received ${chunk.length} bytes of data.`);
});

readStream.on('end', () => {
  console.log('Se termino de leer.');
});

readStream.on('error', (err) => {
  console.error(`Ocurrio un error: ${err}`);
});
