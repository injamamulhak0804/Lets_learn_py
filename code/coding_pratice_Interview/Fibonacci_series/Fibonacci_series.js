const Fibonacci_series = (num) => {
    let a = 0, b = 1, c = 0, n = num;
    console.log(a,b);
    n = n - 2
    while( n > 0){
        c = a + b;
        console.log(c);
        a = b
        b = c
        n--
    }
}

const Fibonacci_series2 = (num) => {
    let arr = [0, 1]
    for(let i = 2; i < num; i++){
        arr[i] = arr[i - 1] + arr[i - 2]
    }
    console.log(arr);
}

// Fibonacci_series2(10)

