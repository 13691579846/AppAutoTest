"""
------------------------------------
@Time : 2019/8/8 18:14
@Auth : linux超
@File : loan_page.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
from .base.base import Base
from .locator.pages_locator import LoanPageLocator as Locator


class LoanPage(Base):

    def loan_amount(self, amount):
        if amount:
            self.input_loan_amount(amount)
        return self.click_next_setup()

    def loan_business(self, rate, bidding_day, uses, limit_day, day, payment, address):
        if limit_day == "按天":
            self.click_loan_limit()
            self.select_loan_limit_day(limit_day, day)
        if limit_day == "按月":
            self.click_loan_limit()
            self.select_loan_limit_mouth(limit_day, day)
        if rate:
            self.input_loan_rate(rate)
        if bidding_day:
            self.click_loan_bidding()
            self.select_loan_bidding_option(bidding_day)
        if uses:
            self.click_loan_uses()
            self.select_loan_uses_option(uses)
        if limit_day == '按月' and day != "1月":
            if payment:
                self.click_payment()
                self.select_payment_option(payment)
        if address:
            self.click_loan_address()
            self.select_loan_address(address)
        return self.click_submit()

    def select_loan_limit_day(self, limit_day, day):
        """借款期限选择按天"""
        self.select_loan_limit_option(limit_day)
        return self.select_loan_limit_day_option(day)

    def select_loan_limit_mouth(self, limit_day, mouth):
        self.select_loan_limit_option(limit_day)
        return self.select_loan_limit_mouth_option(mouth)

    def select_loan_address(self, address):
        self.select_address_option(address)
        return self.select_address_second_option(address)

    def input_loan_amount(self, amount):
        return self.input_value(Locator.loan_amount_input, amount)

    def click_next_setup(self):
        return self.click(Locator.next_setup)

    def input_loan_rate(self, rate):
        return self.input_value(Locator.loan_rate, rate)

    def click_loan_bidding(self):
        return self.click(Locator.loan_bidding_btn)

    def select_loan_bidding_option(self, bidding_day):
        """key表示选项天数，value表示对应选项的元素的位置"""
        days_option = {
            "1天": 0,
            "2天": 1,
            "3天": 2,
            "4天": 3,
            "5天": 4
        }
        return self.select_list_option(Locator.loan_options, days_option[bidding_day])

    def click_loan_uses(self):
        return self.click(Locator.loan_uses_btn)

    def select_loan_uses_option(self, uses):
        uses_option = {
            "按揭赎楼借款": 0,
            "车辆抵押借款": 1,
            "红本抵押借款": 2,
            "短期周转": 3,
            "生意周转": 4,
            "逾期周转": 5,
            "创业借款": 6
        }
        return self.select_list_option(Locator.loan_options, uses_option[uses])

    def click_loan_limit(self):
        return self.click(Locator.loan_limit_btn)

    def select_loan_limit_option(self, limit):
        limit_option = {
            "按天": 0,
            "按月": 1
        }
        return self.select_list_option(Locator.loan_options, limit_option[limit])

    def select_loan_limit_day_option(self, option):
        day_option = {
            "1天": 0,
            "2天": 1,
            "3天": 2,
            "4天": 3,
            "5天": 4,
            "6天": 5,
            "7天": 6
        }
        return self.select_list_option(Locator.loan_options, day_option[option])

    def select_loan_limit_mouth_option(self, option):
        mouth_option = {
            "1月": 0,
            "2月": 1,
            "3月": 2,
            "4月": 3,
            "5月": 4,
            "6月": 5,
            "7月": 6
        }
        return self.select_list_option(Locator.loan_options, mouth_option[option])

    def click_payment(self):
        return self.click(Locator.loan_payment_btn)

    def select_payment_option(self, payment):
        payment_option = {
            "一次性": 0,
            "按月付息到期还本": 1,
            "按月等额本息线下": 2,
            "按月等额本息": 3
        }
        return self.select_list_option(Locator.loan_options, payment_option[payment])

    def click_loan_address(self):
        return self.click(Locator.loan_address_btn)

    def select_address_option(self, address):
        address_option = {
            "北京": 0,
            "天津": 1
        }
        return self.select_list_option(Locator.loan_options, address_option[address])

    def select_address_second_option(self, address):
        address_second_option = {
            "北京": 0,
            "天津": 1
        }
        return self.select_list_option(Locator.loan_options, address_second_option[address])

    def click_submit(self):
        return self.click(Locator.submit_btn)

    @property
    def get_submit_text(self):
        return self.get_element_text(Locator.submit_btn)

    @property
    def get_fail_massage(self):
        return self.get_element_text(Locator.error_info)

    def close_fail_massage(self):
        return self.click(Locator.error_commit_btn)

    @property
    def get_loan_success_info(self):
        return self.get_element_text(Locator.loan_success_info)

    def click_success_confirm(self):
        return self.click(Locator.loan_success_confirm_btn)


if __name__ == '__main__':
    pass
