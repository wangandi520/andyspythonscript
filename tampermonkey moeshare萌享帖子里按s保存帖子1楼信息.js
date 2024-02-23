// ==UserScript==
// @name         moeshare萌享帖子里按s保存帖子1楼信息
// @namespace    http://tampermonkey.net/
// @version      0.5
// @description  try to take over the world!
// @author       You
// @match        https://www.moeshare.cc/read-htm-tid*
// @match        https://moeshare.cc/read-htm-tid*
// @icon         https://www.google.com/s2/favicons?domain=moeshare.cc
// @grant        none
// ==/UserScript==

function downloadHTML() {
	//可以搭配下载html文件中的图片并修改地址成为本地文件名（拖拽，多个本地html文件）.py
	//把图片保存到本地电脑中
    var tidName = document.querySelector('#subject_tpc').innerText
    var info = document.querySelector('#subject_tpc').innerHTML
    info = info + '<p><a href="' + window.location.href + '">' + window.location.href + '</a></p>'
    info = info + document.querySelector('#readfloor_tpc > table > tbody > tr.vt > td.floot_left > div > div.readName.b > a').innerHTML + ' ' + document.querySelector('#td_tpc > div.tipTop.s6 > span:nth-child(3)').innerHTML + '<br/>'
    info = info + document.querySelector('#read_tpc').innerHTML + '<br/>'
    var getSign = document.querySelector('#readfloor_tpc > table > tbody > tr:nth-child(2) > td > div.pr > div > table > tbody > tr > td');
    if (getSign !== null && getSign !== undefined){
        info = info + getSign.innerHTML + '<br/>';
    }
    info = info + '<p>本文件创建时间 ' + new Date().toLocaleString() + '</p>'
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
