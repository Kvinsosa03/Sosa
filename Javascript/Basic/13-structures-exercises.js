/*
Clase 28 - Ejercicios: Estructuras
Vídeo: https://youtu.be/1glVfFxj8a4?t=11451
*/

// 1. Crea un array que almacene cinco animales

let myArray = ["perro","gato" ,"halcon" ,"leon" ,"paloma" ]
console.log(myArray)

// 2. Añade dos más. Uno al principio y otro al final

myArray.push('caballo')
myArray.unshift("tigre")
console.log(myArray)

// 3. Elimina el que se encuentra en tercera posición

myArray.pop(2)
console.log(myArray)

// 4. Crea un set que almacene cinco libros

let mySet = new Set(["libro1","libro2" ,"libro3" ,"libro4" ,"libro5" ])
console.log(mySet)

// 5. Añade dos más. Uno de ellos repetido

mySet.add("libro6")
mySet.add("libro6")
console.log(mySet)

// 6. Elimina uno concreto a tu elección

mySet.delete("libro2")
console.log(mySet)

// 7. Crea un mapa que asocie el número del mes a su nombre

let myMap = new Map([
    [1, "enero"],
    [2, "febrero"],
    [3, "marzo"],
    [4, "abril"],
    [5, "mayo"],
    [6, "junio"],
    [7,"julio"],
    [8, "agosto"],
    [9, "septiembre"],
    [10, "octubre"],
    [11, "nobiembre"],
    [12,"diciembre"]
])
console.log(myMap)

// 8. Comprueba si el mes número 5 existe en el map e imprime su valor

console.log(myMap.has(5))

// 9. Añade al mapa una clave con un array que almacene los meses de verano

let verano = ["junio", "julio", "agosto"]
myMap.set("verano", verano)
console.log(myMap)

// 10. Crea un Array, transfórmalo a un Set y almacénalo en un Map

let newArray = []
let newSet = new Set()
newArray = Array.from(newSet)
myMap.set(newSet)
console.log(myMap)