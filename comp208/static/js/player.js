// Creating a Music Player  Class Singleton Pattern
class Player {
    constructor() {
        if (Player.instance) {
            return Player.instance;
        }

        return this.getInstance(...arguments);
    }

    // Build Examples
    getInstance() {
        let instance = new PlayerCreator(...arguments);
        // Hook up the constructed instance to the Player class
        Player.instance = instance;
        return instance;
    }
}

// Song Information
class Musics {

    // constructor
    constructor() {
		// Bottom Song List Container
	   this.song_index = 0;
	   this.loop_mode = 0;
	   this.audio = document.querySelector('.music-player__audio');
	   this.song_list = $('.music__list_content');
	   this.render_doms = {
            title: $('.music__info--title'),
            singer: $('.music__info--singer'),
            image: $('.music-player__image img'),
            blur: $('.music-player__blur')
        };
        this.getSongs()
    }

    // Get song list
    getSongs() {
        let mp3list = []

        let csrf = $('input[name="csrfmiddlewaretoken"]').val()

        $.ajax({
                type: 'POST',
                url: "/media_list",
                data: {id:1, csrfmiddlewaretoken:csrf},
                dataType: 'json',
                success: function (data) {
					// Assign mp3list to this.songs
					this.songs = data.list;
					// Call the method that renders the song list
					this.renderSongList();
                }.bind(this),
                error: function (e) {
                    console.log("ERROR : ", e);
               }
        });
    }
	// Generating Playlists
    renderSongList() {
        let _str = '';
        this.songs.forEach((song, i) => {
            _str += `<li class="music__list__item">${song.title}</li>`
        });
        this.song_list.html(_str);
    }

	// Render the view according to the song
    renderSongStyle() {
        let {
            title,
            singer,
            songUrl,
            imageUrl
        } = this.getSongByNum(this.song_index);
        this.audio.src = songUrl;
        this.render_doms.title.html(title);
        this.render_doms.singer.html(singer);
        this.render_doms.image.prop('src', imageUrl);
        this.render_doms.blur.css('background-image', 'url("' + imageUrl + '")');

        // Class name of the item in the toggle list play
        this.song_list.find('.music__list__item').eq(this.song_index).addClass('play').siblings().removeClass('play');
    }
    // Methods to get songs by index
    getSongByNum(index) {
        return this.songs[index];
    }

	// Changing the song index
    changeSongIndex(type) {
        if (typeof type === 'number') {
            this.song_index = type;
        } else {
            if (this.loop_mode === 0) {
                // list cycle
                this.song_index += type === 'next' ? 1 : -1;
                if (this.song_index > this.songs.length - 1) this.song_index = 0;
                if (this.song_index < 0) this.song_index = this.songs.length - 1;
            } else if (this.loop_mode === 1) {
                // random playback
                let _length = this.songs.length;
                let _random = Math.floor(Math.random() * _length);
                for (let i = 0; i < 10000; i++) { // If the random number is itself, then continue to randomise
                    if (this.song_index == _random) {
                        _random = Math.floor(Math.random() * _length);
                    } else {
                        this.song_index = _random;
                        break;
                    }
                }
            } else if (this.loop_mode === 2) {
                this.song_index = this.song_index;
            }
        }
    }

	// Switching Songs
    changeSong(type) {
        // Change Index
        this.changeSongIndex(type);
        // Record the state before cutting the song
        let _is_pause = this.audio.paused;
        // Changing the view display after a song cut
        this.renderSongStyle();
        // If it was playing before the song was cut, keep it playing
        if (!_is_pause) this.audio.play();
    }
}

