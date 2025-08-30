// ==UserScript==
// @name         网页自动跳转
// @namespace    http://tampermonkey.net/
// @version      2025-05-08
// @description  网页自动跳转
// @author       wangandi520
// @match        https://jump2.bdimg.com/safecheck*
// @match        https://jump.bdimg.com/safecheck*
// @match        http://jump.bdimg.com/safecheck*
// @match        https://c.pc.qq.com/*
// @match        https://wx.mail.qq.com/*
// @match        https://link.zhihu.com/*
// @match        https://gitee.com/link*
// @match        https://95598.csg.cn/*
// @grant        none
// ==/UserScript==

// 百度贴吧
if (window.location.href.startsWith('https://jump2.bdimg.com/safecheck')) {
    const hrefValue = document.querySelector('.btn.btn-next').getAttribute('href');
    window.location.href = hrefValue;
}
if (window.location.href.startsWith('https://jump.bdimg.com/safecheck')) {
    const hrefValue = document.querySelector('.btn.btn-next').getAttribute('href');
    window.location.href = hrefValue;
}
if (window.location.href.startsWith('http://jump.bdimg.com/safecheck')) {
    const hrefValue = document.querySelector('.btn.btn-next').getAttribute('href');
    window.location.href = hrefValue;
}

// qq群
if (window.location.href.startsWith('https://c.pc.qq.com/')) {
	const urlObj = new URL(window.location.href)
    window.location.href = urlObj.searchParams.get('url');
}

// qq邮箱
if (window.location.href.startsWith('https://wx.mail.qq.com/')) {
    const hrefValue = document.querySelector('#linkText').textContent;
    window.location.href = hrefValue;
}

//知乎
if (window.location.href.startsWith('https://link.zhihu.com/')) {
    const hrefValue = document.querySelector('body > div.wrapper > div.content > p.link').textContent;
    window.location.href = hrefValue;
}

//gitee
if (window.location.href.startsWith('https://gitee.com/link')) {
    const hrefValue = document.querySelector('body > div > div > div.content-link > div').textContent;
    window.location.href = hrefValue;
}

//自动关闭南方电网户号详情客户经理联系方式并跳转到页面底部
if (window.location.href.startsWith('https://95598.csg.cn/')) {
    setTimeout(() => {
        document.querySelector('body > div:nth-child(8) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > button').click();
        window.scrollTo(0, document.documentElement.scrollHeight)
    }, 2000);
}
