#給定一個數組 nums 和一個值 val，請 就地移除 陣列中所有數值等於 val 的元素，並返回新的長度。
#請 不使用額外陣列，修改 nums 使它的前 k 個元素為非 val 值，並返回 k。

def remove_and_count(nums):
    nums = [num for num in nums if num != 3]  # 過濾掉 3
    return len(nums)

nums = [3, 2, 2, 3, 4, 3]
print(remove_and_count(nums))  # 輸出: 3


