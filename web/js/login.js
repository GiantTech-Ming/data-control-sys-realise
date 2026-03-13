window.onload = function(){

    let user = getCookie("user")

    if(user){
        location.href="dashboard.html"
    }

}

function login(){

    let name = document.getElementById("name").value
    let password = document.getElementById("password").value

    let xhr = new XMLHttpRequest()

    xhr.open("POST","http://localhost:5000/login")

    xhr.setRequestHeader("Content-Type","application/json")

    xhr.onreadystatechange=function(){

        if(xhr.readyState===4){

            let res = JSON.parse(xhr.responseText)

            if(res.status==="success"){

                document.cookie="user="+name+";path=/"

                location.href="dashboard.html"

            }else{

                document.getElementById("msg").innerText="登录失败"

            }
        }
    }

    xhr.send(JSON.stringify({
        name:name,
        password:password
    }))
}

function getCookie(name){

    let arr = document.cookie.split(";")

    for(let i=0;i<arr.length;i++){

        let pair = arr[i].trim().split("=")

        if(pair[0]===name){
            return pair[1]
        }
    }

    return null
}