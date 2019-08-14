"""
------------------------------------
@Time : 2019/8/10 19:20
@Auth : linux超
@File : register_data.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""


class RegisterData(object):
    """注册"""
    phone = "13274517393"

    # 缺少必填项
    lack_required_items = [
        {
            "code": "",
            "login_pwd": "linuxxiaochao123",
            "verify_pwd": "linuxxiaochao123",
            "agree": 1,
            "expected": "请输入验证码"
        },
        {
            "code": "1234561",
            "login_pwd": "",
            "verify_pwd": "linuxxiaochao123",
            "agree": 1,
            "expected": "请输入6-16位的密码"
        },
        {
            "code": "1234562",
            "login_pwd": "linuxxiaochao123",
            "verify_pwd": "",
            "agree": 1,
            "expected": "请输入6-16位的确认密码"
        },
        {
            "code": "",
            "login_pwd": "",
            "verify_pwd": "",
            "agree": 0,
            "expected": "请输入6-16位的密码"
        }
    ]

    code_incorrect = [
        {
            "code": "123451",
            "login_pwd": "linuxxiaochao",
            "verify_pwd": "linuxxiaochao",
            "agree": 1,
            "expected": "验证码错误或已过期"
        }
    ]

    non_agree = [
        {
            "code": "123452",
            "login_pwd": "linuxxiaochao123",
            "verify_pwd": "linuxxiaochao123",
            "agree": 0,
            "expected": "请阅读并同意"
        }
    ]

    password_format_error = [
        {
            "code": "123453",
            "login_pwd": "linuxxiaochao",
            "verify_pwd": "linuxxiaochao",
            "agree": 1,
            "expected": "密码格式错误"
        }
    ]
