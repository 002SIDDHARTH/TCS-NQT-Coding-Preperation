def Largest_Element(arr):
   largest=arr[0]
   for i in range(1,len(arr)):
      if arr[i]>largest:
         largest=arr[i]
   return largest
   

arr=[3,5,7,9,12]
print(Largest_Element(arr))