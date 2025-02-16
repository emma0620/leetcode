#給定一個長度為 n+1 的數組 nums，其中的數字範圍為 1 到 n，且 只有一個數字重複出現至少一次，請找出這個重複的數字

def findDuplicate(nums):
    seen = set()  # 用來存放出現過的數字
    for num in nums:
        if num in seen:  # 如果已經出現過，回傳這個數字
            return num
        seen.add(num)  # 沒出現過就加入集合
    return -1  


nums = [3, 1, 3, 4, 2]
print(findDuplicate(nums))  # 輸出: 3

nums = [1, 3, 4, 2, 2]
print(findDuplicate(nums))  # 輸出: 2