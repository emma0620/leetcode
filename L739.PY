#給定一個 temperatures 數組，每個元素代表一天的氣溫。對於每一天，找出 幾天後 才會遇到更高的氣溫。如果未來都沒有更高溫度，則返回 0

def dailyTemperatures(temperatures):
    res = [0] * len(temperatures)  # 初始化結果陣列
    stack = []  # 存放索引（維持單調遞減）

    for i, temp in enumerate(temperatures):
        # 當前溫度比棧頂溫度高，更新結果
        while stack and temperatures[stack[-1]] < temp:
            prev_index = stack.pop()  # 彈出棧頂
            res[prev_index] = i - prev_index  # 計算相差天數

        stack.append(i)  # 當前索引入棧
    
    return res

temps = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(temps))

# Step 1:  [73]  ➝ 入棧
# Step 2:  [74]  ➝ 73 出棧，res[0] = 1
# Step 3:  [75]  ➝ 74 出棧，res[1] = 1
# Step 4:  [75, 71]  ➝ 71 入棧
# Step 5:  [75, 71, 69]  ➝ 69 入棧
# Step 6:  [75, 72]  ➝ 69 出棧，71 出棧，res[4] = 1, res[3] = 2
# Step 7:  [76]  ➝ 75 出棧，72 出棧，res[2] = 4, res[5] = 1
# Step 8:  [76, 73]  ➝ 73 入棧（因為後面沒更高溫）
