def Left_Array_Rotate(arr,K):
    for i in range(0,K):
        temp=arr[0]
        for j in range(0,len(arr)-1):
            arr[j]=arr[j+1]
        arr[len(arr)-1]=temp
    for i in range(0,len(arr)):
        print(arr[i])
    
arr=[1,2,3,4,5,6]
K=3
print(Left_Array_Rotate(arr,K))