/*
Clase 30 - Ejercicios: Bucles
Vídeo: https://youtu.be/1glVfFxj8a4?t=12732
*/

// NOTA: Explora diferentes sintaxis de bucles para resolver los ejercicios

// 1. Crea un bucle que imprima los números del 1 al 20

for(let i = 0; i < 20; i++){
    console.log(i+1)
}

// 2. Crea un bucle que sume todos los números del 1 al 100 y muestre el resultado

let suma = 0
for(let i = 0; i < 101; i++){
    suma += i
}
console.log(suma)

// 3. Crea un bucle que imprima todos los números pares entre 1 y 50

let i = 0
    i +=2
while(i<=50){
    console.log(i)
    i += 2
}

// 4. Dado un array de nombres, usa un bucle para imprimir cada nombre en la consola

let list = ["Kevin", "Keytlin", "Yaque", "Lazaro"]
for (let value of list) {
    console.log(value)
}

// 5. Escribe un bucle que cuente el número de vocales en una cadena de texto

let string = "Hola mi nombre es Kevin"
let vocales = 0
for (let value of string){
    if(value=="a"||value=="e"||value=="i"||value=="o"||value=="u"){
         vocales++
    }      
}
console.log(vocales)
    

// 6. Dado un array de números, usa un bucle para multiplicar todos los números y mostrar el producto

list = [3, 9, 11, 21, 23]
let mult = 1
for(let i of list){
    mult *= i
}
console.log(mult)

// 7. Escribe un bucle que imprima la tabla de multiplicar del 5

for(let i = 0; i <= 10; i++){
    console.log("5 *", i,"=",i*5)
}

// 8. Usa un bucle para invertir una cadena de texto

let invertido = ""
for(let i = string.length -1; i>=0; i--){
    invertido += string[i]
}
console.log(invertido)

// 9. Usa un bucle para generar los primeros 10 números de la secuencia de Fibonacci

let previo = 0
let siguiente = 1
for(let i = 0; i < 10; i++){
    let sum = previo + siguiente
    previo = siguiente
    siguiente = sum
    console.log(sum)
}

// 10. Dado un array de números, usa un bucle para crear un nuevo array que contenga solo los números mayores a 10

let newList = []
for(let i of list){
    if(i>10){
        newList.push(i)
    }
}
console.log(newList)