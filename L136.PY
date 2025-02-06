#給定一個非空的整數陣列 nums，除了 一個元素 只出現 一次，其他元素都出現 兩次。請找出這個 只出現一次的數字。

def singleNumber2(nums):
    return 2 * sum(set(nums)) - sum(nums)

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num  # XOR 運算
    return result


nums = [4, 1, 2, 1, 2]
print("方法一")
print(singleNumber(nums))

print("方法二")
print(singleNumber2(nums))


