const Amstrong_number = (n) =>{
    let r, n1, sum = 0;
    n1 = n;
    i = 3
    while(n > 0){
        r = n % 10;
        sum = sum + r*r*r*r
        n = Math.trunc(n/10)
    }
    if(n1 == sum){
        console.log("Amstrong number");
    }else{
        console.log("Not a Amstrong number");
    }
}

// Amstrong_number(8208)