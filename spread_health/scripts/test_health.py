import unittest

from spread_health.api.member_service import MemberService
from parameterized import parameterized

class TestFindByTelephone(unittest.TestCase):
    ms=None
    @classmethod
    def setUpClass(cls) -> None:
        cls.ms=MemberService()
    @parameterized.expand([('13020210001','李白'),('13555985732',None),('135090921*!',None)])
    def test_find_by_telephone(self,tel,expect):
        resp=self.ms.find_by_telephone(tel)
        if resp is None:
            self.assertEqual(expect,resp)
        else:
            self.assertEqual(expect,resp.get("name"))

        # def test_find_by_telephone(self):
        #     tel="13020210001"
        #     resp=self.ms.find_by_telephone(tel)
        #     self.assertEqual("李白",resp.get("name"))
        # def test_find_by_telephone_noexist(self):
        #     tel = "13555985732"
        #     resp = self.ms.find_by_telephone(tel)
        #     self.assertEqual(None, resp)
        # def test_find_by_telephone_type_error(self):
        #     tel = "135090921*!"
        #     resp = self.ms.find_by_telephone(tel)
        #     self.assertEqual(None, resp)