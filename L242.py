#給定兩個字串 s 和 t，請判斷 t 是否為 s 的字母異位詞（Anagram）。字母異位詞指的是 由相同字母組成、但順序不同 的字串。

from collections import Counter

def isAnagram(s: str, t: str) -> bool:

    return Counter(s) == Counter(t)

def isAnagram2(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

# 測試
print("方法一")
print(isAnagram("anagram", "nagaram"))  # True
print(isAnagram("rat", "car"))  # False


print("方法二")
print(isAnagram2("anagram", "nagaram"))  # True
print(isAnagram2("rat", "car"))  # False