//The class that actually builds the player
class PlayerCreator {
    constructor() {
        // Audio dom element, because many api's require native audio calls, so don't use jq to get
        this.audio = document.querySelector('.music-player__audio');
        // this.audio.muted = true; // Control Mute
        this.audio.volume = 0.5;

        //artifact
        this.util = new Util();
		this.musics = new Musics(); //Song Information

        this.song_index = 0; // Index of currently playing songs
        this.loop_mode = 0; // 1 2
        // Bottom Song List Container
        this.song_list = $('.music__list_content');

        // The dom group to be rendered when switching songs
        this.render_doms = {
            title: $('.music__info--title'),
            singer: $('.music__info--singer'),
            image: $('.music-player__image img'),
            blur: $('.music-player__blur')
        };

        // The dom group to be rendered when the sound is disabled
        this.ban_dom = {
            control__btn: $('.control__volume--icon')
        };

        // Time display container
        this.render_time = {
            now: $('.nowTime'),
            total: $('.totalTime')
        };

        // gramophone record
        this.disc = {
            image: $('.music-player__image'),
            pointer: $('.music-player__pointer')
        };
        // Player initialisation
        this.init();
    }
    // Initialisation functions
    init() {
        this.bindEventListener();
    }

    // Binding various events
    bindEventListener() {
        // play button
        this.$play = new Btns('.player-control__btn--play', {
            click: this.handlePlayAndPause.bind(this)
        });
        // previous song
        this.$prev = new Btns('.player-control__btn--prev', {
			click: () => this.musics.changeSong('prev')
        });
        // next song
        this.$next = new Btns('.player-control__btn--next', {
			click: () => this.musics.changeSong('next')
        });
        // recurrent mode
        this.$mode = new Btns('.player-control__btn--mode', {
            click: this.changePlayMode.bind(this)
        });
        // prohibitory note
        this.$ban = new Btns('.control__volume--icon', {
            click: this.banNotes.bind(this)
        });
        // list click
        this.song_list.on('click', 'li', (e) => {
            let index = $(e.target).index();
            this.musics.changeSong(index);
        });

        // Volume control audio tab volume vlouem property control 0-1
        new Progress('.control__volume--progress', {
            min: 0,
            max: 1,
            value: this.audio.volume,
            handler: (value) => { //When changing progress
                this.audio.volume = value;
            }
        });


        // Song Progress this.audio.duration
        // Can be triggered when playing (basic information about the song is already obtained)
        this.audio.oncanplay = () => {
            // Avoiding Repeated Instantiation
            if (this.progress) {
                this.progress.max = this.audio.duration; //Update duration after switching songs
                this.render_time.total.html(this.util.formatTime(this.audio.duration));
                return false;
            }
            this.progress = new Progress('.player__song--progress', {
                min: 0,
                max: this.audio.duration,
                value: 0,
                handler: (value) => {
                    this.audio.currentTime = value;
                }
            });
            // Adjustment of total duration
            this.render_time.total.html(this.util.formatTime(this.audio.duration));
        };

        // It will be triggered continuously during playback
        this.audio.ontimeupdate = () => {
            this.progress.setValue(this.audio.currentTime);
            // Adjusting the current duration
            this.render_time.now.html(this.util.formatTime(this.audio.currentTime));
        };

        // When the song finishes playing
        this.audio.onended = () => {
            this.musics.changeSong('next');
            // Play it, change the song and replay it
            this.audio.play();
        }

    }

    // Playback Pause Control
    handlePlayAndPause() {
        let _o_i = this.$play.$el.find('i');
        // This.audio.paused has a value of true, which means it is currently not playing.
        if (this.audio.paused) { // It's paused. Needs to play.
            this.audio.play();
            _o_i.removeClass('icon-play').addClass('icon-pause');
            this.disc.image.addClass('play');
            this.disc.pointer.addClass('play')
        } else {
            this.audio.pause();
            _o_i.addClass('icon-play').removeClass('icon-pause');
            this.disc.image.removeClass('play');
            this.disc.pointer.removeClass('play');
        }
    }

    // Changing the cycle mode
    changePlayMode() {
        this.loop_mode++;
        if (this.loop_mode > 2) this.loop_mode = 0;
        this.renderPlayMode();
    }

