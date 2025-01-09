class Solution: 
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        sign = -1 if x < 0 else 1

        reversed_str = str(abs(x))[::-1]
        reversed_num = int(reversed_str) * sign

        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0

        return reversed_num

solution = Solution()

print(solution.reverse(123))      
print(solution.reverse(-123))     
print(solution.reverse(120))      
print(solution.reverse(1234567889)) 
