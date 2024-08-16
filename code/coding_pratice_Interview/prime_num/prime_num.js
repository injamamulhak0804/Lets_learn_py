const prime_num = (n) => {
    let flag = 0;
    for(let i = 2; i < n; i++){
        if(n % i == 0){
            flag = 1
        }
    }

    if(flag){
        console.log("The Given number is a prime number");
    }
    else{
        console.log("The Given number is not a Prime  number");    
    }
}

// prime_num(9)