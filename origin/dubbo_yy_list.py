from dubboclient import DubboClient


dubboclt= DubboClient("211.103.136.244",6502)

month="2023-06"
resp=dubboclt.invoke("OrderSettingService","getOrderSettingByMonth",month)
print(resp)