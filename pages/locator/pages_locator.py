"""
------------------------------------
@Time : 2019/8/1 17:13
@Auth : linux超
@File : pages_locator.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
from appium.webdriver.common.mobileby import MobileBy


class HomePageLocator(object):
    welcome_btn = \
        (MobileBy.ID, 'com.xxzb.fenwoo:id/btn_start')
    home_btn = \
        (MobileBy.XPATH, '//android.widget.TabWidget[@resource-id=\"android:id/tabs\"]/android.widget.LinearLayout[1]')
    project_btn = \
        (MobileBy.XPATH, '//android.widget.TabWidget[@resource-id=\"android:id/tabs\"]/android.widget.LinearLayout[2]')
    found_btn = \
        (MobileBy.XPATH, '//android.widget.TabWidget[@resource-id=\"android:id/tabs\"]/android.widget.LinearLayout[3]')
    # myself_btn = \
    #    (MobileBy.XPATH, '//android.widget.TabWidget[@resource-id=\"android:id/tabs\"]/android.widget.LinearLayout[4]')
    myself_btn = (MobileBy.XPATH, '//android.widget.TextView[@text="我"]')
    # 更多标
    more_loan = (MobileBy.ID, 'com.xxzb.fenwoo:id/layout_more_loan')
    # 投标
    invest_btn = (MobileBy.ID, 'com.xxzb.fenwoo:id/pbar_process')
    # 首页中的我要借款按钮
    loan_btn = (MobileBy.ID, 'com.xxzb.fenwoo:id/layout_borrow_money')


class LoginLocator(object):
    login_register_btn = \
        (MobileBy.ID, 'com.xxzb.fenwoo:id/btn_login')
    phone_input = \
        (MobileBy.ID, 'com.xxzb.fenwoo:id/et_phone')
    next_step = \
        (MobileBy.ID, 'com.xxzb.fenwoo:id/btn_next_step')
    # 格式不正确的手机号，无效的手机号码提示信息
    invalid_phone = \
        (MobileBy.ID, 'com.xxzb.fenwoo:id/tv_message')
    # 提示框的确认按钮
    confirm_btn = \
        (MobileBy.ID, 'com.xxzb.fenwoo:id/btn_confirm')
    # 格式正确且已经注册的手机号码会直接跳到输入密码页面
    password_view = \
        (MobileBy.ID, 'com.xxzb.fenwoo:id/et_pwd')
    # 确定按钮
    commit_btn = \
        (MobileBy.ID, 'com.xxzb.fenwoo:id/btn_next_step')
    # 密码错误时候的提示
    password_warn = \
        (MobileBy.ID, 'com.xxzb.fenwoo:id/tv_login_warn')
    # 忘记密码
    forget_password = \
        (MobileBy.ID, 'com.xxzb.fenwoo:id/tv_forget_pwd')
    # 输入密码显示label
    password_label = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text(\"输入密码\")')


class RegisterLocator(object):
    # 注册按钮
    register_btn = (MobileBy.ID, 'com.xxzb.fenwoo:id/btn_register')
    # 验证码输入框
    verify_code = (MobileBy.ID, 'com.xxzb.fenwoo:id/et_code')
    # 登录密码输入框
    login_password = (MobileBy.ID, 'com.xxzb.fenwoo:id/et_pwd')
    # 确认码
    confirm_password = (MobileBy.ID, 'com.xxzb.fenwoo:id/et_confirm_pwd')
    # 同意
    agree_btn = (MobileBy.ID, 'com.xxzb.fenwoo:id/cb_protocol')
    # 注册失败提示
    register_message = (MobileBy.ID, 'com.xxzb.fenwoo:id/tv_message')
    # 关闭弹出框
    close_message = (MobileBy.ID, 'com.xxzb.fenwoo:id/btn_confirm')


class InvestPageLocator(object):
    # 金额输入框
    amount_view = (MobileBy.ID, 'com.xxzb.fenwoo:id/et_investamount')
    # 立即投资
    invest_now_btn = (MobileBy.ID, 'com.xxzb.fenwoo:id/btn_investnow')
    # 投资成功弹窗
    invest_success_massage = (MobileBy.ID, 'com.xxzb.fenwoo:id/tv_title')
    # 关闭弹窗
    confirm_btn = (MobileBy.ID, 'com.xxzb.fenwoo:id/btn_confirm')


class UserPageLocator(object):
    # 以后再说
    cancel_btn = (MobileBy.ID, 'com.xxzb.fenwoo:id/btn_cancel')
    # 马上设置
    confirm_btn = (MobileBy.ID, 'com.xxzb.fenwoo:id/btn_confirm')
    # 昵称
    my_name = (MobileBy.ID, 'com.xxzb.fenwoo:id/tv_name')


class LoanPageLocator(object):
    # 借款金额输入框
    loan_amount_input = (MobileBy.ID, 'com.xxzb.fenwoo:id/cet_loan_money')
    # 下一步
    next_setup = (MobileBy.ID, 'com.xxzb.fenwoo:id/btn_loan_next')
    # 借款利率
    loan_rate = (MobileBy.ID, 'com.xxzb.fenwoo:id/cet_loan_rate')
    # 竞标天数
    loan_bidding_btn = (MobileBy.ID, 'com.xxzb.fenwoo:id/layout_loan_bidding')
    # 借款用途
    loan_uses_btn = (MobileBy.ID, 'com.xxzb.fenwoo:id/layout_loan_uses')
    # 借款期限
    loan_limit_btn = (MobileBy.ID, 'com.xxzb.fenwoo:id/layout_loan_limit')
    # 还款方式
    loan_payment_btn = (MobileBy.ID, 'com.xxzb.fenwoo:id/layout_loan_payment')
    # 地区
    loan_address_btn = (MobileBy.ID, 'com.xxzb.fenwoo:id/layout_loan_address')
    # 提交按钮
    submit_btn = (MobileBy.ID, 'com.xxzb.fenwoo:id/btn_loan_submit')
    # 错误提示信息
    error_info = (MobileBy.ID, 'com.xxzb.fenwoo:id/tv_message')
    # 关闭错误提示框
    error_commit_btn = (MobileBy.ID, 'com.xxzb.fenwoo:id/btn_confirm')
    # 天数, 用途, 期限, 还款方式 列表选项
    loan_options = \
        (MobileBy.XPATH,
         '//android.widget.ListView[@resource-id=\"com.xxzb.fenwoo:id/listView\"]/android.widget.RelativeLayout')
    # '//android.widget.ListView[@resource-id=\"com.xxzb.fenwoo:id/listView\"]/android.widget.RelativeLayout[3]'
    loan_success_info = (MobileBy.ID, 'com.xxzb.fenwoo:id/tv_title')
    loan_success_confirm_btn = (MobileBy.ID, 'com.xxzb.fenwoo:id/btn_confirm')


if __name__ == '__main__':
    pass
