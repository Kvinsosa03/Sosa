/*
Clase 27 - Maps
Vídeo: https://youtu.be/1glVfFxj8a4?t=10755
*/

// Map (Diccionario: Clave, Valor)  

// Declaración

let myMap = new Map()

console.log(myMap)

// Inicialiación

myMap = new Map([
    ["name", "Brais"],
    ["email", "braismoure@mouredev.com"],
    ["age", 37]
])

console.log(myMap)

// Métodos y propiedades

// set // actualiza o agrega elemento

myMap.set("alias", "mouredev")
myMap.set("name", "Brais Moure")

console.log(myMap)

// get // recuperar valores

console.log(myMap.get("name"))
console.log(myMap.get("surname"))

// has // comprobar si existe una clave

console.log(myMap.has("surname"))
console.log(myMap.has("age"))

// delete

myMap.delete("email")

console.log(myMap)

// keys, values y entries

console.log(myMap.keys()) // listados con claves
console.log(myMap.values()) // listado con valores
console.log(myMap.entries()) // listado con claves y valores

// size // tamano

console.log(myMap.size)

// clear

myMap.clear()

console.log(myMap)



