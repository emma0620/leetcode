#給定兩個整數陣列 nums1 和 nums2，請回傳它們的 交集（重複元素只計算一次）。

def intersection(nums1, nums2):
    nums1 = set(nums1)  
    nums2 = set(nums2)  
    seen = [] 
    
    for num in nums1:  
        if num in nums2:  
            seen.append(num)  
    
    return seen 

def intersection2(nums1, nums2):
    return list(set(nums1) & set(nums2))  # 使用 & 取得交集

nums1 = [1,2,2,1]
nums2 = [2,2]

nums3 = [4,9,5]
nums4 = [9,4,9,8,4]

print("方法1")
print(intersection(nums1, nums2))
print(intersection(nums3, nums4))
print("方法2")
print(intersection2(nums1, nums2))
print(intersection2(nums3, nums4))