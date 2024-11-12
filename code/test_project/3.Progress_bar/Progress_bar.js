const inputEl = document.getElementById("input")
const btnEl = document.getElementById("btn")
const barEl = document.getElementById("bar")
const errEl = document.getElementById("error")

let input_value = 100
btnEl.addEventListener("click", ()=>{
    input_value = inputEl.value 
    if(input_value <= 100){
        barEl.innerText = input_value + "%"
        barEl.style.width = `${input_value}%`
        errEl.innerText = ""
    }else{
        errEl.innerText = "Invalid credentials"
    }
})
barEl.innerText = input_value + "%"
barEl.style.width = `${input_value}%`
