/*
Clase 32 - Ejercicios: Funciones
Vídeo: https://youtu.be/1glVfFxj8a4?t=14146
*/

// NOTA: Explora diferentes sintaxis de funciones para resolver los ejercicios

// 1. Crea una función que reciba dos números y devuelva su suma

function func1(a, b){
    return a + b
}
console.log(func1(2, 2))

// 2. Crea una función que reciba un array de números y devuelva el mayor de ellos

function func2(a){
    let mayor = 0
    for(let i of a){
        if(i > mayor){
            mayor = i
        }
    }
    return mayor
}
let list = [3, 9, 11, 21, 23, 8, 17, 1]
console.log(func2(list))

// 3. Crea una función que reciba un string y devuelva el número de vocales que contiene

function func3(a){
    let vocales = 0
    for (let value of a){
        if(value=="a"||value=="e"||value=="i"||value=="o"||value=="u"){
         vocales++
        }
    }
    return vocales
}
let mensaje = "Hola mi nombre es Kevin"
console.log(func3(mensaje))

// 4. Crea una función que reciba un array de strings y devuelva un nuevo array con las strings en mayúsculas

function func4(a){
    let list = []
    for(let i = 0; i < a.length; i++){
        list.push(a[i].toUpperCase())
    }
    return list
}
let newlist = ["Kevin", "Keytlin", "Yaque", "Lazaro"]
console.log(func4(newlist))

// 5. Crea una función que reciba un número y devuelva true si es primo, y false en caso contrario

function func5(a){
    if(a<=1){
        return false
    }else if(a==2){
        return true
        
    }
    for(let i=2; i<= Math.sqrt(a); i++){
        if(a%i===0){
            return false
        }
    }
    return true  
}
console.log(func5(6))

// 6. Crea una función que reciba dos arrays y devuelva un nuevo array que contenga los elementos comunes entre ambos

function func6(a,b){
    let list = []
    for(let i of a){
        for(let j of b){
            if(i==j){
                list.push(j)
            }
        }
    }
    return list
}
let prueba1 = ["Kevin","Sosa","Felipe"]
let prueba2 = ["Key","Sosa","Felipe"]
console.log(func6(prueba1,prueba2))

// 7. Crea una función que reciba un array de números y devuelva la suma de todos los números pares

function func7(a){
    let suma = 0
    for(let i of a){
        if(i%2 ==0){
            suma += i
        }
    }
    return suma
}
list = [2, 9, 11, 21, 10, 8, 17, 1]
console.log(func7(list))

// 8. Crea una función que reciba un array de números y devuelva un nuevo array con cada número elevado al cuadrado

function func8(a){
    let cuadrado = []
    for(let i=0; i<a.length; i++){
        cuadrado.push(a[i]**2) 
    }
    return cuadrado
}
list = [1, 2, 3, 4, 5, 6]
console.log(func8(list))

// 9. Crea una función que reciba una cadena de texto y devuelva la misma cadena con las palabras en orden inverso

function func9(a){
    let invertido = ""
    for(let i = a.length -1; i>=0; i--){
        invertido += a[i]
    }
    return invertido
}
list = "Hola mi nombre Kevin"
console.log(func9(list))

// 10. Crea una función que calcule el factorial de un número dado


