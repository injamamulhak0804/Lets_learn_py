const reverseArray = (arr)=>{
    // const ans = arr.reverse() // with plugin
    const ans1 = [] 
    
    //without plugin
    for(let i = arr.length; i > 0; i--){
        ans1.push(i)
    }

    const ans3 = arr.slice().reverse()
    
    console.log(ans3);
}

// reverseArray([1,2,3])