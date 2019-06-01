# -*- coding: UTF-8 -*-
a1=input()
A=[]
for i in a1:
    A.append(i)
B=input().split()
ACM=input().split()
English=input().split()
num=input()
All=A+B
Both=list(set(ACM+English))
English_ACM=set(ACM).intersection(set(English))
print("Total:"+str(len(set(All))))
print("Not in race:"+str(sorted(set(All)^set(Both)))+",nums:"+str(len(list(set(All)^set(Both)))))
print("All racers:",sorted(Both)," nums:",len(list(Both)))
print("ACM + English:"+str(sorted(English_ACM))+",num:"+str(len(English_ACM)))
print("Only ACM:"+str(sorted(set(English)^set(Both))))
print("Only English:"+str(sorted(set(ACM)^set(Both))))
print("ACM Or English:"+str(sorted(set(ACM)^set(English))))
if num in A:
    new =list(A)
    new.remove(num)
    print(sorted(set(new)))
elif num in B:
    new = list(B)
    new.remove(num)
    print(sorted(set(new)))
