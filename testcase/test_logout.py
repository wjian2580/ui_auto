import allure

@allure.feature('退出登录')
class TestLogout():

    def test_logout(self, action):
        action.logout()
