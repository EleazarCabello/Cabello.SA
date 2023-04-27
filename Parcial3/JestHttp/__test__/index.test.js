const request = require("supertest")
const url = "http://localhost:8082"

describe('Testear Get a la ruta de Usuario ',()=>{
    it("Deberia regresar codigo 200",()=>{
        request(url)
            .get('/usuario')
            .end(function(err,res){
            expect(res.statusCode).toBe(200);
})
    })  
})

describe('Testear Get a la ruta de Usuario con Call Back Async-Await ',()=>{
    it("Deberia regresar codigo 200",async()=>{
        let response = await request(url).get('/usuario')
        expect(response.statusCode).toBe(200)
})
})
