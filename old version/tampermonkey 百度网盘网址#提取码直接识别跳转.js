// ==UserScript==
// @name         百度网盘网址#提取码直接识别跳转
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://pan.baidu.com/*
// @icon         https://www.google.com/s2/favicons?domain=greasyfork.org
// @grant        none
// ==/UserScript==


// 网址格式：
// https://pan.baidu.com/s/xxxxxxx#yyyy
// yyyy是提取码
var address = window.location.href.split('#');
if (address[1]){
    document.getElementById("accessCode").value = address[1];
    document.getElementById("submitBtn").click();
}