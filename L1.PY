
def twoSum(nums, target):
    index_map = {}  # 用於記錄數值 -> 索引的對應
    for i, num in enumerate(nums):
        diff = target - num
        # 檢查差值是否已在 index_map 中
        if diff in index_map:
            return [index_map[diff], i]  # 返回匹配的索引
        # 將目前的數值及其索引記錄到字典
        index_map[num] = i

def twoSum_2(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]+nums[j]==target:
                return i, j
     



# 測試範例
nums = [2, 7, 11, 15]
target = 9
print(f"方法一 {twoSum(nums, target)}")  # 輸出 [0, 1]
print(f"方法二 {twoSum_2(nums, target)}")  # 輸出 [0, 1]

