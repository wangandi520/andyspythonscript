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

function downloadIamge(selector, name) {
    // 创建一个img标签
    var image = new Image()
    // 解决跨域 Canvas 污染问题
    image.setAttribute('crossOrigin', 'anonymous')
    image.onload = function () {
        var canvas = document.createElement('canvas')
        canvas.width = image.width
        canvas.height = image.height
        var context = canvas.getContext('2d')
        context.drawImage(image, 0, 0, image.width, image.height)
        var url = canvas.toDataURL('image/png')
        // 生成一个a元素
        var a = document.createElement('a')
        // 创建一个单击事件
        var event = new MouseEvent('click')
        // 将a的download属性设置为我们想要下载的图片名称，若name不存在则使用‘下载图片名称’作为默认名称
        a.download = name + '.png' || 'one' // one是默认的名称
        // 将生成的URL设置为a.href属性
        a.href = url
        // 触发a的单击事件
        a.dispatchEvent(event)
     }
    image.src = selector.src
}

function downloadHTML() {
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

    var getAllImg = document.getElementById("read_tpc").getElementsByTagName("img")
    for (let imgIndex = 0; imgIndex < getAllImg.length; imgIndex++){
        if (imgIndex < 10){
            downloadIamge(getAllImg[imgIndex],tidName + '0' + imgIndex)
            getAllImg[imgIndex].src = tidName + '0' + imgIndex + '.png'
        }
        else if (imgIndex >= 10){
            downloadIamge(getAllImg[imgIndex],tidName + imgIndex)
            getAllImg[imgIndex].src = tidName + imgIndex + '.png'
        }
    }
    let element = document.createElement('a')
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(info))
    element.setAttribute('download', tidName + '.html')
    element.style.display = 'none'
    document.body.appendChild(element);
    element.click()
    document.body.removeChild(element);

	let image = document.get
}

document.onkeydown = function () {
    // 这里改成其他快捷键
    if (event.keyCode == 83) {
        downloadHTML();
    }
}
