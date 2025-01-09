# LeetCode 53: 最大子數組和

# 描述：給定一個整數數組，找到具有最大和的連續子數組（至少包含一個元素），返回其最大和。


def maxSubArray(nums):
    # 初始化dp陣列，dp[i] 表示以 nums[i] 結束的最大子數組和
    current_sum = nums[0]  # 以第一個元素為起點的最大子數組和
    max_sum = nums[0]      # 初始化最大和

    for i in range(1, len(nums)):
        # 更新當前的最大和
        current_sum = max(current_sum + nums[i], nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

# 測試案例1
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))  # 輸出: 6, 最大和是 4 + (-1) + 2 + 1

# 測試案例2
nums = [1]
print(maxSubArray(nums))  # 輸出: 1, 只有一個元素 1

# 測試案例3
nums = [5,4,-1,7,8]
print(maxSubArray(nums))  # 輸出: 23, 最大和是 5 + 4 + (-1) + 7 + 8