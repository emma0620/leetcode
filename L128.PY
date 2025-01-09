# LeetCode 128: 最長連續序列

# 描述：給定一個未排序的整數數組，找出其中最長的連續元素序列的長度。要求算法的時間複雜度為 O(n)。

def longestConsecutive(nums):
    # 將數組元素存入哈希集合
    num_set = set(nums)
    max_length = 0

    for num in num_set:
        # 只有當 num-1 不在集合中時，才從 num 開始計算連續序列
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            # 向後查找連續數字
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            # 更新最大連續序列長度
            max_length = max(max_length, current_length)

    return max_length


# 測試案例1
nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums))  # 輸出: 4, 最長連續序列是 [1, 2, 3, 4]

# 測試案例2
nums = [0, -1]
print(longestConsecutive(nums))  # 輸出: 2, 最長連續序列是 [-1, 0]

# 測試案例3
nums = [1, 2, 0, 1]
print(longestConsecutive(nums))  # 輸出: 3, 最長連續序列是 [0, 1, 2]
