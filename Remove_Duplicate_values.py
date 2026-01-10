arr =[1,2,1,2,3]
for i in range(len(arr)):
    is_duplicate = False
    for j in range(i):
        if arr[i]==arr[j]:
            is_duplicate = True
            break
    else:
        print(arr[i], end=" ")

            


