from dubboclient import DubboClient


dubboclt=DubboClient("211.103.136.244",6502)
resp=dubboclt.invoke("MemberService","findByTelephone","13020210001")
print("结果为：",resp)