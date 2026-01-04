def string_analysis_two_pointer(s):
    non_repeating = []
    repeating = []

    n = len(s)

    for i in range(n):
        count = 0
        j = 0

        while j < n:
            if s[i] == s[j]:
                count += 1
            j += 1

        if count == 1:
            non_repeating.append(s[i])
        elif count > 1 and s[i] not in repeating:
            repeating.append(s[i])

    print("All non-repeating characters:", non_repeating)
    print("All repeating characters:", repeating)

    if non_repeating:
        print("First non-repeating character:", non_repeating[0])
        print("Last non-repeating character:", non_repeating[-1])
    else:
        print("No non-repeating characters found")


s = "siddharth"
string_analysis_two_pointer(s)
