let modulo = require("../src/modulo")

describe('set de test al modulo',()=>{
    test('Si le mando 2 y 3 debe regresar 3',()=>{
        expect(modulo.areaTriangulo(2,3)).toBe(3);
    })
})