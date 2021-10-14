class SolutionOfArray:
    
    # 删除排序数组中的重复项
    # 给你一个有序数组 nums ，请你删除重复出现的元素，使每个元素只出现一次 ，返回删除后数组的新长度。
    # 不要使用额外的数组空间，你必须修改输入数组,并在使用 O(1) 额外空间的条件下完成。
    # Hint: 由于数组是有序的，比较相邻两个数是否相等。
    def RemoveDuplicateItems(arr = [1,1,2,2,3,3,3,5,6,6]):
        for index in range(len(arr) - 1, 0, -1):
            if arr[index - 1] == arr[index]:
                del(arr[index])
        print(len(arr))
        print(arr)

    # 存在重复元素
    # 给定一个整数数组，判断是否存在重复元素。
    # 如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false。
    # Hint：使用集合元素的唯一性，判断放入集合后元素数量和遍历的次数是否一致
    def ContainDuplicateItem1(arr = [1,2,3,1]):
        list = {arr[0]} 
        result = False
        for i in range(1, len(arr), 1):
            list.add(arr[i])
            if len(list) != i + 1:
                result = True
                break
        print(result)
    # Hint: 先排序再比较相邻 - **内存消耗较低
    def ContainDuplicateItem2(arr = [1,2,3,1]):
        arr.sort()
        result = False
        for i in range(1, len(arr), 1):
            if(arr[i - 1] == arr[i]):
                result = True
        print(result)


    
    
    # 买卖股票的最佳时机
    # 给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。
    # 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
    # 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


        
# SolutionOfArray.RemoveDuplicateItems()

# SolutionOfArray.ContainDuplicateItem1()
# SolutionOfArray.ContainDuplicateItem2()