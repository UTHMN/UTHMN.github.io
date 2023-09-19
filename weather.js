const apiKey = "d05209b7b4075f46ee62255e9a0bdb95";
const apiUrl = "https://api.openweathermap.org/data/2.5/weather?units=metric&q=";

const searchBox = document.querySelector(".search input")
const searchBtn = document.querySelector(".search button")
const WeatherIcon = document.querySelector(".weather-icon");

console.log("hehehe here is my very secret api key: " + apiKey)

async function checkWeather(city){
    const response = await fetch(apiUrl + city + '&appid=${apiKey}');
    var data = await response.json()

    console.log(data);

    document.querySelector(".city").innerHTML = data.name;
    document.querySelector(".temp").innerHTML = Math.round(data.main.temp) + "°c";
    document.querySelector(".humidty").innerHTML = data.main.humidty + "%";
    document.querySelector(".wind").innerHTML = data.wind.speed + " km/h" ; 

    if(data.weather[0].main == "Clouds"){
        WeatherIcon.src = "weatherimg/clouds.png";
    }
    else if(data.weather[0].main == "Clear"){
        WeatherIcon.src = "weatherimg/clear.png";
    }
    else if(data.weather[0].main == "Rain"){
        WeatherIcon.src = "weatherimg/rain.png";
    }
    else if(data.weather[0].main == "Drizzle"){
        WeatherIcon.src = "weatherimg/mist.png";
    }

    document.ATTRIBUTE_NODE.querySelector(".weather").style.display = "block";

}

searchBtn.addEventListener("click", ()=>{
    checkWeather(searchBox.value);
})

checkWeather();