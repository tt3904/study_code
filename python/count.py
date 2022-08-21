# -- coding:utf-8 --

from collections import Counter

list=["name","liyi","clasee",1,"stu",4,"liyi"]

print("方法2", dict(Counter(list)))

list2=["name","liyi","clasee",1,"stu",4,"liyi"]
li={name1:0 for name1 in set(list2)}
print(li)
for name1 in list2:
    if name1 in li:
        li[name1]+=1
    else:
        li[name1]=1
print("方法1",li)