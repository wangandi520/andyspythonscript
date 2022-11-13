// ==UserScript==
// @name 音频应用替换IP
// @namespace http://tampermonkey.net/
// @version 0.1
// @Description try to take over the world!
// @Author xup
// @match http://43.225.39.42/*
// @grant none
// ==/UserScript==

var getLinks = document.getElementsByTagName('a');
for(var i=0; i< getLinks.length; i++){
    if(getLinks[i].href.indexOf("http://www.audiobar.net.cn")!==-1) {
        getLinks[i].href = decodeURIComponent(getLinks[i].href.replace('http://www.audiobar.net.cn', 'http://43.225.39.42'));
    }
}