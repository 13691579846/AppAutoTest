"""
------------------------------------
@Time : 2019/8/10 21:25
@Auth : linux超
@File : invest_data.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""


class InvestData(object):
    """借款"""
    invest_fail = [
        {
            "amount": "",
            "expected": "请输入投资金额"
        }
        # {
        #     "amount": 0,
        #     "expected": "最小投资金额为100.0"
        # },
        # {
        #     "amount": 99,
        #     "expected": "投资金额必须为100的整数倍"
        # },
        # {
        #     "amount": 101,
        #     "expected": "投资金额必须为100的整数倍"
        # }
    ]

    invest_success = [
        {
            "amount": 100,
            "expected": "投资成功"
        }
    ]
