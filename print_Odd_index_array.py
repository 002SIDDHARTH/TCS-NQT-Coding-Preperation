arr=[4,5,6,7,8,9,10]
if not arr:
    print("Array is Empty")
else:
    for i in range(1,len(arr),2):
        print(arr[i],end=" ")