# LeetCode 227: 基本計算器 II
# 題目描述：
# 實現一個基本的計算器來解析並計算只包含正整數和四種基本運算符 (+, -, *, /) 的字串。不帶括號，但要考慮運算符的優先順序（乘除優先於加減）。輸入的字串可能包含空格

def calculate(s: str) -> int:
    stack = []
    current_num = 0
    operation = "+"  # 記錄當前的運算符
    
    for i, char in enumerate(s):
        # 如果是數字，累積到 current_num
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        
        # 如果是運算符或最後一個字符，執行當前的運算
        if char in "+-*/" or i == len(s) - 1:
            if operation == "+":
                stack.append(current_num)
            elif operation == "-":
                stack.append(-current_num)
            elif operation == "*":
                stack.append(stack.pop() * current_num)
            elif operation == "/":
                # 注意 Python 的整數除法，需向零取整
                stack.append(int(stack.pop() / current_num))
            
            # 更新運算符並重置 current_num
            operation = char
            current_num = 0

    return sum(stack)

# 測試
print(calculate("3+2*2"))  # 7
print(calculate(" 3/2 "))  # 1
print(calculate(" 3+5 / 2 "))  # 5
