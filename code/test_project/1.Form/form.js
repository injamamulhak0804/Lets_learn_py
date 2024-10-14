const NameEl = document.getElementById("name")
const EmailEl = document.getElementById("email")
const PasswordEl = document.getElementById("password")
const Button = document.getElementById("btn")
const FillEl = document.querySelector(".fill")
const Email_INC = document.querySelector(".email_inc")
const Password_INC = document.querySelector(".pass_inc")

Button.addEventListener("click", ()=>{
    //get value
    const name = NameEl.value 
    const email = EmailEl.value
    const password = PasswordEl.value

    if(!name || !email || !password){
        FillAllFields()
    }else{
        FillEl.style.visibility = "hidden"
        if(!email.includes("@")){
            Email_INC.style.visibility = "visible"
        }else{
            Email_INC.style.visibility = "hidden"    
        }
        Validation(password)
    }
    
})

function FillAllFields(){
    FillEl.style.visibility = "visible"
}
function Validation(user_pass){    
    const minlength = 8;
    const isUpper = /[A-Z]/.test(user_pass)
    const isLower = /[a-z]/.test(user_pass)
    const isNumber = /\d/.test(user_pass)
    const isSpecial =  /[^\w\s]/.test(user_pass)


    if(!user_pass >= 8 || !isLower || !isUpper || !isNumber || !isSpecial){
        Password_INC.style.visibility = "visible" 
    }else{
        Password_INC.style.visibility = "hidden" 
    }

}