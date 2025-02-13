#給定一個長度為 n 的陣列 nums，其中的數字範圍是 1 到 n。有些數字出現了，有些數字沒出現，請找出所有沒有出現在 nums 中的數字。

def find_disappeared_numbers(nums):
    nums = sorted(set(nums))  # 去重並排序
    missing_nums = []

    for index in range(len(nums) - 1):  # 遍歷到倒數第二個數
        if nums[index] + 1 != nums[index + 1]:  # 如果不連續
            for missing in range(nums[index] + 1, nums[index + 1]):  # 補上遺漏的數字
                missing_nums.append(missing)
    
    return missing_nums

# 測試
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(find_disappeared_numbers(nums))  # 輸出：[5, 6]
