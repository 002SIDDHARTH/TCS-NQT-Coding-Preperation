def Sec_Lowest_Element(arr):
    arr=[8,6,3,5,9,1,7]
    Lowest=float('inf')
    Sec_Lowest=float('inf')
    for i in arr:
        if i<Lowest:
          Sec_Lowest=Lowest
          Lowest=i
        elif(i!=Lowest and i < Sec_Lowest):
           Sec_Lowest=i
    return Sec_Lowest
arr=[8,6,3,5,9,1,7]
print(Sec_Lowest_Element((arr)))