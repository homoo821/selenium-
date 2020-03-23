# -*- coding:utf-8 -*-
#Author: homoo
#Data: 2020/3/7
#File: upload_file.py
import win32gui
import win32con

class UploadFile():
    def upload_file(self,windows_title,filepath):
        # 获取一级窗口
        dialog=win32gui.FindWindow("#32770",windows_title)
        # 获取二级窗口
        comboxex32=win32gui.FindWindowEx(dialog,0,'ComboBoxEx32',None)
        # 获取三级窗口
        combox = win32gui.FindWindowEx(comboxex32, 0, 'ComboBox', None)
        # 文本输入窗口--四级
        edit = win32gui.FindWindowEx(combox, 0, 'Edit', None)
        # 打开按钮--二级
        button = win32gui.FindWindowEx(combox, 0, 'Button', None)

        # 输入文件地址
        win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,filepath)
        # 点击打开按钮--提交文件
        win32gui.SendMessage(dialog,win32con.WM_COMMAND,1,button)


if __name__ == '__main__':
    UploadFile().upload_file('打开',r"C:\Users\Administrator\Desktop\python-install.txt")