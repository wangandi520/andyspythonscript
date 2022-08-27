// ==UserScript==
// @name         漫画补档帖子回帖用户名在浏览器f12中显示
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://www.manhuabudangbs.com/read*
// @icon         https://www.google.com/s2/favicons?domain=manhuabudangbs.com
// @grant        none
// ==/UserScript==

var name = document.getElementsByClassName('readName b');


for (var i = 0, len = name.length; i < len; i++) {
    console.log(name[i].children[1].innerHTML);
}