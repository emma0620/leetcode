# LeetCode 224: 基本計算器 (Basic Calculator)
# 題目描述：實現一個基本的計算器來解析一個只包含加號、減號、括號和非負整數的字串，並返回計算結果。要求支持括號的處理，需要在堆疊中處理嵌套括號的運算


def calculate(s: str) -> int:
    stack = []  # 用來存放符號和結果
    sign = 1  # 1表示加號，-1表示減號
    result = 0  # 最終結果
    current_num = 0  # 當前數字

    for char in s:
        if char.isdigit():
            # 如果字符是數字，則組成當前數字
            current_num = current_num * 10 + int(char)
        elif char == "+":
            # 如果是加號，則更新結果並重置當前數字
            result += sign * current_num
            current_num = 0
            sign = 1  # 更新符號為加號
        elif char == "-":
            # 如果是減號，則更新結果並重置當前數字
            result += sign * current_num
            current_num = 0
            sign = -1  # 更新符號為減號
        elif char == "(":
            # 遇到左括號，將當前結果和符號入堆疊
            stack.append(result)
            stack.append(sign)
            result = 0  # 重置結果
            sign = 1  # 重置符號為加號
        elif char == ")":
            # 遇到右括號，先將當前結果加到堆疊中
            result += sign * current_num
            current_num = 0
            result *= stack.pop()  # 拿出符號並處理
            result += stack.pop()  # 拿出之前保存的結果

    # 最後記得把最後一個數字加進去
    result += sign * current_num
    return result


print(calculate("1 + 1"))  # 2
print(calculate(" 2-1 + 2 "))  # 3
print(calculate("(1+(4+5+2)-3)+(6+8)"))  # 23
