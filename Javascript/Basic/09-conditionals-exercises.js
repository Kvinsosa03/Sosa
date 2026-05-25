/*
Clase 24 - Ejercicios: Condicionales
Vídeo: https://youtu.be/1glVfFxj8a4?t=8652
*/

// if/else/else if/ternaria

// 1. Imprime por consola tu nombre si una variable toma su valor

let nombre = "Sosa"
if (nombre == "Kevin"){
    console.log("Kevin")
}else{
    console.log("No Kevin")
}

// 2. Imprime por consola un mensaje si el usuario y contraseña concide con unos establecidos

let usuario = "Kevin"
let contraseña = "abkevinso"
if(usuario == "Kevin" && contraseña == "abkevinso"){
    console.log("Bien")
}else{
    console.log("Mal")
}

// 3. Verifica si un número es positivo, negativo o cero e imprime un mensaje

let number = 15
if(number == 0){
    console.log('Es 0')
}else if(number < 0){
    console.log("Es negativo")
}else{
    console.log("Es positivo")
}

// 4. Verifica si una persona puede votar o no (mayor o igual a 18) e indica cuántos años le faltan

let edad = 18 - number
if(number <= 18){
    console.log(`No puede votar, le faltan, ${edad} años`)
}else{
    console.log("Puede votar")
}

// 5. Usa el operador ternario para asignar el valor "adulto" o "menor" a una variable
//    dependiendo de la edad 

let mensaje = edad >= 18 ? "Adulto" : "Menor"
console.log(mensaje) 

// 6. Muestra en que estación del año nos encontramos dependiendo del valor de una variable "mes"

let variable = 2
let mes 

switch (variable) {
    case 0:
        mes = "Enero"
        break
    case 1:
        mes = "Febrero"
        break
    case 2:
        mes = "Marzo"
        break
    case 3:
        mes = "Abril"
        break
    case 4:
        mes = "Mayo"
        break
    case 5:
        mes = "Junio"
        break
    case 6:
        mes = "Julio"
        break
    case 7:
        mes = "Agosto"
        break
    case 8:
        mes = "Septiembre"
        break
    case 9:
        mes = "Octubre"
        break
    case 10:
        mes = "Noviembre"
        break    
    default:
        mes = "Diciembre"
}
console.log(mes)

// 7. Muestra el número de días que tiene un mes dependiendo de la variable del ejercicio anterior

// switch

// 8. Usa un switch para imprimir un mensaje de saludo diferente dependiendo del idioma

// 9. Usa un switch para hacer de nuevo el ejercicio 6

// 10. Usa un switch para hacer de nuevo el ejercicio 7