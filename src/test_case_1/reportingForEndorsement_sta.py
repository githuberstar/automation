from ..models import myunit
from ..page_object.basicInfoPage import BasicInfo
import unittest


class ReportingForEndorsementTest(myunit.MyTest):
    """上报签批"""
    def test_basic(self):
        """登录模块的测试以及公证类别的选择"""
        test = BasicInfo(self.driver)
        test.new_business()
        test.notary_category()
        # self.assertEqual(po.user_error_hint(), "账号不能为空")


if __name__ == "__main__":
    unittest.main()