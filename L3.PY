#給定一個字串 s，請找出不包含重複字元的最長子字串的長度。

def lengthOfLongestSubstring(s):
    seen = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))