// ==UserScript==
// @name         网页自动跳转
// @namespace    http://tampermonkey.net/
// @version      2025-05-08
// @description  网页自动跳转
// @author       wangandi520
// @match        https://jump2.bdimg.com/safecheck*
// @match        https://c.pc.qq.com/*
// @grant        none
// ==/UserScript==

// 百度贴吧
if (window.location.href.startsWith('https://jump2.bdimg.com/safecheck')) {
	document.querySelector('.btn.btn-next')
    const hrefValue = document.querySelector('.btn.btn-next').getAttribute('href');
    window.location.href = hrefValue;
}

// qq群;
if (window.location.href.startsWith('https://c.pc.qq.com/')) {
	const urlObj = new URL(window.location.href)
	urlObj.searchParams.get('url')
    window.location.href = urlObj.searchParams.get('url');
}