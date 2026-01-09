arr=[1,2,3,4,5]
K=2
for i in range(0,K):
    temp=arr[len(arr)-1]
    for j in range(len(arr)-1,0,-1):
        arr[j]=arr[j-1]
    arr[0]=temp

print(arr)