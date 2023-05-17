import json

from spread_health.api.base_service import BaseService


class OrderSettingService(BaseService):
    def __init__(self):
        super().__init__()
        self.service_name = "OrderSettingService"
    def add(self, info):
        resp = self.dubboclt.invoke(self.service_name, "add", info)
        if resp=="null":
            return True
        else:
            return False
    def change(self, date):
        date["class"] = "com.itheima.pojo.OrderSetting"
        resp = self.dubboclt.invoke(self.service_name, "editNumberByDate", date)
        if resp=="null":
            return True
        else:
            return False
    def list(self, month):
        resp = self.dubboclt.invoke(self.service_name, "getOrderSettingByMonth", month)
        return json.loads(resp)

