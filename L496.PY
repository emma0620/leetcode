#給定兩個沒有重複元素的數組 nums1 和 nums2，其中 nums1 是 nums2 的子集。對於 nums1 中的每個元素 x，找到 nums2 中第一個大於 x 的數字，否則返回 -1。

def nextGreaterElement(nums1, nums2):
    stack = []
    greater_map = {}  # 記錄 nums2 中每個數的下一個更大元素
    
    for num in nums2:
        while stack and stack[-1] < num:
            smaller = stack.pop()
            greater_map[smaller] = num  # 記錄下一個更大值
        stack.append(num)

    return [greater_map.get(num, -1) for num in nums1]  # 沒找到則回傳 -1


def nextGreaterElement2(nums1, nums2):
    results = []
    
    for num in nums1:
        found = False  # 是否找到 num 在 nums2 的位置
        next_greater = -1  # 預設為 -1
        for j in range(len(nums2)):
            if nums2[j] == num:
                found = True  # 找到 num 在 nums2 的位置
            if found and nums2[j] > num:
                next_greater = nums2[j]
                break  # 找到後跳出迴圈
        results.append(next_greater)
    
    return results

# 測試
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print("方法一")
print(nextGreaterElement(nums1, nums2))  # [-1, 3, -1]

print("方法二")
print(nextGreaterElement2(nums1, nums2))  # [-1, 3, -1]
