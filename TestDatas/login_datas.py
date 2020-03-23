# -*- coding:utf-8 -*-
#Author: homoo
#Data: 2020/3/7
#File: login_data.py

# 正常场景-测试数据
success_data={"user":"18684720553","pwd":"python"}

# 异常登录数据-表单提示的不正确
form_data=[
    {"user": "1868472055", "pwd": "python", "msg_check":"请输入正确的手机号"},
    {"user": "186847205531", "pwd": "python", "msg_check":"请输入正确的手机号"},
    {"user": "", "pwd": "python", "msg_check":"请输入手机号"},
    {"user": "12384720553", "pwd": "python", "msg_check":"请输入正确的手机号"},
    {"user": "18684720553", "pwd": "", "msg_check":"请输入密码"}
]

# 异常登录数据-页面中间提示的不正确
pagecenter_data=[
    {"user": "18684720553", "pwd": "1234", "msg_check":"帐号或密码错误!"},
    {"user": "15512341234", "pwd": "python", "msg_check":"此账号没有经过授权，请联系管理员!"}
]
