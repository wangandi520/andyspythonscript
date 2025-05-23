// ==UserScript==
// @name         moeshare助手自动评分下载1楼内容
// @namespace    http://tampermonkey.net/
// @version      0.8
// @description  按钮位置在搜索按钮上面
// @author       https://github.com/wangandi520/andyspythonscript
// @match        https://moeshare.cc/read*
// @match        https://www.moeshare.cc/read*
// @grant        none
// ==/UserScript==

// 按钮位置在搜索按钮上面，要打开某一帖后才会显示
// 不想启动的功能，请改成0=不启动，1=启用
// 回帖用户名在浏览器f12中显示
var optionShowUserName = 1
// www.moeshare.cc跳转到moeshare.cc
var optionJumpToMoeshare = 0
// 显示评分打卡按钮
var optionShowPingfenDakaButton = 1
// 显示打卡按钮
var optionShowDakaButton = 1
// 显示保存按钮
var optionShowSaveButton = 1
// 显示工作状态
var optionShowStatus = 1


if (optionJumpToMoeshare){
    var getUrl = window.location.href
    if (getUrl.substr(0,11) == "https://www"){
        window.location.href = "https://moeshare.cc" + getUrl.substr(23,getUrl.length);
    }
    /**
	if (getUrl.substr(0,11) == "https://moe"){
		window.location.href = "https://www.moeshare.cc" + getUrl.substr(19,getUrl.length);
	}
	**/
}

if (optionShowPingfenDakaButton){
	let pingfenbutton = document.createElement('button');
	pingfenbutton.innerHTML = '自动评分打卡';
	pingfenbutton.style.backgroundColor = 'green';
	pingfenbutton.style.color = 'white';
	pingfenbutton.style.border = 'none';
	pingfenbutton.style.padding = '10px 20px';
	pingfenbutton.addEventListener('click', function() {
		if (optionShowStatus){
			document.querySelector('#navA > div.navA > ul > span > span').innerHTML = '<span>打卡开始</span>';
		}
		var eachScore = document.getElementsByClassName('r-score');
		var i = 1;
		var myinterval;
		myinterval = setInterval(function(){
			pingfen(eachScore,i);
			if (optionShowStatus){
				document.querySelector('#navA > div.navA > ul > span > span').innerHTML = '<span>正在评分第' + i + '楼</span>';
			}
			i = i + 1;
			if (i > 10){
				clearInterval(myinterval);
                let iframe = document.createElement('iframe');
                document.lastElementChild.appendChild(iframe);
                iframe.style = 'display: none;';
                iframe.src = 'https://moeshare.cc/jobcenter.php?action=punch&step=2';
				if (optionShowStatus){
					document.querySelector('#navA > div.navA > ul > span > span').innerHTML = '<span>打卡可能完成</span>';
				}
			}
		}, 5000);
	});
	document.querySelector('#navA > div.navA > ul').appendChild(pingfenbutton);
}

if (optionShowDakaButton){
	let dakabutton = document.createElement('button');
	dakabutton.innerHTML = '仅打卡';
	dakabutton.style.backgroundColor = 'blue';
	dakabutton.style.color = 'white';
	dakabutton.style.border = 'none';
	dakabutton.style.padding = '10px 20px';
	dakabutton.addEventListener('click', function() {
        let iframe = document.createElement('iframe');
        document.lastElementChild.appendChild(iframe);
        iframe.style = 'display: none;';
        iframe.src = 'https://moeshare.cc/jobcenter.php?action=punch&step=2';
        if (optionShowStatus){
            document.querySelector('#navA > div.navA > ul > span > span').innerHTML = '<span>打卡可能完成</span>';
        }
	});
	document.querySelector('#navA > div.navA > ul').appendChild(dakabutton);
}

if (optionShowSaveButton){
	let downloadbutton = document.createElement('button');
	downloadbutton.innerHTML = '保存1楼内容';
	downloadbutton.style.backgroundColor = 'red';
	downloadbutton.style.color = 'white';
	downloadbutton.style.border = 'none';
	downloadbutton.style.padding = '10px 20px';
	downloadbutton.addEventListener('click', function() {
		downloadHTML();
	});
	document.querySelector('#navA > div.navA > ul').appendChild(downloadbutton);


}

if (optionShowUserName){
		var name = document.getElementsByClassName('readName b');
		for (var i = 0, len = name.length; i < len; i++) {
			console.log(i + '  ' + name[i].children[1].innerHTML);
		}
}

if (optionShowStatus){
	let myMessage = document.createElement('span');
	myMessage.style.color = 'white';
	document.querySelector('#navA > div.navA > ul').appendChild(myMessage);
	myMessage.innerHTML = '<span>moeshare脚本加载成功</span>';
}

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

function pingfen(eachScore,i){
    eachScore[i - 1].click();
    setTimeout(function(){
        var my = document.querySelector('#c_model');
        setTimeout(function(){
            document.querySelector('#box_container .btn2 button').click();
        }, 1000);
    }, 1000);
}
