const passwordStrengthInTest = (input) =>{
    //ODD or Even
    // const result = input%2 == 0 ? "even" : "odd";
    // console.log(result);

    // const rev_str = input.toLowerCase().split("").reverse().join("")
    // if(input.toLowerCase() == rev_str){
    //     console.log("palindrome");
    // }else{
    //     console.log("Not a palindrome");       
    // }

    //Without plugin
    let r_str = ""
    for (let i = input.length - 1; i >= 0; i--){
        r_str+=input[i];
    }
    const result = input === r_str ? "Palindrome" : "Not a Palindrome"
    console.log(result);
    
}
passwordStrengthInTest("mame")