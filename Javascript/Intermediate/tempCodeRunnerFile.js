// 2. Crea tres funciones task1(callback), task2(callback) y task3(callback). 
//    Cada función debe tardar 1 segundo en ejecutarse y luego llamar al callback.

function task1(callback){
    setTimeout(() => {
        console.log("Un segundo")
        callback()
    },1000)
}
function task2(callback){
    setTimeout(() => {
        console.log("Dos segundos")
        callback()
    },1000)
}
function task3(callback){
    setTimeout(() => {
        console.log("Tres segundos")
        callback()
    },1000)
}
task1(() => {
    task2(() => {
        task3(() => {
            console.log("Ya pasaron lo tres segundos")
        })
    })
})

// 3. Crea una función para verificar un número que retorne una Promesa. 
//    Si el número es par, la promesa se resuelve con el mensaje "Número par". 
//    Si el número es impar, la promesa se rechaza con el mensaje "Número impar".

function Promesa(a){
    return new Promise((resolve,reject) =>{
            if(a%2 === 0){
                resolve("Numero par")
            }else{
                reject("Numero Impar")
            }
        })
}

Promesa(4)
    .then(result => console.log(result))
    .catch(error => console.log(error))

// 4. Crea tres funciones que devuelvan promesas:
//    firstTask(): tarda 1s y muestra "Primera tarea completada".
//    secondTask(): tarda 2s y muestra "Segunda tarea completada".
//    thirdTask(): tarda 1.5s y muestra "Tercera tarea completada".

function Promesa1(){
    return new Promise((resolve) =>{
        setTimeout(() =>{
            console.log("Primera tarea completada")
            resolve()
        },1000) 
    })   
}
function Promesa2(){
    return new Promise((resolve) =>{
        setTimeout(() =>{
            console.log("Segunda tarea completada")
            resolve()
        },2000) 
    })   
}
function Promesa3(){
    return new Promise((resolve) =>{
        setTimeout(() =>{
            console.log("Tercera tarea completada")
            resolve()
        },1500) 
    })   
}
Promesa1()
    .then(Promesa2())
    .then(Promesa3())

// 5. Transforma el ejercicio anterior de Promesas en una función async/await llamada executeTasks().

function Promesa(ms){
    return new Promise(resolve => setTimeout(resolve,ms))
}
async function executeTasks() {
    await Promesa(4000)
    console.log("Primera tarea completada con async/await")
    await Promesa(2000)
    console.log("Segunda tarea completada con async/await")
    await Promesa(1000)
    console.log("Tercera tarea completada con async/await")
}
executeTasks()