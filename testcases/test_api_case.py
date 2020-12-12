# -!- coding: utf-8 -!-
import os
import paramunittest
import unittest
import warnings
from utils.testcase_data_utils import TestcaseDataUtils
from utils.requests_utils import RequestsUtils

test_case_lists = TestcaseDataUtils().convert_testcase_data_to_list()
@paramunittest.parametrized(
    *test_case_lists
)
class TestApiCase(paramunittest.ParametrizedTestCase):
    def setUp(self) -> None:
        warnings.simplefilter('ignore',ResourceWarning)
    def setParameters(self, case_id, case_step):
        self.case_id = case_id
        self.case_step = case_step
    def test_api_case(self):
        self._testMethodName = self.case_step[0].get('测试用例编号')
        self._testMethodDoc = self.case_step[0].get('测试用例名称')
        test_result = RequestsUtils().request_by_step(self.case_step)
        self.assertTrue(test_result['check_result'],test_result['message'])


if __name__ == '__main__':
    unittest.main(verbosity=2)


