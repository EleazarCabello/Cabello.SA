let events = require('events');
let em = new events.EventEmitter();

em.on('saludar',function(sata){
    console.log("Hola Mundo "+ data);
})

em.addListener('saludar',function(sata){
    console.log("Hola Mundo 2do Listener"+ data);
});

em.emit('saludar','Juan');