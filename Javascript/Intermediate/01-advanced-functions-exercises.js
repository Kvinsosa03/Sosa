/*
Clase 12 - Funciones avanzadas
Vídeo: https://youtu.be/iJvLAZ8MJ2E?t=4112
*/

// 1. Crea una función que retorne a otra función

function func1(){
    return func2()
}
function func2(){
        console.log("func2 esta dentro de func1")
}   
func1()

// 2. Implementa una función currificada que multiplique 3 números

function multiply(a){
    return function (b){
        return function(c){
            return a*b*c
        }
    }
}
console.log(multiply(2)(2)(10))
let valueA = multiply(2)
let valueAB = valueA(2)
let valueABC = valueAB(10)
console.log(valueABC)

// 3. Desarrolla una función recursiva que calcule la potencia de un número elevado a un exponente

function recursiva(a,b){
    if(b<0){
        throw new Error("El exponente debe ser positivo")
    }else if(b==0){
        return 1
    }
    return a * recursiva(a,b-1)
}
console.log(recursiva(2,5))

// 4. Crea una función createCounter() que reciba un valor inicial y retorne un objeto con métodos para increment(), decrement() y getValue(), utilizando un closure para mantener el estado

function createCounter(a){
    let value = a
    let objeto = {
       increment: function(){
            value++
            console.log(value)
       },
       decrement: function(){
            value--
            console.log(value)
       },
       getValue: function(){
            console.log(`El valor es: ${value}`)
       }
    }
    return objeto
}
console.log(createCounter())
let value = createCounter(0)
value.increment()
value.increment()
value.increment()
value.decrement()
value.decrement()
value.getValue()

// 5. Crea una función sumManyTimes(multiplier, ...numbers) que primero sume todos los números (usando parámetros Rest) y luego multiplique el resultado por multiplier

function sumManyTimes(multiplier, [...numbers]){
    let suma = 0
    for (let number of numbers) {
        suma += number
    }
    return suma * multiplier
}
let list = [1,2,3,4,5]
console.log(sumManyTimes(2,list))

// 6. Crea un Callback que se invoque con el resultado de la suma de todos los números que se le pasan a una función

function func3(Callback,...numbers){
       let suma = 0
    for (let number of numbers) {
        suma += number
    }
    Callback(suma)
}
function mostrar(suma){
    console.log(`La suma es ${suma}`)
}
func3(mostrar,1,2,3,4,5)

// 7. Desarrolla una función parcial

function func4(a){
    return function (b,c){
            return a*b*c
        }
}
let value1 = func4(2)
console.log(value1(2,2))

// 8. Implementa un ejemplo que haga uso de Spread

const numbers = [1, 2, 3]
function func5(a, b, c) {
    return a + b + c
}
console.log(func5(...numbers))

// 9. Implementa un retorno implícito

const multiply = (a, b) => a * b
console.log(multiply(2, 5))

// 10. Haz uso del this léxico
