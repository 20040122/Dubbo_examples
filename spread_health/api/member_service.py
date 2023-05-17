import json

from spread_health.api.base_service import BaseService


class MemberService(BaseService):
    def __init__(self):
        super().__init__()
        self.service_name = "MemberService"
    def find_by_telephone(self, telephone):
        resp = self.dubboclt.invoke(self.service_name, "findByTelephone", telephone)
        # 将字符串转换为字典
        return json.loads(resp)
    def select(self, months):
        resp = self.dubboclt.invoke(self.service_name, "findMemberCountByMonths", months)
        # 将字符串转换为字典,list
        return json.loads(resp)
    def add(self, info):
        info["class"] = "com.itheima.pojo.Member"
        resp = self.dubboclt.invoke(self.service_name, "add", info)
        if resp=="null":
            return True
        else:
            return False
