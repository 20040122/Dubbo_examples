from dubboclient import DubboClient

dubboclt= DubboClient("211.103.136.244",6502)
info={"id":911,"name":"张三","phoneNumber":"13555985732"}
info["class"]="com.itheima.pojo.Member"
resp=dubboclt.invoke("MemberService","add",info)
print("结果为：",resp)