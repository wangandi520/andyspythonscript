// ==UserScript==
// @name         网页自动跳转
// @namespace    http://tampermonkey.net/
// @version      2025-05-08
// @description  网页自动跳转
// @author       wangandi520
// @match        https://jump2.bdimg.com/safecheck*
// @match        https://c.pc.qq.com/*
// @match        https://link.zhihu.com/*
// @grant        none
// ==/UserScript==

// 百度贴吧
if (window.location.href.startsWith('https://jump2.bdimg.com/safecheck')) {
    const hrefValue = document.querySelector('.btn.btn-next').getAttribute('href');
    window.location.href = hrefValue;
}

// qq群;
if (window.location.href.startsWith('https://c.pc.qq.com/')) {
	const urlObj = new URL(window.location.href)
    window.location.href = urlObj.searchParams.get('url');
}

//知乎
if (window.location.href.startsWith('https://link.zhihu.com/')) {
    const hrefValue = document.querySelector('body > div.wrapper > div.content > p.link').textContent;
    window.location.href = hrefValue;
}