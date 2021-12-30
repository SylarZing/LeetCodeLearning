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
    # Hint: 双游标,一个记录当前最小值，同时记录一个当前最大利润（初始利润为0）
    def MaxProfit1(prices = [2,4,5,1]) -> int:
        if (len(prices) == 0):
            return 0
        maxValue = 0
        minPrice = prices[0]
        for index in range (1, len(prices)):
            minPrice = min(minPrice, prices[index])
            maxValue = max(maxValue, prices[index] - minPrice)
        print(maxValue)
        return maxValue
    # Hint: 动态规划
    def MaxProfit2(prices = [2,4,5,1]) -> int:
        # dp[i][0] -- i + 1 天结束时候没股票时的最大收益
        # dp[i][1] -- i + 1 天结束时候有股票时的最大收益
        
        # dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        # dp[i][1] = max(dp[i-1][1], -prices[i])
        # dp[0][0] = 0
        # dp[0][1] = -prices[0]
        length = len(prices)
        if (length == 0):
            return 0 
        unhold = 0
        hold = -prices[0]
        for i in range(1,length):
            unhold = max(unhold, hold + prices[i])
            hold = max(hold, -prices[i])
        print(unhold)
        return unhold

    # ~~~~~ 最大子序和 ~~~~~
    # Link: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn3cg3/
    # Hint: 动态规划
    def MaxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]) -> int:
        # dp[i] -- 表示数组中前i+1（注意这里的i是从0开始的）个元素构成的连续子数组的最大和
        # dp[i] = max(dp[i - 1], 0) + nums[i]
        length = len(nums)
        dp = [0] * length
        dp[0] = nums[0]
        maximum = dp[0]
        for i in range(1, length):
            if (dp[i - 1] > 0):
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]
            
        print(max(dp))
        return max(dp)
        








# SolutionOfDynamicPlanning.ClimbStairs1()
# SolutionOfDynamicPlanning.ClimbStairs2()
# SolutionOfDynamicPlanning.ClimbStairs3()

# SolutionOfDynamicPlanning.MaxProfit1()
# SolutionOfDynamicPlanning.MaxProfit2()

SolutionOfDynamicPlanning.MaxSubArray()