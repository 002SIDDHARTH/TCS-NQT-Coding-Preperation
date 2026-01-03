arr=[12,35,85,90]
Large=arr[0]
sec_Large=arr[0]
for i in range(1,len(arr)):
    if arr[i]>Large:
        Large=arr[i]
for i in range(1,len(arr)):
    if (arr[i]>sec_Large and arr[i] !=Large):
        sec_Large=arr[i]
print("Sec_Largest_Element :",sec_Large)