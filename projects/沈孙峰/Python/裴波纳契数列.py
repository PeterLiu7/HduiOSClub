
def F(n):
    if (n == 0 or n == 1) :
        return n
    else :
        return F(n-1)+F(n-2)

n = int(input("请输入一个数"))

for i in range(0,n) :
    print(F(i))