class MemberCounter:
    members=0
    def init(self):
        MemberCounter.members+=1

m1=MemberCounter()
m1.init()
print(MemberCounter.members)

m2=MemberCounter()
m2.init()
print(MemberCounter.members)

print(m1.members)
print(m2.members)

# 修改m1的属性值，其他的属性值不变
m1.members='Two'
print(m1.members)

print(m2.members)
print(MemberCounter.members)