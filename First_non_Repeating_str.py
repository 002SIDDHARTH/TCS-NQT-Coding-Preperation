def First_Non_Repeating_str(st):
    for i in range(len(st)):
        count=0
        for j in range(len(st)):
            if st[i]==st[j]:
                count+=1
        if count==1:
            return st[i]
    return 
st='ssddharth'
print(First_Non_Repeating_str(st))
