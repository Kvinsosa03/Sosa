/*
Clase 20 - Ejercicios: Operadores
Vídeo: https://youtu.be/1glVfFxj8a4?t=6458
*/

// 1. Crea una variable para cada operación aritmética

let suma = 1+1
let resta = 1-1
let mult = 2*2
let division = 10/2
let modulo = 10%2
let exponente = 10**2

// 2. Crea una variable para cada tipo de operación de asignación,
//    que haga uso de las variables utilizadas para las operaciones aritméticas

let varible = 10
varible += 2
varible -= 2
varible *= 2
varible /= 2
varible %= 2
varible **= 2

// 3. Imprime 5 comparaciones verdaderas con diferentes operadores de comparación

console.log(2==2)
console.log(2<5)
console.log(2>1)
console.log(2<=5)
console.log(2>=2)

// 4. Imprime 5 comparaciones falsas con diferentes operadores de comparación

console.log(2==5)
console.log(2<1)
console.log(2>5)
console.log(2<=1)
console.log(2>=5)

// 5. Utiliza el operador lógico and

console.log(2<=5 && 2==2)

// 6. Utiliza el operador lógico or

console.log(2<=5 || 5==2)

// 7. Combina ambos operadores lógicos

console.log(2<=5 && 2==2 || 10<15)

// 8. Añade alguna negación

console.log(!(2<=5 && 2==2 || 10<15))

// 9. Utiliza el operador ternario

const myVariable = true
myVariable ? console.log("bien") : console.log("mal")

// 10. Combina operadores aritméticos, de comparáción y lógicas

