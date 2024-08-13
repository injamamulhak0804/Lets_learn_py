const reverse_string = (str) =>{
    // Method1 plugin
    // const ans = str.split('').reverse().join('')
    
    // Method2 without plugin
    let ans2 = ""
    for (let i = str.length - 1; i >= 0; i--){
        ans2 += str[i]
    }

    console.log(ans2);
}
// reverse_string("hello")
