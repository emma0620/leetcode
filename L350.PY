#給定兩個數組 nums1 和 nums2，請找出它們的交集元素，並且每個元素的出現次數與其在數組中最少出現次數相同

from collections import Counter

def intersect(nums1, nums2):
    count1 = Counter(nums1)  # 記錄 nums1 每個數字的出現次數
    result = []

    for num in nums2:
        if count1[num] > 0:  # 若該數字在 nums1 中還有剩餘數量
            result.append(num)
            count1[num] -= 1  # 減少數量

    return result


nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersect(nums1, nums2))


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersect(nums1, nums2))# 交集是 [4,9]，順序不固定
