def Reverse(arr):
    p1=0
    p2=len(arr)-1
    while p1 <p2:
        arr[p1],arr[p2]=arr[p2],arr[p1]
        p1+=1
        p2-=1
    return arr

arr=[2,4,7,9,0,1]
Reverse(arr)
print("Reverse an Array :", arr)

#  Recursive method

def reverse_array(arr, start, end):
    if start >= end:
        return

    arr[start], arr[end] = arr[end], arr[start]
    reverse_array(arr, start + 1, end - 1)


arr = [1, 8, 2, 6, 4, 3]
reverse_array(arr, 0, len(arr) - 1)
print("Recursive method",arr)
