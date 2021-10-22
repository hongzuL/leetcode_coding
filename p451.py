# 451. Sort Characters By Frequency

def frequencySort(s):
    s_dict = dict()
    outs = ""
    for c in s:
        if c not in s_dict:
            s_dict[c] = s.count(c)
    
    s_dict = dict(sorted(s_dict.items(), key=lambda item:item[1], reverse=True))
    for key in s_dict:
        outs += s_dict[key] * key
    return outs



def main():
    s= "aaacccc"
    print(frequencySort(s))

main()