/*
Clase 38 - Objetos y clases avanzados
Vídeo: https://youtu.be/iJvLAZ8MJ2E?t=11832
*/

// 1. Agregega una función al prototipo de un objeto

let personGeneral = {
    name: "Kevin",
    age: 22
}

let person1 = personGeneral
console.log( typeof person1)
console.log(person1)
person1.greet = function(){
    console.log("Hola")
}
person1.greet()

// 2. Crea un objeto que herede de otro

let person2 = Object.create(personGeneral)
person2.surname = "Sosa"
console.log(person2.name)
console.log(person2.age)
console.log(person2.surname)
person2.greet()

// 3. Define un método de instancia en un objeto

function Person(name, age) {
    this.name = name
    this.age = age
}

Person.prototype.greet = function () {
    console.log(`Hola, soy ${this.name}`)
}

let newPerson = new Person("Brais", 37)
newPerson.greet()

// 4. Haz uso de get y set en un objeto

let SetGet = {
    name: "Kevin",
    age: 22,

    set(name){
        this.name = name
    },

    get(){ 
        console.log(`El nombre es ${this.name}`)
    }
}
let value1 = SetGet
value1.set('Key')
value1.get()

// 5. Utiliza la operación assign en un objeto

let fullPerson = Object.assign(SetGet, person2)
console.log(fullPerson)

// 6. Crea una clase abstracta

class Abstracta{
    constructor(name){
        if(new.target===Abstracta){
            throw new Error("No se puede instanciar una clase abstracta")
        }
        this.name = name
    }
}

// 7. Utiliza polimorfismo en dos clases diferentes

class Person1{
    constructor(name,age){
        this.name = name
        this.age = age
    }
    hobies(){
        console.log("Hace Ejercicios")
    }
}
class Hombre extends Person1{
    hobies(){
        console.log("Hace Hierro")
    }
}
let Kevin = new Hombre("Kevin",22)
console.log(Kevin)
Kevin.hobies()

// 8. Implementa un Mixin

class Mujer extends Person1{
    hobies(){
        console.log("Hace pilates")    
    }
}

let Comida = {
    comidaFavorita(){
        console.log("spaguetis")    
    }
}

Object.assign(Hombre.prototype,Comida)
Object.assign(Mujer.prototype,Comida)

Kevin.comidaFavorita()

// 9. Crea un Singleton

class Session{
    constructor(name){
        if (Session.instance) {
            return Session.instance
    }
    this.name = name
    Session.instance = this
    }
}
let session1 = new Session("Kevin")
let session2 = new Session("Key")
console.log(session1.name)    
console.log(session2.name)    

// 10. Desarrolla un Proxy