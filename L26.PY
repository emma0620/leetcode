#給定一個 非遞減排序 的整數數組 nums，原地移除重複數字，並回傳 移除後的數組長度。你不能使用額外的陣列，必須直接修改 nums

def removeDuplicates(nums):
    if not nums:
        return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1


print(removeDuplicates([1, 1, 2]))
print(removeDuplicates([1, 1, 2, 3, 4, 4]))