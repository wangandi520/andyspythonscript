// ==UserScript==
// @name         按s保存b站视频信息到txt文件
// @namespace    http://tampermonkey.net/
// @version      0.2
// @description  try to take over the world!
// @author       You
// @match        https://www.bilibili.com/video/*
// @icon         https://www.google.com/s2/favicons?domain=manhuabudangbbs.com
// @grant        none
// ==/UserScript==

function downloadHTML() {
    //使用bilibili evolved的快捷键功能时会冲突，在快捷键设置里添加一个空的自定义快捷可以禁用
	//标题
    var tidName = document.querySelector('#viewbox_report > div.video-info-title > div > h1').innerText
	//网址
    var info = tidName + '<p><a href="' + window.location.href + '">' + window.location.href + '</a></p>'
    info = info + '上传时间：' + document.querySelector('#viewbox_report > div.video-info-meta > div > div.pubdate-ip.item > div').innerText + '<br/>'
    info = info + '播放数：' + document.querySelector('#viewbox_report > div.video-info-meta > div > div.view.item > div').innerText + '<br/>'
    info = info + '弹幕数：' + document.querySelector('#viewbox_report > div.video-info-meta > div > div.dm.item > div').innerText + '<br/>'
    info = info + '上传者： ' + document.querySelector('#mirror-vdcon > div.right-container.is-in-large-ab > div > div.up-panel-container > div.up-info-container > div.up-info--right > div.up-info__detail > div > div.up-detail-top > a.up-name').innerText + '<br/>'
    var getSign = document.querySelector('#mirror-vdcon > div.right-container.is-in-large-ab > div > div.up-panel-container > div.up-info-container > div.up-info--right > div.up-info__detail > div > div.up-description.up-detail-bottom')
    if (getSign !== null && getSign !== undefined){
        info = info + '上传者签名： ' + getSign.innerText + '<br/>';
    }
    info = info + '点赞： ' + document.querySelector('#arc_toolbar_report > div.video-toolbar-left > div.video-toolbar-left-main > div:nth-child(1) > div > span').innerText + '<br/>'
    info = info + '投币： ' + document.querySelector('#arc_toolbar_report > div.video-toolbar-left > div.video-toolbar-left-main > div:nth-child(2) > div > span').innerText + '<br/>'
    info = info + '收藏： ' + document.querySelector('#arc_toolbar_report > div.video-toolbar-left > div.video-toolbar-left-main > div:nth-child(3) > div > span').innerText + '<br/>'
    info = info + '转发： ' + document.querySelector('#share-btn-outer > div > span').innerText + '<br/>'
    var getPart = document.querySelector('#multi_page > div.cur-list')
    if (getPart !== null && getPart !== undefined){
        info = info + '视频选集： ' + getPart.innerText + '<br/>';
    }
    info = info + '视频简介： ' + document.querySelector('#v_desc > div.basic-desc-info').innerText + '<br/>'
    info = info + '<p>本文件创建时间：' + new Date().toLocaleString() + '</p>'
    let element = document.createElement('a')
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(info))
    element.setAttribute('download', tidName + '.html')
    element.style.display = 'none'
    document.body.appendChild(element);
    element.click()
    document.body.removeChild(element);
}

document.onkeydown = function () {
    // 这里改成其他快捷键
    if (event.keyCode == 83) {
        downloadHTML();
    }
}
