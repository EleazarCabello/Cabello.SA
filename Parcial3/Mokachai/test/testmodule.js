
let modulo = require('../src/modulo.js')
let expect = require('chai').expect;

describe("pruebas a la funcion Area Triangulo",function(){
    it("Deberia de regresar un numero 3",function(){
        let resultado=modulo.areaTriangulo(2,3)

        expect(resultado).to.be.a("number");
        expect(resultado).to.equal(3);
    })

})