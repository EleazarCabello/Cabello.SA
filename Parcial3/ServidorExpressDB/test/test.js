let chai = require('chai');
let chaiHttp = require('chai-http');
const expect = require('chai').expect;

chai.use(chaiHttp);

const url = 'http://localhost:8082';

describe('Consulta de Usuarios: ',()=>{
    it('deberia consultar el usuario 1', (done)=>{
        chai.request(url)
        .get('/id/1')
        .end( function(err,res){
            expect(res).to.have.status(200);
            expect(res.text).to.be.a('string');
            done();
            
        })
    })
})