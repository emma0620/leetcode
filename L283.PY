#給定一個陣列 nums，將所有 0 移動到陣列的最後，並且保持其他非零元素的相對順序不變。請就地修改 nums，不得使用額外的陣列。

def moveZeroes(nums):
    zero_count = nums.count(0)  # 計算 0 的數量
    nums[:] = [num for num in nums if num != 0]  # 過濾掉 0
    nums.extend([0] * zero_count)  # 在後面補上 0


def moveZeroes2(nums):
    i = 0
    length = len(nums)
    
    while i < length:
        if nums[i] == 0:
            nums.pop(i)   # 刪除 0
            nums.append(0) # 將 0 加到尾巴
            length -= 1    # 陣列長度減 1，但 `nums.append(0)` 又補回來
        else:
            i += 1  # 只有當 `nums[i]` 不是 0 時才前進



# 測試
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # 輸出: [1, 3, 12, 0, 0]

print("另一個方法")
nums2 = [0, 1, 0, 3, 12]
moveZeroes2(nums2)  # 直接修改 nums2，但不回傳值
print(nums2)  # 正確輸出: [1, 3, 12, 0, 0]
