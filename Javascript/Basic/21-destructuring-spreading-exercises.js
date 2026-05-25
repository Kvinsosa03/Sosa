/*
Clase 36 - Ejercicios: Desestructuración y propagación
Vídeo: https://youtu.be/1glVfFxj8a4?t=16802
*/

// 1. Usa desestructuración para extraer los dos primeros elementos de un array

let myArray = [1, 2, 3, 4]
let [value1, value2] = myArray
console.log(value1)
console.log(value2)

// 2. Usa desestructuración en un array y asigna un valor predeterminado a una variable

let [ , , value3 = 0, , value4 = 0] = myArray
console.log(value3)
console.log(value4)

// 3. Usa desestructuración para extraer dos propiedades de un objeto

let person = {
    name: "Key",
    age: 25,
    alias: "Sosita",
    ocupation: "cajera"
}
let {name, age} = person
console.log(name)
console.log(age)

// 4. Usa desestructuración para extraer dos propiedades de un objeto y asígnalas
//    a nuevas variables con nombres diferentes

let {name: value5, age: value6} = person
console.log(value6)
console.log(value5)

// 5. Usa desestructuración para extraer dos propiedades de un objeto anidado

let person2 = {
    name: "Kevin",
    age: 22,
    alias: "Sosa",
    walk: function () {
        console.log("La persona camina.")
    },
    job: {
        name: "student",
        exp: 16,
        work: function () {
            console.log(`La persona de ${this.age} años de experiencia trabaja.`)
        }
    }
}
let {job:{name: value7, exp: value8}} = person2
console.log(value7)
console.log(value8)

// 6. Usa propagación para combinar dos arrays en uno nuevo

let newArray = ["Kevin","Sosa",22]
let combinacion = [...myArray,...newArray]
console.log(combinacion)

// 7. Usa propagación para crear una copia de un array

let copia = [...newArray]
console.log(copia)

// 8. Usa propagación para combinar dos objetos en uno nuevo

let combinacionObjetos = {...person,...person2}
console.log(combinacionObjetos)

// 9. Usa propagación para crear una copia de un objeto

let copia2 = {...person}
console.log(copia2)

// 10. Combina desestructuración y propagación