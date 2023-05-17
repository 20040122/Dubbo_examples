from htmltestreport import HTMLTestReport
import unittest

from spread_health.scripts.test_health import TestFindByTelephone

suite=unittest.TestSuite()
suite.addTests(unittest.makeSuite(TestFindByTelephone))

runner=HTMLTestReport("../spread_health/reports/测试报告.html",title="健康管理系统测试报告")
runner.run(suite)
