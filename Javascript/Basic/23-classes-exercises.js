/*
Clase 39 - Ejercicios: Clases
Vídeo: https://youtu.be/1glVfFxj8a4?t=18630
*/

// 1. Crea una clase que reciba dos propiedades

class Person{
    constructor(name,surname){
        this.name = name
        this.surname = surname
    }
}
let person = new Person("Kevin","Sosa")
console.log(person)

// 2. Añade un método a la clase que utilice las propiedades

Person.prototype.presentarse = function(){
    console.log(`Mi nombre es ${this.name} ${this.surname}`)
}

// 3. Muestra los valores de las propiedades e invoca a la función

console.log(person)
person.presentarse()

// 4. Añade un método estático a la primera clase

Person.saludo = function(){
    console.log("Hola")
}

// 5. Haz uso del método estático

Person.saludo()

// 6. Crea una clase que haga uso de herencia

class Kevin extends Person{
    ocupation(){
        console.log("Soy estudiante")
    }
}
let value = new Kevin("Kevin","Sosa")
value.presentarse()
value.ocupation()
Kevin.saludo()

// 7. Crea una clase que haga uso de getters y setters 
// 8. Modifica la clase con getters y setters para que use propiedades privadas
// 9. Utiliza los get y set y muestra sus valores

class Person2{

    #age
    #name
    #surname

    constructor(name,surname,age){
        this.#name = name
        this.#surname = surname
        this.#age = age
    }
    get name(){
        return this.#name
    }
    get surname(){
        return this.#surname
    }
    set age(age){
        this.#age = age
    }
}
let value2 = new Person2("Kevin","Sosa",22)
console.log(value2)
console.log(value2.name)
console.log(value2.surname)
console.log(value2.age)
value2.age = 23

// 10. Sobrescribe un método de una clase que utilice herencia 