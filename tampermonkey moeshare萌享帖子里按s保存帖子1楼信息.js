// ==UserScript==
// @name         moeshare save tid infos
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://moeshare.cc/*
// @icon         https://www.google.com/s2/favicons?domain=moeshare.cc
// @grant        none
// ==/UserScript==
var checkTime = function (i) {
    if (i < 10) {
        i = "0" + i;
    }
    return i;
}

var showtime = function () {
    var nowdate = new Date();
    var year = nowdate.getFullYear(),
        month = nowdate.getMonth() + 1,
        date = nowdate.getDate(),
        day = nowdate.getDay(),
        week = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"],
        h = nowdate.getHours(),
        m = nowdate.getMinutes(),
        s = nowdate.getSeconds(),
        hh = checkTime(h),
        mm = checkTime(m),
        ss = checkTime(s);
    return year + "年" + month + "月" + date + "日 " + week[day] + " " + hh + ":" + mm + ":" + ss;

}

function downloadTXT(filename, contentType) {
    var tidName = document.querySelector('#subject_tpc').innerText
    var info = tidName + '\n\n'
    info = info + window.location.href
    info = info + document.querySelector('#readfloor_tpc > table > tbody > tr.vt > td.floot_left > div > div.readName.b').innerText + document.querySelector('#td_tpc > div.tipTop.s6 > span:nth-child(3)').innerText + '\n'
    info = info + document.querySelector('#read_tpc').innerText + '\n'
    info = info + '本文件创建时间 ' + showtime() + '\n'
    let element = document.createElement('a')
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(info))
    element.setAttribute('download', tidName)
    element.style.display = 'none'
    document.body.appendChild(element);
    element.click()
    document.body.removeChild(element);
}

document.onkeydown = function () {
    // 这里改成其他快捷键
    if (event.keyCode == 83) {
        downloadTXT();
    }
}
