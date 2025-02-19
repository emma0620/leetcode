from collections import Counter

def firstUniqChar(s: str) -> int:
    counts = Counter(s)
    for i, char in enumerate(s):
        if counts[char] == 1:
            return i
    return -1


print(firstUniqChar("leetcode"))  # 輸出: 0
print(firstUniqChar("loveleetcode"))  # 輸出: 2
print(firstUniqChar("aabbcc"))  # 輸出: -1
print(firstUniqChar("abcdef"))  # 輸出: 0
print(firstUniqChar("aabbccddeeff"))  # 輸出: -1