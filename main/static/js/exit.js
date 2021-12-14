window.addEventListener("load", load_exit);


function load_exit(){
   
   let btExit = document.querySelector('#exit')
   btExit.addEventListener('click',event=>{
    
    fetch(`http://localhost:8000/exit`)
    window.location.replace("/");
    
   })
}