    // Changing the button style
    renderPlayMode() {
        let _classess = ['loop', 'random', 'single'];
        let _o_i = this.$mode.$el.find('i');
        // prop change some tag's own attributes attr change some tag's custom attributes
        _o_i.prop('class', 'iconfont icon-' + _classess[this.loop_mode])
    }

    // song duration
    songTime() {
        let totalMinute = parseInt(this.audio.duration / 60) < 10 ? "0" + parseInt(this.audio.duration / 60) : parseInt(this.audio.duration / 60);
        let totalSecond = parseInt(this.audio.duration % 60) < 10 ? "0" + parseInt(this.audio.duration % 60) : parseInt(this.audio.duration % 60);
        $('.totalTime').text(totalMinute + ':' + totalSecond);
    }

    // silence
    banNotes() {
        let _o_i = this.$ban.$el.find("i");
        if (this.audio.muted == true) { // Enable if sound is disabled
            this.audio.muted = false;
            _o_i.removeClass('icon-muted').addClass('icon-volume');
        } else {
            this.audio.muted = true;
            _o_i.removeClass('icon-volume').addClass('icon-muted');
        }
    }
}

// progress bar
class Progress {
    constructor(selector, options) {
        $.extend(this, options);
        // Mounting incoming arguments to this
        this.$el = $(selector);
        this.width = this.$el.width();
        this.init();
    }

    // Progress bar initialisation
    init() {
        this.renderBackAndPointer();
        this.bindEvents();
        this.drag();
        this.value;
        this.changeDOMStyle(this.width * this.value);
    }
    // Rendering back and pointer for progress bars
    renderBackAndPointer() {
        this.$back = $('<div class="back">');
        this.$pointer = $('<div class="pointer">');

        this.$el.append(this.$back);
        this.$el.append(this.$pointer);
    }

    setValue(value) { // Active call, pass in value, set progress bar style
        let _distance = this.width * value / (this.max - this.min);
        this.changeDOMStyle(_distance);
    }

    drag() {
        let ele = this.$pointer;
        let father = this.$el;
        let flag = false; // Whether the mouse clicks
        ele.mousedown((e) => {
            flag = true;
            let mousePos = {
                x: e.offsetX
            };
            $(document).mousemove((e) => {
                if (flag === true) {
                    let _left = e.clientX - father.offset().left - mousePos.x;
                    let _distance = Math.max(0, Math.min(_left, father.outerWidth(false) - ele.outerWidth(false)))
                    let _ratio = _distance / father.outerWidth(false);
                    let _value = _ratio * (this.max - this.min); // Current volume value
                    this.changeDOMStyle(_distance);
                    this.handler(_value); // After changing the progress, execute the callback
                }
            })
        });
        $(document).mouseup(() => {
            flag = false;
        })

    }

    bindEvents() { // Change on mouse click
        this.$el.click((e) => {
            let _x = e.offsetX; // Mouse distance to the left of the element
            let _ratio = _x / this.width;
            let _value = _ratio * (this.max - this.min); // Current volume value
            this.changeDOMStyle(_x);
            this.handler(_value); // After changing the progress, execute the callback
        })
    }
    // Change pointer and back
    changeDOMStyle(distance) {
        this.$back.width(distance + 7 == 7 ? 0 : distance + 7);// When progress is 0 change the progress bar background to 0 otherwise add the length of the progress button
        this.$pointer.css('left', distance + 'px');
    }
}


// pushbutton class
class Btns {
    constructor(selector, handlers) {
        this.$el = $(selector); // elemental
        this.bindEvents(handlers);
    }
    bindEvents(handlers) { // bind an event
        for (const event in handlers) {
            // Ensure that key-value pairs are present in the object when using values
            if (handlers.hasOwnProperty(event)) {
                this.$el.on(event, handlers[event]);
            }
        }
    }
}
new Player();