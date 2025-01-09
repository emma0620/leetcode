# LeetCode 718: 最長重复子數組

# 描述：給定兩個整數數組，找出並返回兩個數組中公共的、長度最長的子數組的長度。

def findLength(nums1, nums2):
    m, n = len(nums1), len(nums2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_len = 0

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if nums1[i] == nums2[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1
                max_len = max(max_len, dp[i][j])
    return max_len

nums1 = [1, 2, 3, 2, 1]
nums2 = [3, 2, 1, 4, 7]
print(findLength(nums1, nums2))  # 3