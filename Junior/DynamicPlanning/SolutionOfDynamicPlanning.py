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
    # Hint: 普通计算
    def ClimbStairs2(n = 3) -> int:
        if (n == 1):
            return 1
        else:
            value = [0 for i in range(n + 1)]
            value[1] = 1
            value[2] = 2
            for i in range (3,n + 1):
                value[i] = value[i-1] + value[i-2]
            return value[n]
    # Hint: 避免使用数组，使用三个数交替运算
    def ClimbStairs3(n = 3) -> int:
        i = 0
        j = 1
        for index in range(n):
            k = i + j
            i = j
            j = k
        return k

    # ~~~~~买卖股票的最佳时机 I~~~~~
    # Link: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn8fsh/
    # Hint: 双游标
    def MaxProfit1(prices = [2,4,1]) -> int:
        if (len(prices) == 0):
            return 0
        maxValue = 0
        minPrice = prices[0]
        for index in range (1, len(prices)):
            minPrice = min(minPrice, prices[index])
            maxValue = max(maxValue, prices[index] - minPrice)
            print(maxValue)
        return maxValue

        


# SolutionOfDynamicPlanning.ClimbStairs1()
# SolutionOfDynamicPlanning.ClimbStairs2()
# SolutionOfDynamicPlanning.ClimbStairs3()

SolutionOfDynamicPlanning.MaxProfit1()
