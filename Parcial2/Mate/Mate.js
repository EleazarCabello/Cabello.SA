/**
 * Funcion que calcula el area de un cuadrado
 * @param {Number} lado Lado del cuadrado
 * @returns Resultado del cuadrado
 */
export function areaCuadrada (lado){
    return lado*lado ;
}

/**
 * Esta funcion calcula el area de un triangulo
 * @param {Number} base Base del triangulo
 * @param {Number} altura Altura del triangulo
 * @returns Area del tringulo
 */
export function areaTriangulo (base,altura){
    return (base*altura)/2
}

/**
 * Esta funcion calcula el area de un circulo
 * @param {Number} radio Radio del circulo
 * @returns Area del circulo
 */
export function areaCirculo (radio){
    return Math.pow(radio*Math.PI),2;
}