/*
Clase 34 - Ejercicios: Objetos
Vídeo: https://youtu.be/1glVfFxj8a4?t=15675
*/

// 1. Crea un objeto con 3 propiedades

let person ={
    myName: "Kevin",
    myAge: 22,
    ocupation: "student"
}
console.log(person)

// 2. Accede y muestra su valor

console.log(person.myName)
console.log(person.myAge) 
console.log(person.ocupation)

// 3. Agrega una nueva propiedad

person.surName = "Sosa"
console.log(person.surName)

// 4. Elimina una de las 3 primeras propiedades

delete person.myName
delete person.myAge
delete person.ocupation
console.log(person)

// 5. Agrega una función e invócala

person.walk = function() {
    console.log("Kevin camina")
}
person.walk()

// 6. Itera las propiedades del objeto

for(let i in person){
    console.log(i, ":",person[i])
}

// 7. Crea un objeto anidado

let person2 ={
    myName: "Kevin",
    myAge: 22,
    ocupation: "student",
    favorite: {
        movie: "Avatar",
        serie: "Game of Trones"
    }
}

// 8. Accede y muestra el valor de las propiedades anidadas

console.log(person2.favorite.movie)
console.log(person2.favorite.serie)

// 9. Comprueba si los dos objetos creados son iguales

console.log(person.name == person2.name)

// 10. Comprueba si dos propiedades diferentes son iguales

console.log(person.name == person2.ocupation)