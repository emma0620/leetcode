
#給你一個數組 nums，對於每個數字 nums[i]，請找出陣列中 比它小的數字個數，並回傳結果數組

def smallerNumbersThanCurrent(nums):
    sorted_nums = sorted(nums)
    rank = {num: i for i, num in enumerate(sorted_nums)}
    return [rank[num] for num in nums]


nums = [8, 1, 2, 2, 3]
print(smallerNumbersThanCurrent(nums))