const Kth_largest_element = (arr) =>{
    let kth = 0;
    for(let i = 0; i < arr.length; i++){
        if(arr[i] > kth){
            kth = arr[i]
        }
    }
    console.log("Kth_largest_element is: ", kth);
    
}
// Kth_largest_element([234,234,89,23,567,45,123])