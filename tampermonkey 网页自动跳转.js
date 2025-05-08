// ==UserScript==
// @name         网页自动跳转
// @namespace    http://tampermonkey.net/
// @version      2025-05-08
// @description  try to take over the world!
// @author       You
// @match        https://jump2.bdimg.com/safecheck*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=bdimg.com
// @grant        none
// ==/UserScript==

// 百度贴吧
if (document.querySelector('.btn.btn-next')) {
    const hrefValue = document.querySelector('.btn.btn-next').getAttribute('href');
    window.location.href = hrefValue;
}