def vowel_and_const(string):
    v=0
    c=0
    for i in range(len(string)):
        vowels='aeiouAEIOU'
        if string[i] not in vowels:
            c+=1
        else:
            v+=1
    return v,c
string='Python'
print(vowel_and_const(string))
