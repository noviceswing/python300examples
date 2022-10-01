# 反转3位数的整数

class Solution:
    def reverseInteger(self, number):
        B = int(number/100)
        S = int(number%100/10)
        G = int(number%10)
        return(G*100 + S*10 + B)

if __name__ == "__main__":
    solution = Solution()
    num = int(input('输入反转数字：'))
    ans = solution.reverseInteger(num)
    print(ans)

# 反转数字一般可用/和%来实现