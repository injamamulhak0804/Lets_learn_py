const odd_or_even = (num) =>{    
    let count_even = 0, count_odd = 0;
    for(let i = 0; i < num.length; i++){
        if(num[i] % 2 == 0){
            count_even += 1
        }else{
            count_odd += 1
        }
    }
    console.log("Even number is: ", count_even);
    console.log("Odd number is: ", count_odd);
}

// odd_or_even([2, 4, 6, 8, 10, 3, 5, 9])