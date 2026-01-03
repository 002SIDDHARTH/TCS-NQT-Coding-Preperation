def smallest_elenment(array):
    smallest=array[0]
    for i in range(1,len(array)):
        if array[i]<smallest:
          smallest=array[i]
    return smallest

array=[8,2,4,7,5,0]
print(smallest_elenment(array))