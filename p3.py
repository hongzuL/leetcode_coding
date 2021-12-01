# 3. Longest Substring Without Repeating Characters
def lengthOfLongestSubstring(s):
    if s == "":
        return 0
    max_len = 0
    sub_string = ""
    for i in range(len(s)):
        cs = s[i]
        sub_stringl = list()
        sub_stringl.append(cs)
        for j in range(i+1, len(s)):
            if s[j] not in sub_stringl:
                sub_stringl.append(s[j])
            else:
                break
        if len(sub_stringl) > max_len:
            max_len = len(sub_stringl)
            sub_string = "".join(sub_stringl)

    print(max_len)
    print(sub_string)
    return max_len

lengthOfLongestSubstring("pwwkew")