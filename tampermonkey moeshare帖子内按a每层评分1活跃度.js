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



function pingfen(eachScore,i,count){
    eachScore[i - 1].click();
    console.log('正在评分第' + i + '楼');
    setTimeout(function(){
        var my = document.querySelector('#c_model');
        my.querySelector('select').selectedIndex = 1;
        my.querySelector('input').value = 1;
        setTimeout(function(){
            document.querySelector('#box_container .btn2 button').click();
            count = count + 1;
            console.log('评分完毕，活跃度 +' + count);
        }, 1000);
    }, 1000);
}

document.onkeydown = function(){
    var eachScore = document.getElementsByClassName('r-score');
    var i = 1;
    var count = 0;
    //在帖子内，按a键开始自动评分
    if (event.keyCode == 65){
        setInterval(function(){
            pingfen(eachScore,i,count);
            i = i + 1;
        }, 5000);
    }
}
