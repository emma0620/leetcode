#給定一個整數數組 nums，請判斷是否存在任何重複的元素。如果任一值在陣列中至少出現一次，則返回 true，否則返回 false。

def containsDuplicate(nums):
     
    if len(nums) != len(set(nums)):
        return True
    return False


def containsDuplicate2(nums):
    seen = {}  
    for num in nums:
        if num in seen: 
            return True
        seen[num] = True 
    return False  

print("方法一")
print(containsDuplicate([1, 2, 3, 1]))  # 輸出: True (因為有重複的 1)
print(containsDuplicate([1, 2, 3, 4]))  # 輸出: False (沒有重複的元素)
print(containsDuplicate([1, 1, 1, 1]))  # 輸出: True (因為有重複的 1)
print("方法二")
print(containsDuplicate2([1, 2, 3, 1]))  # 輸出: True (因為有重複的 1)
print(containsDuplicate2([1, 2, 3, 4]))  # 輸出: False (沒有重複的元素)
print(containsDuplicate2([1, 1, 1, 1]))  # 輸出: True (因為有重複的 1)
