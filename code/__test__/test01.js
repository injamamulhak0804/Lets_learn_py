const passwordStrengthInTest = (input) =>{
    let r_str = ""
    for (let i = input.length - 1; i >= 0; i--){
        r_str+=input[i];
    }
    const result = input === r_str ? "Palindrome" : "Not a Palindrome"
    console.log(result);
    
}
// passwordStrengthInTest("mame")