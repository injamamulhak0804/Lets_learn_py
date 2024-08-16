const sum_of_digits = (n) =>{
    let sum = 0;
    while(n > 0){
        let r = n % 10;
        sum += r;
        n = Math.trunc(n / 10)
    }
    console.log("sum_of_digits: ", sum);
    
}

// sum_of_digits(123)