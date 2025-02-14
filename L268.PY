#給定一個包含 n 個不同數字的陣列 nums，這些數字範圍為 [0, n]，找出缺失的那個數字。


def missingNumber(nums):
    nums = sorted(set(nums))  
    for i in range(len(nums) - 1):  # 避免索引溢出
        if nums[i] + 1 != nums[i + 1]:  
            return nums[i] + 1
    return nums[-1] + 1 if nums[0] == 0 else 0 

print(missingNumber([3, 0, 1]))  # 輸出 2
print(missingNumber([0, 1]))  # 輸出 2
print(missingNumber([9,6,4,2,3,5,7,0,1]))  # 輸出 8