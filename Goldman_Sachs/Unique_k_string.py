def unique_k(string, k):
    substr = []
    n = len(string)
    for i in range(n-k+1):
        str = string[i:i+k]
        if str in substr:
            next
        else:
            substr.append(str)

    return(sorted(substr))

string = "GoldMan"
string2= "caaab"
print(unique_k(string2,2))
