# -*- coding:utf-8 -*-
#Author: homoo
#Data: 2020/3/12
#File: invest_datas.py

# 正常场景-测试数据
success_invest_data={"money":"500"}

# 异常场景-投资金额不为100的整倍数、错误的格式等
no100_data=[
    {"money":"150","msg_check":"投标金额必须为100的倍数"}
]

# 异常登录数据-页面中间提示的不正确
pagecenter_data=[
    {"user": "18684720553", "pwd": "1234", "msg_check":"帐号或密码错误!"},
    {"user": "15512341234", "pwd": "python", "msg_check":"此账号没有经过授权，请联系管理员!"}
]
