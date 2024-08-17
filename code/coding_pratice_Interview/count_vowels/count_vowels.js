const count_vowels = (value) =>{
    count = 0;
    for(let i = 0; i < value.length; i++){
        if(value.charAt(i) == "a" || value.charAt(i) == "e" || value.charAt(i) == "i" || value.charAt(i) == "o" || value.charAt(i) == "u"){
            count += 1
        }
    }   
    console.log(count);
}
    
// count_vowels("education")