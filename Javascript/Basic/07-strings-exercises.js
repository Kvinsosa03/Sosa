/*
Clase 22 - Ejercicios: Strings
Vídeo: https://youtu.be/1glVfFxj8a4?t=7226
*/

// 1. Concatena dos cadenas de texto

let nombre = "Kevin"
let saludo = "Hola " + nombre 
console.log(saludo)

// 2. Muestra la longitud de una cadena de texto

console.log(saludo.length)

// 3. Muestra el primer y último carácter de un string

console.log(saludo[0])
console.log(saludo[9])

// 4. Convierte a mayúsculas y minúsculas un string

console.log(saludo.toUpperCase())
console.log(saludo.toLowerCase())

// 5. Crea una cadena de texto en varias líneas

let other = `Cadena
de texto
en varias
lineas`
console.log(other)

// 6. Interpola el valor de una variable en un string

console.log(`Mi nombre es ${nombre}`)

// 7. Reemplaza todos los espacios en blanco de un string por guiones

console.log(saludo.replace(" ","-"))

// 8. Comprueba si una cadena de texto contiene una palabra concreta

console.log(saludo.includes("Sosa"))

// 9. Comprueba si dos strings son iguales

console.log(saludo==other)

// 10. Comprueba si dos strings tienen la misma longitud

console.log(saludo.length == other.length)
