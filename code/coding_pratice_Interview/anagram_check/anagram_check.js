const anagram_check = (s1, s2) =>{
    let s1len = s1.length
    let s2len = s2.length
    let count = 0
    console.log(s1);
    
    if(s1len === s2len){
        for(let i = 0; i < s1len; i++){
            for(let j = 0; j < s2len; j++){
                if(s1[i] == s2[j]){
                    count++
                    break;
                }
            }
        }
        if(s1len == count){
            console.log("Its a anagram");
            
        }else{
            console.log("Its not a anagram");
            
        }
    }else{
        console.log("Not an anagram value");
    }
}

// anagram_check("zamamu", "mamjaz")