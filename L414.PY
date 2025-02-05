


def secondLargest(nums):
    unique_nums = sorted(set(nums))  # 移除重複值並排序
    return unique_nums[-2] if len(unique_nums) > 1 else -1



print(secondLargest([1, 2, 3, 4]))    # 輸出: 3
print(secondLargest([4, 1, 2, 2, 3])) # 輸出: 3
print(secondLargest([7, 7, 7, 7]))    # 輸出: -1
print(secondLargest([5]))             # 輸出: -1