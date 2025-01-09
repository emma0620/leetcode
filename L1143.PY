# LeetCode 1143: 最長公共子序列

# 描述：給定兩個字符串，返回這兩個字符串的最長公共子序列的長度。子序列是指在不改變順序的情況下，刪除某些字符（也可以不刪除）後的字符串。

def longestCommonSubsequence(text1, text2):
    m, n = len(text1), len(text2)
    # 初始化 dp 陣列，大小為 (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1  # 字符相同時，長度加 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # 否則取最大值

    # 返回最長公共子序列的長度
    return dp[m][n]

text1 = "abcde"
text2 = "ace"
print(longestCommonSubsequence(text1, text2))  # 輸出 3 ("ace")

text1 = "abc"
text2 = "abc"
print(longestCommonSubsequence(text1, text2))  # 輸出 3 ("abc")

text1 = "abc"
text2 = "def"
print(longestCommonSubsequence(text1, text2))  # 輸出 0 (沒有公共子序列)