const passwordStrength = (input) =>{
    let strength = 0
    const isUpper = /[A-Z]/.test(input) 
    const isLower = /[a-z]/.test(input) 
    const isDigit = /\d/.test(input)
    const isSpecial = /[^\w\s]/.test(input)
    const minlenth = 8
    
    if(!input.length >= minlenth){
        strength += 1
    }
    if(!isUpper){
        strength += 1
    }
    if(!isLower){
        strength += 1
    }
    if(!isDigit){
        strength += 1
    }
    if(!isSpecial){
        strength += 1
    }
    return strength
}

const strength = passwordStrength("password12@3P") // 1
// console.log(strength);


// atleast 8 character length
// Uppercase
// lowerCase
// numbers
// special Characters

// In optimize way


const optimizePasswordStrength = (input) =>{
    // let strength = 0
    const requiremensts = [
        input.length < 8, // false
        !/[a-z]/.test(input), //false
        !/[A-Z]/.test(input), //false
        !/\d/.test(input), // false
        !/[^\w\s]/.test(input), //false
    ]
    const str = requiremensts.filter((items)=> items==true)
    console.log(str.length);
    
}
// optimizePasswordStrength("@12Aasasd")

// optimize in more way

const optimizeMorePasswordStrength = (input) =>{
    // let strength = 0
    const requiremensts = [
        input.length >= 8, // true
        /[a-z]/.test(input), //true
        /[A-Z]/.test(input), //true
        /\d/.test(input), // true
        /[^\w\s]/.test(input), //true
    ]
    const str = requiremensts.reduce((count, valid)=>(count + (valid ? 0 : 1)), 0)
    console.log(str);
    
}
optimizePasswordStrength("Password123@")
