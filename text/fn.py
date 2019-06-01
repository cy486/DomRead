def fn(a,b):
    s=0
    num=str(a)
    for i in range(1,b+1):
        s+=int(num*i)
    return str(s)
a,b=input().split()
s=fn(int(a),int(b))
print(s)
print()