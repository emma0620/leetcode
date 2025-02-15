#給定一個排序好的不重複整數陣列 nums，請將連續的數字合併成區間，輸出區間格式的字串。如果數字是單獨的，就直接輸出該數字

def summaryRanges(nums):
    if not nums:
        return []
    
    result = []
    start = nums[0]  # 區間起點

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1] + 1:  # 如果當前數字不是前一個數字 +1
            if start == nums[i - 1]:
                result.append(str(start))  
            else:
                result.append(f"{start}->{nums[i - 1]}")  # 形成區間

            start = nums[i]  # 更新新的區間起點
    
    # 最後一個區間
    if start == nums[-1]:
        result.append(str(start))
    else:
        result.append(f"{start}->{nums[-1]}")

    return result

# 測試範例
nums = [0, 1, 2, 4, 5, 7] 
print(summaryRanges(nums))  
# 輸出：["0->2", "4->5", "7"]
