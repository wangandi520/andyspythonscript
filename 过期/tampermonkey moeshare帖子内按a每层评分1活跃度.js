// ==UserScript==
// @name         moeshare帖子内按a每层评分1活跃度
// @namespace    http://tampermonkey.net/
// @version      0.2
// @description  try to take over the world!
// @author       https://github.com/wangandi520/andyspythonscript
// @match        https://moeshare.cc/read*
// @match        https://www.moeshare.cc/read*
// @icon         https://www.google.com/s2/favicons?domain=moeshare.cc
// @grant        none
// ==/UserScript==



function pingfen(eachScore,i){
    eachScore[i - 1].click();
    console.log('正在评分第' + i + '楼');
    setTimeout(function(){
        var my = document.querySelector('#c_model');
        setTimeout(function(){
            document.querySelector('#box_container .btn2 button').click();
        }, 1000);
    }, 1000);
}

document.onkeydown = function(){
    var eachScore = document.getElementsByClassName('r-score');
    var i = 1;
    var myinterval;
    //在帖子内，按a键开始自动评分
    if (event.keyCode == 65){
        myinterval = setInterval(function(){
            pingfen(eachScore,i);
            i = i + 1;
            if (i > 10){
                clearInterval(myinterval);
                console.log('评分完成');
            }
        }, 5000);
    }
}
