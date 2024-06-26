// playback target
let audio = document.querySelector('#ado')
// play button
const _audio = document.querySelector('._audio')
const _voice = document.querySelector('._voice')

// Audio Settings
audio.src = "./media/小さな恋のうた.mp3"
audio.controls = false
audio.loop = true
audio.volume = 0.3











// Playback start and pause and related icon font changes
function bofang() {
    if (audio.paused) {
        audio.play()
        _audio.classList.remove('icon-bofang')
        _audio.classList.add('icon-zanting')
    } else {
        audio.pause()
        _audio.classList.remove('icon-zanting')
        _audio.classList.add('icon-bofang')
    }
}

// Mute or not mute and related icon font modification
_voice.addEventListener('click', () => {
    if (audio.muted) {
        audio.muted = false
        _voice.classList.remove('icon-yinliangguanbi')
        _voice.classList.add('icon-yinliangkai')
    } else {
        audio.muted = true
        _voice.classList.remove('icon-yinliangkai')
        _voice.classList.add('icon-yinliangguanbi')
    }
})

// The initialisation function is called once.
changeSong()

// Wrapping the audio initialisation function
function changeSong() {
    // Get Audio Duration
    if (audio != null) {
        audio.load()
        audio.oncanplay = function () {
            let duraTime = document.querySelector('.duraTime')
            duraTime.innerHTML = transTime(audio.duration)
        }
    }

    // Formatting Time Format
    function transTime(time) {
        let duration = parseInt(time)
        let minute = parseInt(duration / 60)
        let sec = (duration % 60) + ''
        let isM0 = ':'
        if (minute == 0) {
            minute = '00'
        } else if (minute < 10) {
            minute = "0" + minute
        }
        if (sec.length == 1) {
            sec = "0" + sec
        }
        return minute + isM0 + sec
    }

    // hourly rate bar
    const progress = document.querySelector(".progress");
    const slide = document.querySelector(".slide");
    const fill = document.querySelector(".fill")
    audio.ontimeupdate = function () {
        let l = (audio.currentTime / audio.duration) * 100;
        slide.style.left = l + "%";
        fill.style.width = l + "%";
        if (audio.currentTime == 0) {
            slide.style.left = "0%";
        }
        const currentTime = document.querySelector(".currentTime");
        currentTime.innerHTML = transTime(parseInt(audio.currentTime));
        const duraTime = document.querySelector(".duraTime");
        duraTime.innerHTML = transTime(audio.duration);
    };

    // Progress bar drag
    slide.onmousedown = function (e) {
        let x = e.clientX - this.offsetLeft
        document.onmousemove = function (e) {
            let jlx = ((e.clientX - x) / progress.clientWidth) * 100
            if (jlx <= 100 && jlx >= 0) {
                slide.style.left = jlx + "%"
            }
            audio.currentTime = (jlx / 100) * audio.duration
        }
        document.onmouseup = function () {
            document.onmousemove = null
            document.onmouseup = null
        }
    }
    slide.ontouchstart = function (e) {
        let x = e.targetTouches[0].clientX - this.offsetLeft
        document.ontouchmove = function (e) {
            let jlx = ((e.targetTouches[0].clientX - x) / progress.clientWidth) * 100
            if (jlx <= 100 && jlx >= 0) {
                slide.style.left = jlx + '%'
            }
            audio.currentTime = (jlx / 100) * audio.duration
        }
        document.ontouchend = function (e) {
            document.ontouchmove = null
            document.ontouchend = null
        }
    }
}

// right_box > .navigation Modify the style of right_box navigation bar section1

const items = document.querySelectorAll('.navigation li')
function setActive() {
    items.forEach((items) => {
        items.classList.remove('active')
    })
    this.classList.add('active')
    current_tag.innerText = this.innerText
}

items.forEach((items) => {
    items.addEventListener('click', setActive)
})

// Get recommended songs   Song cut function
const image = document.querySelector('._img')
const recm_list = document.querySelectorAll('.recm_list ul li')
const audio_list = ['夜驱', 'Call your name', 'rain', 'アムリタ', '群青','oddtaxi','小さな恋のうた']
const image_list = ['夜驱', 'callYourName', 'rain', '翼年代', '群青','oddtaxi','小さな恋のうた']
// ftleft After cutting the song, the corresponding picture song title and artist name need to be switched.
const songName = document.querySelector('.songName')
const singer = document.querySelector('.singer')
const songAndSinger_list = [
    ['夜に駆ける','YOASOBI'],
    ['Call your name','李阿亚'],
    ['rain','Aimer'],
    ['アムリタ','牧野由依'],
    ['群青','YOASOBI'],
	['oddtaxi','KISAlaki'],
	['小さな恋のうた','MONGOL800']
]

for (let i = 0; i < recm_list.length; i++) {
    recm_list[i].addEventListener('click', function() {
        audio.src = "./audio/" + audio_list[i] + ".mp3"
        image.src = "./image/main/" + image_list[i] + ".jpg"
        songName.innerHTML = songAndSinger_list[i][0] + '<i class="iconfont icon-aixin"></i>'
        singer.innerHTML = songAndSinger_list[i][1]
        changeSong()
        audio.play()
    })
}


let currentIndex = audio_list.indexOf('小さな恋のうた');


function playPrev() {
    // Calculate the index of the previous song
    currentIndex = (currentIndex - 1 + audio_list.length) % audio_list.length;
    // Update and play the selected song
    updateAndPlayCurrentSong();
}

function playNext() {
    // Calculate the index of the next song
    currentIndex = (currentIndex + 1) % audio_list.length;
    // Update and play the selected song
    updateAndPlayCurrentSong();
}

function updateAndPlayCurrentSong() {
    // Updates audio source, picture and song information based on the current index
    audio.src = "./audio/" + audio_list[currentIndex] + ".mp3"
    image.src = "./image/main/" + image_list[currentIndex] + ".jpg"
    songName.innerHTML = songAndSinger_list[currentIndex][0] + '<i class="iconfont icon-aixin"></i>'
    singer.innerHTML = songAndSinger_list[currentIndex][1]
    changeSong()
    audio.play()
}
