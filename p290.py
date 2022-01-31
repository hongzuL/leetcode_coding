class Solution:
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        # idea is to use hashmap to store the mapping between pattern and s
        # then compare the pattern and s again
        # time complexity is O(n)
        # space complexity is O(n)
        s_list = s.split()
        if len(pattern) != len(s_list):
            return False
        pattern_dict = {}
        s_dict = {}
        for i in range(len(pattern)):
            if pattern[i] in pattern_dict:
                if pattern_dict[pattern[i]] != s_list[i]:
                    return False
            else:
                pattern_dict[pattern[i]] = s_list[i]
            if s_list[i] in s_dict:
                if s_dict[s_list[i]] != pattern[i]:
                    return False
            else:
                s_dict[s_list[i]] = pattern[i]
        return True

pattern = "abba"
s = "dog cat cat dog"
pattern = "abba"
s = "dog cat cat fish"
print(Solution().wordPattern(pattern, s))