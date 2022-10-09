function passwordone(){
    var a =document.getElementById("password");
    var c =document.getElementById("hide1");
    var d =document.getElementById("hide2");
    
    if (a.type === "password"){
        a.type = "text";
        c.style.display = "block";
        d.style.display = "none";
    }
    else{
        a.type = "password";
        c.style.display = "none";
        d.style.display = "block";
    }

}

function passwordtwo(){
    var b =document.getElementById("password2");
    var e =document.getElementById("hide3");
    var f =document.getElementById("hide4");

    if (b.type === "password"){
        b.type = "text";
        e.style.display = "block";
        f.style.display = "none";
    }
    else{
        b.type = "password";
        e.style.display = "none";
        f.style.display = "block";
    }
}