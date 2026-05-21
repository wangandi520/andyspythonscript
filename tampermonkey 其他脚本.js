// ==UserScript==
// @name         其他脚本
// @namespace    http://tampermonkey.net/
// @version      2026-05-21
// @description  其他脚本
// @author       wangandi520
// @match        https://rodata.zhaouc.com/*
// @match        https://ro.zhaouc.com/*
// @grant        none
// ==/UserScript==

// 塔人仙境传说网页禁止播放音乐
if (window.location.href.startsWith('https://rodata.zhaouc.com/')) {
    document.querySelector('.top-music')?.remove();
}
if (window.location.href.startsWith('https://ro.zhaouc.com/')) {
    document.querySelector('.top-music')?.remove();
}