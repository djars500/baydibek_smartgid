

let player = document.getElementById('mainPlayer'),
    playBtn = document.getElementById('playBtn'),
    path = '/static/images/icons-weather/',
    weatherIcon = document.getElementById('weatherIcon'),
    weatherText = document.getElementById('weatherText');



function playAndPause(e) {
    if (player.paused) {
        player.play();
        playBtn.children[0].classList.add('deactive');
        playBtn.children[0].classList.remove('active');
        playBtn.children[1].classList.add('active');
        playBtn.children[1].classList.remove('deactive');
        console.log(playBtn.children);
        console.log('played');
    }
    else {
        player.pause();
        playBtn.children[1].classList.add('deactive');
        playBtn.children[1].classList.remove('active');
        playBtn.children[0].classList.add('active');
        playBtn.children[0].classList.remove('deactive');
        console.log('paused');
    }
}

if (playBtn){
    playBtn.addEventListener('click', playAndPause)
}



let cityName = 'Shayan';
let APIkey = '904b90fbf88a2f026a9029ba82b7009c';
let url = `http://api.openweathermap.org/data/2.5/weather?q=${cityName}&appid=${APIkey}`;
fetch(url)
.then(response => response.json())
.then((result) => {
    let temp = parseInt(result.main.temp-273.15);
    let icon = path+`${result.weather[0].icon}.png`;

    weatherIcon.setAttribute('src', icon);
    weatherText.innerText = `+${temp}°`
    
});

let weatherInterval = setInterval(function(){
    let cityName = 'Shayan';
    let APIkey = '904b90fbf88a2f026a9029ba82b7009c';
    let url = `http://api.openweathermap.org/data/2.5/weather?q=${cityName}&appid=${APIkey}`;
    fetch(url)
    .then(response => response.json())
    .then((result) => {
        let temp = parseInt(result.main.temp-273.15);
        let icon = path+`${result.weather[0].icon}.png`;

        weatherIcon.setAttribute('src', icon);
        weatherText.innerText = `+${temp}°`
        
    });
}, 60*60*3 )



let isYes = document.getElementById('date')

if (isYes) {



    let today = new Date();
    isYes.innerHTML = today.getUTCDay() + "." + today.getUTCMonth() + "." + today.getUTCFullYear();

    let time = setInterval(function() {
        let date = new Date();
        document.getElementById("time").innerHTML = (date.getHours() + ":" + date.getUTCMinutes() + ":" + date.getUTCSeconds());
      }, 1000);
    
    

    let date = setInterval(function() {
        let date = new Date();
        document.getElementById("date").innerHTML = (date.getUTCDay() + "." + date.getUTCMonth() + "." + date.getUTCFullYear());
    }, 60*120);
        
        
    
}








const swiper = new Swiper('.swiper-container', {
    // Optional parameters
    direction: 'horizontal',
    loop: true,
  
    // If we need pagination
    pagination: {
      el: '.swiper-pagination',
    },
  
    // Navigation arrows
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
    breakpoints: {
        
        // when window width is >= 640px
        700: {
          slidesPerView: 2,
          spaceBetween: 40
        }
      },
    slidesPerView: 1,
        spaceBetween: 30,
        centeredSlides: true,
    // And if we need scrollbar
    scrollbar: {
      el: '.swiper-scrollbar',
    },
  });