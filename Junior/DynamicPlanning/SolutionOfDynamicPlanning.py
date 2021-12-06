class SolutionOfDynamicPlanning:
    
    # ~~~~~爬楼梯~~~~~
    # Link: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn854d/
    # Hint: 斐波那契数列 第n项通项公式
    def ClimbStairs1(n = 3) -> int:
        if (n == 1):
            return 1
        elif (n == 2):
            return 2
        else:
            return int((((1 + 5**0.5)/2)**(n + 1) - ((1 - 5**0.5)/2)**(n + 1))/(5**0.5))
        


SolutionOfDynamicPlanning.ClimbStairs1()
