# 5. **Best Time to Buy and Sell Stock (LeetCode 121)**  
#    - 找到買賣股票的最佳時機（只允許一次交易）。  
#    - **考點：** 單調隊列、數組遍歷。


# 使用 min(prices) 和 max(prices)（錯誤解法）
def maxProfit_wrong(prices):
    return max(prices) - min(prices)

# 使用遍歷更新最低價格（正確解法）
def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)
    return max_profit

# 測試
prices1 = [7, 1, 5, 3, 6, 4]
prices2 = [7, 6, 4, 3, 1]

print(maxProfit_wrong(prices1))  # 6 - 1 = 5 (正確結果，但僥倖)
print(maxProfit_wrong(prices2))  # 7 - 1 = 6 (錯誤結果)
print(maxProfit(prices1))        # 5 (正確)
print(maxProfit(prices2))        # 0 (正確)
