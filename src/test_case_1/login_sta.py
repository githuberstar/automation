from ..models import myunit
from ..page_object.loginPage import Login
import unittest


class LoginTest(myunit.MyTest):
    def user_login_verify(self, username='chenyan', password='123456'):
        Login(self.driver).user_login(username, password)

    def test_login_1(self):
        self.user_login_verify()
        po = Login(self.driver)
        # self.assertEqual(po.user_error_hint(), "账号不能为空")


if __name__ == "__main__":
    unittest.main()
