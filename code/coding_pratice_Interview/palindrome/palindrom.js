function palimdrome(value){

    revstr = String(value).split('').reverse().join("")
    if(revstr == value){
        console.log("palindrome");
    }else{
        console.log("Not a palindrome");
    }
}
palimdrome(121)
