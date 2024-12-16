// ==UserScript==
// @name         www.moeshare.cc跳转到moeshare.cc
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://moeshare.cc/*
// @match        https://www.moeshare.cc/*
// @icon         https://www.google.com/s2/favicons?domain=moeshare.cc
// @grant        none
// ==/UserScript==

var getUrl = window.location.href
if (getUrl.substr(0,11) == "https://www"){
    window.location.href = "https://moeshare.cc" + getUrl.substr(23,getUrl.length);
}
/**
if (getUrl.substr(0,11) == "https://moe"){
    window.location.href = "https://www.moeshare.cc" + getUrl.substr(19,getUrl.length);
}
**/