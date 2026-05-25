// /*
// Clase 45 - Asincronía
// Vídeo: https://youtu.be/iJvLAZ8MJ2E?t=14558
// */

// 1. Crea una función para saludar que reciba un nombre y un callback. 
//    El callback debe ejecutarse después de 2 segundos y mostrar en consola "Hola, [nombre]".

function func1(name,callback){
    setTimeout(() => {
        callback(name)
    },500)
}
function saludo(name){
    console.log(`Hola, ${name}`)
}
func1("Kevin",saludo)


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

// 6. Crea una función getUser(id) que devuelva una promesa y simule una llamada a una API (que se demore 2s).
//    Si el id es menor a 5, la promesa se resuelve con { id, nombre: "Usuario " + id }.
//    Si el id es 5 o mayor, la promesa se rechaza con el mensaje "Usuario no encontrado".
//    Usa async/await para llamar a getUser(id) y maneja los errores con try/catch.

let usuario ={
    Id: 23,
    Usuario: "Kevin"
}

function getUser(id){
    return new Promise((resolve,reject) => {
        setTimeout(() => {
            if(id<5){
                console.log(id, "Nombre: ",usuario.Usuario, usuario.Id)
                resolve()
            }else if(id>=5){
                console.log("Usuario no encontrado")
                reject()
            } 
        },2000)   
    })
}
async function main(params) {
    try{
        await getUser(params)
        console.log("Operacion Exitosa")
    }catch(error){
        console.log("Operacion Fallida")
    }
    
}
main(5)

// 7. Intenta predecir el resultado de este código antes de ejecutarlo en la consola:
console.log("Inicio")
setTimeout(() => console.log("setTimeout ejecutado"), 0)
Promise.resolve().then(() => console.log("Promesa resuelta"))
console.log("Fin")

/*
Inicio
Fin
Promesa resuelta
setTimeout ejecutado
*/

// 8. Crea tres funciones que devuelvan promesas con tiempos de espera distintos.
//    A continuación, usa Promise.all() para ejecutarlas todas al mismo tiempo y mostrar "Todas las promesas resueltas" cuando terminen.

function tareas(ms,mensaje){
    return new Promise((a,b) => {
        setTimeout(() => a(mensaje),ms)
    })
}
Promise.all([
    tareas(2000,"Tarea uno lista"),
    tareas(1000,"Tarea dos lista"),
    tareas(3000,"Tarea tres lista"),
])
.then(a => {
    console.log("todas las tareas completadas")
    console.log(a)
})
.catch(b => {console.log("alguna tarea fallo") })


// 9. Crea una función waitSeconds(segundos) que use setTimeout dentro de una Promesa para esperar la cantidad de segundos indicada.
//    A continuación, usa async/await para que se espere 3 segundos antes de mostrar "Tiempo finalizado" en consola.

function waitSeconds(segundos){
    return new Promise( result => setTimeout(result,segundos))
}
async function main() {
    await waitSeconds(3000)
    console.log("Tiempo finalizado") 
}
main()

// 10. Crea una simulación de un cajero automático usando asincronía.
//     - La función checkBalance() tarda 1s y devuelve un saldo de 500$.
//     - La función withdrawMoney(amount) tarda 2s y retira dinero si hay suficiente saldo, o devuelve un error si no hay fondos.
//     - Usa async/await para hacer que el usuario intente retirar 300$ y luego 300$ más.
//     
//     Posible salida esperada:
//     Saldo disponible: 500$
//     Retirando 300$...
//     Operación exitosa, saldo restante: 200$
//     Retirando 300$...
//     Error: Fondos insuficientes

let caja ={
    Saldo: 500
}

function checkBalance(){
    setTimeout(() => {
        console.log(`Saldo disponible: ${caja.Saldo}$`)
    },1000)
}
function withdrawMoney(amount){
    return  new Promise((a,b) => {
        setTimeout(() => {
            if(amount<=caja.Saldo){
                caja.Saldo = caja.Saldo-amount
                console.log(`Retirando ${amount}$...`)
                a(`Operación exitosa, saldo restante: ${caja.Saldo}$`)
            }else{
                console.log(`Retirando ${amount}$...`)
                b(" Error: Fondos insuficientes")
            }
        },2000)
    })
}
async function cajeroAutomático() {

    await checkBalance()

    await withdrawMoney(300)
        .then(a => console.log(a))
        .catch(b => console.log(b))

    await withdrawMoney(300)
        .then(a => console.log(a))
        .catch(b => console.log(b))

    
}

cajeroAutomático()