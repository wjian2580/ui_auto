import os
import time
import pytest
import allure
import functools
from public.pages.app import App
import shutil

test_user_data = [{"user": "18310602997", "psw": "123123"},
                  {"user": "18801398500", "psw": "123123"}]


@pytest.fixture(scope='session')
def init():
    if os.path.exists('data'):
        shutil.rmtree('data')
    os.mkdir('data')
    if os.path.exists('report'):
        shutil.rmtree('report')
    os.mkdir('report')

    init = App.start().login()
    yield init
    # init.driver.quit()
    # init.clear_app()
    # driver.resetApp();


# @pytest.fixture(autouse=True)
# def test_log(request, init):
#     os.system('adb logcat -c')
#
#     def attach_log():
#         logcat = init.driver.get_log('logcat')
#         c = '\n'.join(i['message'] for i in logcat)
#         allure.attach(c, 'appLog', allure.attachment_type.TEXT)
#
#     def tear_case():
#         init.driver.close_app()
#         init.driver.launch_app()
#
#     request.addfinalizer(attach_log)
#     request.addfinalizer(tear_case)


# def pytest_sessionstart(session):
#     session.results = dict()


# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     result = outcome.get_result()
#
#     if result.when == 'call':
#         item.session.results[item] = result


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
