

  new gridjs.Grid({
    columns: ["Id", "Usuario", "Edad"],

    server:{
        url: 'http://localhost:8082/usuario',
        then: data => data.map(usuario => [usuario.Id, usuario.Usuario, usuario.Edad])
    }

  }).render(document.getElementById("wrapper"));