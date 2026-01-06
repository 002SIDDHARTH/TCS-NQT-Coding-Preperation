def Factorials(n):
    if n==1:
        return 1
    else:
        Previous_Fact=Factorials(n-1)
        return n * Previous_Fact
print(Factorials(10))