const Button1 = document.getElementById("Button1")
const Button2 = document.getElementById("Button2")
const Pantalla = document.getElementById("Pantalla")
const incPantalla = document.getElementById("incPantalla")
const decPantalla = document.getElementById("decPantalla")


let incremento = 0
let decremento = 0
let pantalla = 0

Button1.addEventListener("click", () => {
    pantalla ++
    Pantalla.textContent = pantalla
    
    if(incremento<=9){
        incremento ++
        incPantalla.textContent = `${incremento} Click`
    }else{
        incremento = 0
        incPantalla.textContent =  `${incremento} Click`
    }
    
})
Button2.addEventListener("click", () => {
    pantalla --
    Pantalla.textContent = pantalla

    if(decremento<=9){
        decremento ++
        decPantalla.textContent =  `${decremento} Click`
    }else{
        decremento = 0
        decPantalla.textContent =  `${decremento} Click`
    }
})