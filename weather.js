const apiKey = "af1c47118ac9f9defffe6d12437bc3a0";
const apiUrl = "https://api.openweathermap.org/data/2.5/weather?units=metric&q=bangalore";

async function checkWeather(){
    const response = await fetch(apiUrl + '&appid=${apiKey}');
    var data = await response.json()

    console.log(data);

    document.querySelector(".city").innerHTML = data.name;
    document.querySelector(".temp").innerHTML = data.main.temp + "°c";
    document.querySelector(".humidty").innerHTML = data.main.humidty + "%";
    document.querySelector(".wind").innerHTML = data.wind.speed + " km/h" ; 
}


checkWeather();