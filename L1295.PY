# 給定一個數組 nums，請找出其中「擁有偶數位數」的數字個數。

# 這裡的 「偶數位數」 是指 這個數字的長度（位數）是偶數，而 不是數字本身是偶數

def findNumbers(nums):
    count = 0
    for num in nums:
        if len(str(num)) % 2 == 0:  
            count += 1
    return count

# 測試
nums = [12, 345, 2, 6, 7896]
print(findNumbers(nums))  # Output: 2
