#給定兩個字串 s 和 t，其中 t 是由 s 隨機打亂後，再額外添加一個字母而成的。請找出這個新增的字母。

def findTheDifference(s, t):
    s = sorted(s)
    t = sorted(t)
    
    for i in range(len(s)):  # 遍歷 s
        if s[i] != t[i]:  # 如果發現不同
            return t[i]  # 直接回傳多出的字母
    
    return t[-1]  # 如果 s 全部匹配，則最後一個字母就是多出的


def findTheDifference2(s, t):
    result = 0
    for char in s + t:
        result ^= ord(char)
    return chr(result)


s = "abcd"
t = "abcde"
s1 = ""
t1 = "y"


print("方法一")
print(findTheDifference(s, t) )
print(findTheDifference(s1, t1))
print("方法二")
print(findTheDifference2(s, t) )
print(findTheDifference2(s1, t1))