from dubboclient import DubboClient


dubboclt= DubboClient("211.103.136.244",6502)

info=[{"orderDate":"2023-06-04 16:45:12","number":117}]
resp=dubboclt.invoke("OrderSettingService","add",info)
print("结果为：",resp)