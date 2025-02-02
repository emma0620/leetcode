#給定一個整數陣列 arr，請判斷每個數字的出現次數是否都是唯一的（沒有兩個數字的出現次數相同）。如果是，回傳 True，否則回傳 False。


from collections import Counter

def uniqueOccurrences(arr):
    count = Counter(arr)  # 計算每個數字的出現次數
    occurrences = list(count.values())  # 取得所有出現次數
    return len(occurrences) == len(set(occurrences))  # 判斷是否所有出現次數都唯一


def uniqueOccurrences2(arr):
    # 計算每個數字的出現次數
    count = {}
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    # 檢查出現次數是否唯一
    occurrences = list(count.values())  # 取得所有出現次數

    return len(occurrences) == len(set(occurrences))  # 判斷是否所有出現次數都唯一

# 測試
print("方法一")
print(uniqueOccurrences([1, 2, 2, 1, 1, 3]))  # True
print(uniqueOccurrences([1, 2, 2, 1, 1, 3, 3, 3]))  # False
print("方法二")
print(uniqueOccurrences2([1, 2, 2, 1, 1, 3]))  # True
print(uniqueOccurrences2([1, 2, 2, 1, 1, 3, 3, 3]))  # False

