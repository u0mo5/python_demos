# coding=utf-8
import subprocess
from time import *
import win32api
import win32con
import win32gui

subprocess.Popen('C:\windows\system32\cmd.exe')
sleep(1)
a = 65;
b = 66;
c = 67;
d = 68;
e = 69;
f = 70;
g = 71;
h = 72;
i = 73;
j = 74;
k = 75
l = 76;
m = 77;
n = 78;
o = 79;
p = 80;
q = 81;
r = 82;
s = 83;
t = 84;
u = 85;
v = 86
w = 87;
x = 88;
y = 89;
z = 90;
i = 97;
ii = 98;
iii = 99;
iv = 100;
five = 101;
vi = 102
vii = 103;
viii = 104;
ix = 105;
zero = 0;

# 定义了常用按键的编码
n = win32gui.FindWindow('ConsoleWindowClass', None)

# 查找打开的窗口，findwindow（x,y）x是类别名，y是窗口标题
p = win32gui.SetForegroundWindow(n)

# 获取指针
win32api.keybd_event(d, 0, 0, 0)
win32api.keybd_event(s, 0, 0, 0)
win32api.keybd_event(m, 0, 0, 0)
win32api.keybd_event(o, 0, 0, 0)
win32api.keybd_event(v, 0, 0, 0)
win32api.keybd_event(e, 0, 0, 0)
win32api.keybd_event(13, 0, 0, 0)
win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
win32api.keybd_event(13, 0, 0, 0)
win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
win32api.keybd_event(13, 0, 0, 0)
# 模拟键盘输入

#获取窗口信息的工具：Microsoft
#Spy + +