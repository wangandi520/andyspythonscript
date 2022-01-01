// ==UserScript==
// @name         moeshare auto score
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://moeshare.cc/*
// @icon         https://www.google.com/s2/favicons?domain=moeshare.cc
// @grant        none
// ==/UserScript==


var i = -1;
document.onkeydown = function(){
    var eachScore = document.getElementsByClassName('r-score');
    if (event.keyCode == 65){
        setTimeout(
            function()
            {
                eachScore[i].click();
                console.log('Floor = ' + i);
                setTimeout(
                    function()
                    {
                        var my = document.querySelector('#c_model');
                        my.querySelector('select').selectedIndex = 1;
                        my.querySelector('input').value = 1;
                        setTimeout(
                            function()
                            {
                                document.querySelector('#box_container .btn2 button').click();
                            }, 1000);
                    }, 1000);
            }, 1000);
    }
i = i + 1;
}
