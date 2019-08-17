"""
------------------------------------
@Time : 2019/8/10 23:50
@Auth : linux超
@File : loan_data.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""


class LoanData(object):
    """投资"""
    loan_amount_none = [
        {
            "amount": "",
            "expected": "请输入借款金额"
        },
        {
            "amount": "0",
            "expected": "借款金额最低不能小于1000元"
        },
        {
            "amount": "999",
            "expected": "借款金额最低不能小于1000元"
        },
        {
            "amount": "1001",
            "expected": "借款金额要求整除1000"
        },
        {
            "amount": "5001000",
            "expected": "借款金额最大不能大于500万"
        }
    ]

    loan_amount_success = [
        {
            "amount": "500000",
            "expected": "提交"  # 投资金额正确页面有提交按钮
        }
    ]

    loan_lack_required_items = [
        {
            "amount": "50000",
            "rate": "",
            "bidding": "",
            "uses": "",
            "limit": "",
            "day_mouth": "",
            "payment": "",
            "address": "",
            "expected": "请输入借款利率"
        },
        {
            "amount": "50000",
            "rate": "0",
            "bidding": "",
            "uses": "",
            "limit": "",
            "day_mouth": "",
            "payment": "",
            "address": "",
            "expected": "借款利率要求大于0"
        },
        {
            "amount": "50000",
            "rate": "1",
            "bidding": "",
            "uses": "",
            "limit": "",
            "day_mouth": "",
            "payment": "",
            "address": "",
            "expected": "请选择竞标天数"
        },
        {
            "amount": "50000",
            "rate": "1",
            "bidding": "1天",
            "uses": "",
            "limit": "",
            "day_mouth": "",
            "payment": "",
            "address": "",
            "expected": "请选择借款用途"
        },
        {
            "amount": "50000",
            "rate": "1",
            "bidding": "1天",
            "uses": "短期周转",
            "limit": "",
            "day_mouth": "",
            "payment": "",
            "address": "",
            "expected": "请选择借款期限"
        },
        {
            "amount": "50000",
            "rate": "1",
            "bidding": "1天",
            "uses": "短期周转",
            "limit": "按月",
            "day_mouth": "2月",
            "payment": "",
            "address": "",
            "expected": "请选择还款方式"
        },
        {
            "amount": "50000",
            "rate": "1",
            "bidding": "1天",
            "uses": "短期周转",
            "limit": "按月",
            "day_mouth": "2月",
            "payment": "一次性",
            "address": "",
            "expected": "请选择所在地区"
        }
    ]
    loan_success = [
        {
            "amount": "50000",
            "rate": "1",
            "bidding": "1天",
            "uses": "短期周转",
            "limit": "按月",
            "day_mouth": "2月",
            "payment": "一次性",
            "address": "北京",
            "expected": "请确认您的借款信息"
        }
    ]
