let http = require('http');

let servidor = http.createServer(function (req, res) {
res.write('Servidor HTTP contestando al 100%');
res.end();
})
servidor.listen(8081, () => console.log('Servidor listo y contestando'));