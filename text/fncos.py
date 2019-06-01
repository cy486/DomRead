def funcos(eps,x):
    e=float(eps)
    x=float(x)
    flag = -1
    item = 1
    m = 2
    sum = 1
    fenmu = 1
    while (item > eps):
        for i in range(1,m+1):
            fenmu=fenmu * i
        fenzi=pow(x, m)
        item=fenzi / fenmu
        sum=sum+flag * item
        m=m+2
        fenmu=1
        flag=-flag
    print("cos(%s)=%0.4f"%(x,sum))

eps=float(input())
x=float(input())
funcos(eps,x )