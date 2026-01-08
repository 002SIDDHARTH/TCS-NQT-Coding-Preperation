arr=[2, -1, 0, -5, 6]
if not arr:
    print("Array is Empty")
else:
    positive=0
    neg=0
    zero=0
    for i in arr:
        if i>0:
            positive+=1
        elif i<0:
            neg+=1
        elif i==0:
            zero+=1
    print("Positive Number Count :",positive)
    print("Negative Number Counts :",neg)
    print("Zero Counts :",zero)
