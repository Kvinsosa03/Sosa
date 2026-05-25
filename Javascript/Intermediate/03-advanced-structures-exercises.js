/*
Clase 23 - Estructuras avanzadas
Vídeo: https://youtu.be/iJvLAZ8MJ2E?t=7514
*/

// 1. Utiliza map, filter y reduce para crear un ejemplo diferente al de la lección

let list = [8, 1, 23, 3, 9, 31, 20, 17, 2, 11]

let mapList = list.map(i => i*2-1)
console.log(mapList)
let filterList = list.filter(i => i<20 && i>10)
console.log(filterList)
let reduceList = list.reduce((i,j) => i+j )
console.log(reduceList)

// 2. Dado un array de números, crea uno nuevo con dichos números elevados al cubo y filtra sólo los números pares

let newList = list.map(i => i**3)
console.log(newList)
console.log(newList.filter(i => i%2 === 0))

// 3. Utiliza flat y flatMap para crear un ejemplo diferente al de la lección

let array = ["Hola",['Mi nomre es',"Kevin","Sosa",["Tengo 22"]]]
let newArray = array.flat(3)
console.log(newArray)
console.log(newArray.flatMap(i => i.split(" ")))

// 4. Ordena un array de números de mayor a menor

let orden = list.sort((a,b) => b-a)
console.log(orden)

// 5. Dados dos sets, encuentra la unión, intersección y diferencia de ellos

let set1 = new Set([1,2,3,4,5])
let set2 = new Set([10,2,33,4,51])
let union = new Set([...set1,...set2])
let intersección = new Set([...set1].filter(i => set2.has(i)))
let diferencia = new Set([...set1].filter(i => !set2.has(i)))
console.log(union)
console.log(intersección)
console.log(diferencia)

// 6. Itera los resultados del ejercicio anterior

union.forEach(i => console.log(i))
intersección.forEach(i => console.log(i))
diferencia.forEach(i => console.log(i))

// 7. Crea un mapa que almacene información se usuarios (nombre, edad y email) e itera los datos

let map = new Map([
    ["nombre","Kevin"],
    ["edad", 22],
    ["email", "kevinso030723@gmail.com"]
])
map.forEach((value,key) => console.log(`${key} : ${value}`))

// 8. Dado el mapa anterior, crea un array con los nombres

let array2 = Array.from(map)
console.log(array2)

// 9. Dado el mapa anterior, obtén un array con los email de los usuarios mayores de edad y transfórmalo a un set



// 10. Transforma el mapa en un objeto, a continuación, transforma el objeto en un mapa con clave el email de cada usuario y como valor todos los datos del usuario