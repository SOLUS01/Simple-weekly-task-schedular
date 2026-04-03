function animateProgress(percent){

let circle = document.getElementById("progressCircle")

let circumference = 502

let offset = circumference - (percent/100)*circumference

let current = circumference

let step = (circumference-offset)/40

let animation = setInterval(()=>{

current -= step

circle.style.strokeDashoffset = current

if(current <= offset){

clearInterval(animation)

}

},20)

}



function toggleTheme(){

document.body.classList.toggle("dark")

}