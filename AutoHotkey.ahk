;https://github.com/wangandi520/andyspythonscript

;小键盘9重新载入脚本
Numpad9::reload

;小键盘8暂停脚本
Numpad8::pause

;小键盘7连续点击鼠标左键
Numpad7::
{
Loop{
Send {LButton}
Sleep 100
}
}

;小键盘6连续点击F6
Numpad6::
{
Loop{
Send {F6}
Sleep 200
}
return
}

;小键盘5抬起鼠标右键
Numpad5::
{
Send {RButton Up}
return
}

;小键盘4抬起鼠标左键
Numpad4::
{
Send {LButton up}
return
}

;小键盘3连续点击F5
Numpad3::
{
Loop{
Send {F5}
Sleep 200
}
return
}

;小键盘2按住鼠标右键
Numpad2::
{
Send {RButton Down}
return
}

;小键盘1按住鼠标左键
Numpad1::
{
Send {LButton Down}
return
}