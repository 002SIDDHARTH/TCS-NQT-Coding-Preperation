A='siddharth'
rev=''
for i in range(len(A)-1,-1,-1):
    rev+=A[i]
print(rev)
# two pointer based 
def reverse_string(s):
    str=list(s)
    first=0
    last=len(str)-1
    while first<last:
        str[first],str[last]=str[last],str[first]
        first+=1
        last-=1

    rev=''
    for ch in str:
        rev+=ch
    return rev
s="Enter Your Strings"
print(reverse_string(s))