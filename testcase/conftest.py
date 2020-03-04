import os
import time
import yaml
import pytest
import shutil
import allure
import functools
from appium import webdriver
from public import base
from public.pages import business_hall, home


test_user_data = [{"user": "18310602997", "psw": "123123"},
                  {"user": "18801398500", "psw": "123123"}]



@pytest.fixture(scope='session')
def action():
    action = base.Action()
    yield action
    action.driver.quit()


# @pytest.fixture(scope='session', autouse=True)
# def clean():
#     if os.path.exists('data'):
#         shutil.rmtree('data')
#     os.mkdir('data')
#     if os.path.exists('report'):
#         shutil.rmtree('report')
#     os.mkdir('report')


@pytest.fixture()
def start_business_hall(action):
    business_hall_page = business_hall.BusinessHall()
    tabs = home.Tabs()
    with allure.step('进入我的tab'):
        action.click_by_text('我的')
        action.attach_screenshot('我的tab')
    with allure.step('新手引导-点击知道了'):
        action.attach_screenshot('新手引导')
        action.click_by_text('知道了')
    with allure.step('点击营业厅icon进入营业厅'):
        # action.click(business_hall_page.entrance_loc)
        action.click_by_text('营业厅')
        action.attach_screenshot('营业厅')


# @pytest.fixture(autouse=True)
# def set_case():
#     os.system('adb logcat -c')

@pytest.fixture(autouse=True)
def setup_case(action, request):
    action.login()
    def back_tear():
        action.driver.close_app()
        action.driver.launch_app()
    request.addfinalizer(back_tear)


@pytest.fixture(autouse=True)
def test_log(request, action):
    os.system('adb logcat -c')
    def attach_log():
        logcat = action.driver.get_log('logcat')
        c = '\n'.join(i['message'] for i in logcat)
        allure.attach(c, 'appLog', allure.attachment_type.TEXT)
    request.addfinalizer(attach_log)
    



def pytest_sessionstart(session):
    session.results = dict()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == 'call':
        item.session.results[item] = result


def retry(retry_times=3, delay=3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print(args)
            for i in range(retry_times):
                try:
                    print('try')
                    return func(*args, **kw)
                except:
                    time.sleep(delay)
                    continue
        return wrapper
    return decorator
    
    
