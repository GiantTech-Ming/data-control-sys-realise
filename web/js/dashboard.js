let chart;

window.onload=function(){

    checkLogin();

    initChart();

    loadData();

    setInterval(loadData,2000);
}

function checkLogin(){

    if(!document.cookie.includes("user")){
        location.href="login.html";
    }
}

function logout(){

    document.cookie="user=; expires=Thu, 01 Jan 1970 00:00:00";
    location.href="login.html";
}

function loadData(){

    let xhr=new XMLHttpRequest();

    xhr.open("GET","data/sensor.json");

    xhr.onreadystatechange=function(){

        if(xhr.readyState===4 && xhr.status===200){

            let data=JSON.parse(xhr.responseText);

            updateUI(data);
        }
    }

    xhr.send();
}

function updateUI(data){

    document.getElementById("temp").innerText=data.temperature;
    document.getElementById("hum").innerText=data.humidity;

    document.getElementById("motor").innerText=data.motor?"运行":"停止";

    document.getElementById("buzzer").innerText=data.buzzer?"开启":"关闭";

    document.getElementById("status").innerText=data.status;

    document.getElementById("suggest").innerText=data.suggest;

    chart.data.labels.push(new Date().toLocaleTimeString());
    chart.data.datasets[0].data.push(data.temperature);

    if(chart.data.labels.length>10){
        chart.data.labels.shift();
        chart.data.datasets[0].data.shift();
    }

    chart.update();
}

function initChart(){

    let ctx=document.getElementById("chart");

    chart=new Chart(ctx,{
        type:"line",
        data:{
            labels:[],
            datasets:[
                {
                    label:"温度变化",
                    data:[],
                    borderColor:"green",
                    fill:false
                }
            ]
        }
    });
}