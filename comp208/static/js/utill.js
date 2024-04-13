class Util {
    constructor() {
        if (Util.instance) return Util.instance;
        return this.getInstance(...arguments);
    }

    getInstance() {
        var instance = {
            /*
             *   formatTime format time (s) to hour:minutes:seconds
             *   @params  time  required number (s)
             *   
             *   return hour:minutes:seconds string
             */

            formatTime(time) {
                // When there's no time to pass
                if (time === undefined) {
                    this.handlerError(123, {
                        method: 'formate',
                        param: 'time'
                    });
                    return false;
                }
                let _time = Math.floor(time);
                let _minutes = Math.floor(_time / 60);
                let _hours = Math.floor(_minutes / 60);
                let _seconds = _time - (_minutes * 60);

                return (_hours ? this.fillZero(_hours) + ':' : '') + this.fillZero(_minutes - (_hours * 60)) + ':' + this.fillZero(_seconds);
            },
            /*
             *   fillZero for numbers less than 10 to fill 0
             *   @params  num  required number
             *   return '01'.. string
             */
            fillZero(num) {
                // When there is no pass time
                if (num === undefined) {
                    this.handlerError(123, {
                        method: 'fillZero',
                        param: 'num'
                    });
                    return false;
                }
                //This function just gives us a different effect when rendering/displaying, don't manipulate the original data
                return num > 9 ? num : '0' + num;
            },
            errors: {
                123: ({
                    method,
                    param
                }) => {
                    return method + 'function need a param ' + param;
                }
            },
            handlerError(code, options) { //处理报错
                console.error('[until error] message' + this.errors[code](options));
            }
        }
        Util.instance = instance;
        return instance;
    }
}

//In order for this tool to remain available later in a modular environment, it needs to be judged and exposed if it is in a modular environment
//commonJs
if (typeof module === 'object' && typeof module.exports === 'object') {
    module.exports = Util;
}

//AMD
if (typeof define === 'function' && define.amd) {
    define('util', [], function () {
        return Util;
    });
}