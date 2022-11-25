const btn = document.querySelector("#darkmode");

var isOn = false;

function darkMode () {
    if(!isOn) {
        document.documentElement.setAttribute('data-theme', 'light');
        document.querySelector('#darkmode').innerHTML = 'DARK MODE';
        isOn = true;
    }
    else {
        document.documentElement.setAttribute('data-theme', 'dark');
        document.querySelector('#darkmode').innerHTML = 'LIGHT MODE';
        isOn = false;
    }
}

btn.addEventListener("click", darkMode)
