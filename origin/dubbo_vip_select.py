from dubboclient import DubboClient


dubboclt= DubboClient("211.103.136.244",6502)
resp=dubboclt.invoke("MemberService","findMemberCountByMonths",["2022-4","2023-4"])
print("结果为：",resp)