#給定一個字串 s，請移除所有母音（a, e, i, o, u），並回傳處理後的字串。

def remove_motherletter(letters):
    remove_letter = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']  # 加入大小寫
    return ''.join(c for c in letters if c not in remove_letter)

def removeVowels(s: str) -> str:
    return "".join([char for char in s if char not in "aeiou"])

# 測試
print("方法一")
print(remove_motherletter("leetcode"))  # 輸出: "ltcd"
print(remove_motherletter("AEIOUxyz"))  # 輸出: "xyz"
print("方法二")
print(removeVowels("leetcode"))  # 輸出: "ltcd"
print(removeVowels("AEIOUxyz"))  # 輸出: "xyz"
