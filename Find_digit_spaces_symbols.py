def finding(sent):
    Digits=0
    Spaces=0
    symbols=0
    for ch in sent:
        if '0'<= ch <= '9':
            Digits+=1
        elif ch==' ':
            Spaces+=1
        elif not ('a' <= ch <= 'z' or 'A' <= ch <= 'Z'):
            symbols+=1
    return Digits, Spaces, symbols
sent='siddhart002@ gmail'
print(finding(sent))