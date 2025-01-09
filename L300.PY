# 描述：給定一個未排序的整數數組，找到其中最長的嚴格遞增子序列，並返回該序列的長度。與連續遞增子序列不同，此處的子序列元素不必是連續


def lengthOfLIS(nums):
    n = len(nums)
    if n == 0:
        return 0

    dp = [1] * n  # 初始化每個位置的 LIS 長度為 1

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # Output: 4 ([2, 3, 7, 101])
print(lengthOfLIS([0, 1, 0, 3, 2, 3]))           # Output: 4 ([0, 1, 2, 3])
print(lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))       # Output: 1 ([7])