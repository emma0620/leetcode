#給定一個整數陣列 nums 和一個整數 k，請判斷數組中是否存在兩個相同的元素，且它們的索引差至多為 k

def containsNearbyDuplicate(nums, k):
    seen = {}  # 用字典來存儲元素及其索引
    for i, num in enumerate(nums):
        if num in seen and i - seen[num] <= k:  # 發現相同元素且索引差在 k 內
            return True
        seen[num] = i  # 更新該數字的索引
    return False

nums = [1,2,3,1]
k = 3
print(containsNearbyDuplicate(nums, k))