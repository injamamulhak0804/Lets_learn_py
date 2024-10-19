const Img = document.getElementById("img")
const Left = document.getElementById("left")
const Right = document.getElementById("right")
const path = ["./assets/blog1.png", "./assets/blog2.png", "./assets/blog3.png"]
let index = 1

Img.src = path[index]
Right.addEventListener("click", ()=>{    
    if (index < 2){
        index+=1        
        Img.src = path[index]
    }if(index == 2){
        Right.classList.add("disable")
    }else{
        Left.classList.remove("disable")
    }
})

Left.addEventListener("click", ()=>{    
    if (index > 0){
        index-=1        
        Img.src = path[index]
    }if(index == 0){
        Left.classList.add("disable")
    }else{
        Right.classList.remove("disable")
    }
})

setInterval(()=>{
    index+=1 
    if(index > 2) {
        index=0
    }
    Img.src = path[index]
    Right.classList.remove("disable")
    Left.classList.remove("disable")
    console.log("Index", index);
    
}, 5000)



