"""
------------------------------------
@Time : 2019/8/10 11:30
@Auth : linux超
@File : login_data.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""


class LoginData(object):
    """登录"""
    login_phone_incorrect = [
        {
            "phone": "",  # 手机号码为空
            "expected": "无效的手机号"
        },
        {
            "phone": "1369157984",  # 手机号码不足11位
            "expected": "无效的手机号"
        }
    ]

    login_phone_format_incorrect = [
        {
            "phone": "12345678901",  # 手机号格式错误
            "expected": "手机号码格式不正确"
        }
    ]

    login_phone_registered = [
        {
            "phone": "13691579846",  # 手机号已注册
            "expected": "输入密码"
        }
    ]

    login_phone_unregister = [
        {
            "phone": "12012345678",  # 手机号未注册
            "expected": "注册"
        }
    ]

    login_password_error = [
        {
            "phone": "13691579846",  # 正确的已注册的手机号
            "password": "linux超",  # 错误的密码
            "expected": "手机号或密码错误"
        }
    ]

    login_password_null = [
        {
            "phone": "13691579846",
            "password": "",  # 密码为空
            "expected": True
        }
    ]

    login_success = [
        {
            "phone": "****",
            "password": "****",
            "expected": "小蜜蜂"
        }
    ]
