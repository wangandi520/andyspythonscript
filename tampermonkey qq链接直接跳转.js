// ==UserScript==
// @name         qq链接直接跳转
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       andy
// @match        https://c.pc.qq.com/*
// @grant        none
// ==/UserScript==

var getUrl = document.querySelector('#url').innerText
window.location.href = getUrl;