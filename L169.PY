#給定一個大小為 n 的陣列 nums，找到其中的多數元素（出現次數超過 ⌊n/2⌋）

from collections import Counter

def majorityElement(nums):
    counts = Counter(nums)  # 計算每個數字出現的次數
    for num, count in counts.items():
        if count > len(nums) / 2:
            return num  # 回傳多數元素
        


def majorityElement2(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:  
            candidate = num  # 設定新候選人
        
        if num == candidate:
            count += 1 
        else:
            count-=1  # 相同 +1，不同 -1
        print(num, count)

    return candidate

print("方法一")
print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,1,2,2]))

print("方法二")
print(majorityElement2([3,2,3]))
print(majorityElement2([2,2,1,1,1,2,2]))

#Boyer-Moore 投票法
#如果 count = 0，我們就丟掉之前的 candidate，改選新 candidate
# 這意味著 相等數字的累計票數大於不同數字的總票數，才不會被淘汰。
# 因此，最終能夠存活下來的候選人，就是出現次數最多的數字。
# 因為多數元素的出現次數比所有其他數的總和還要多

# 假設多數元素 M 出現 k 次，其他元素加起來也是 k-1 次，
# count 不會歸零，最終 M 會存活。