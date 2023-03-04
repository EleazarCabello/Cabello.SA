/*new gridjs.Grid({
    columns: ["Name", "Email", "Phone Number"],
    data: [
      ["John", "john@example.com", "(353) 01 222 3333"],
      ["Mark", "mark@gmail.com", "(01) 22 888 4444"],
      ["Eoin", "eoin@gmail.com", "0097 22 654 00033"],
      ["Sarah", "sarahcdd@gmail.com", "+322 876 1233"],
      ["Afshin", "afshin@mail.com", "(353) 22 87 8356"]
    ]
  }).render(document.getElementById("wrapper"));*/

  new gridjs.Grid({
    columns: ["Id", "Nombre", "Edad"],

    server:{
        url: 'http://localhost:8082/usuario',
        then: data => data.map(usuario => [usuario.Id],[usuario.Nombre],[usuario.Edad])
    }

  }).render(document.getElementById("wrapper"));