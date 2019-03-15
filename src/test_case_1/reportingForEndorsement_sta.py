from ..models import myunit
from ..page_object.basicInfoPage import Login2, BasicInfo, Applier, FileInformation, ExpenseCalculator, \
    NotarizationMatter, NotarizationDocuments
import unittest
import time


class ReportingForEndorsementTest(myunit.MyTest):
    """上报签批"""
    def setUp(self):
        super(ReportingForEndorsementTest, self).setUp()
        login = Login2(self.driver)
        login.new_business()
        time.sleep(1)

    def test_basic(self):
        """登录模块的测试以及公证类别的选择"""
        basic_info = BasicInfo(self.driver)
        basic_info.notary_category()  # 选择业务类别
        basic_info.use_land()  # 选择使用地
        basic_info.notary_purpose()  # 选择公正用途
        basic_info.notary_assistant()  # 选择公证员助理
        basic_info.service_type()  # 选择服务类别
        # self.assertEqual(po.user_error_hint(), "账号不能为空")

    def test_applier(self):
        """测试添加申请人"""
        applier = Applier(self.driver)
        applier.add_applier()

    def test_file_information(self):
        file_information = FileInformation(self.driver)
        file_information.add_file_infomation()

    def test_expense_calculator(self):
        expense_calculator = ExpenseCalculator(self.driver)
        expense_calculator.charge_fee()

    def test_notarization_matter(self):
        notarization_matter = NotarizationMatter(self.driver)
        notarization_matter.add_notarization_matter()

    def test_notarization_documents(self):
        self.test_basic()
        self.test_applier()
        self.test_notarization_matter()
        notarization_documents = NotarizationDocuments(self.driver)
        notarization_documents.add_notarization_document()


if __name__ == "__main__":
    unittest.main()
