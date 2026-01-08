arr=[1,2,3,4]
if not arr:
    print("Array is Empty")
else:
    Copy_arr=[]
    for i in arr:
        Copy_arr.append(i)
    print("Original_Array :", arr)
    print("Copy_arr :",Copy_arr)

# With Out Append Method
arr1 = [1, 2, 3]
arr2 = [0] * len(arr1)

for i in range(len(arr1)):
    arr2[i] = arr1[i]

print(arr2)
