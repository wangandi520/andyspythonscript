;https://github.com/wangandi520/andyspythonscript

;双击AutoHotkey64.exe，或把AutoHotkey64.ahk拖到AutoHotkey64.exe启动脚本
;小键盘9重新载入脚本，停止所有动作
;小键盘8连续点击D
;小键盘7连续点击F
;小键盘6连续点击鼠标左键
;小键盘5按住鼠标左键
;小键盘4抬起鼠标左键

;小键盘9重新载入脚本，停止所有动作
Numpad9::reload

;小键盘8连续点击D
Numpad8::
{
Loop{
Send "{D}"
Sleep 200
}
return
}

;小键盘7连续点击F
Numpad7::
{
Loop{
Send "{F}"
Sleep 200
}
return
}

;小键盘6连续点击鼠标左键
Numpad6::
{
Loop{
Send "{LButton}"
Sleep 200
}
}

;小键盘5按住鼠标左键
Numpad5::
{
Send "{LButton Down}"
return
}

;小键盘4抬起鼠标左键
Numpad4::
{
Send "{LButton Up}"
return
}