from dubboclient import DubboClient


dubboclt= DubboClient("211.103.136.244",6502)

date={"orderDate":"2023-06-04 16:45:12","number":25,"class":"com.itheima.pojo.OrderSetting"}
resp=dubboclt.invoke("OrderSettingService","editNumberByDate",date)
