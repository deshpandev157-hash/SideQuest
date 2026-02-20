const API = "http://127.0.0.1:5000/api";

// REGISTER
function register(){
    fetch(API + "/auth/register",{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({
            username:document.getElementById("username").value,
            email:document.getElementById("email").value,
            password:document.getElementById("password").value
        })
    })
    .then(res=>res.json())
    .then(data=>{
        alert(data.message);
        window.location="login.html";
    });
}

// LOGIN
function login(){
    fetch(API + "/auth/login",{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({
            email:document.getElementById("email").value,
            password:document.getElementById("password").value
        })
    })
    .then(res=>res.json())
    .then(data=>{
        localStorage.setItem("token",data.token);
        alert("Login successful!");
        window.location="index.html";
    });
}
