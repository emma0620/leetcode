#給定兩個字串 word1 和 word2，請交錯合併兩個字串。

def mergeAlternately(word1, word2):
    result = []
    i, j = 0, 0
    
    # 交替合併兩個字串
    while i < len(word1) and j < len(word2):
        result.append(word1[i])
        result.append(word2[j])
        i += 1
        j += 1
    
    # 將剩下的字母附加到結果中
    result.extend(word1[i:])
    result.extend(word2[j:])
    
    # 將結果轉換為字串
    return ''.join(result)

# 測試
word1 = "abc"
word2 = "def"
print(mergeAlternately(word1, word2))  # 輸出 "adbcef"
