class SolutionOfnumsay:
    
    # ~~~~~删除排序数组中的重复项~~~~~
    # 给你一个有序数组 nums ，请你删除重复出现的元素，使每个元素只出现一次 ，返回删除后数组的新长度。
    # 不要使用额外的数组空间，你必须修改输入数组,并在使用 O(1) 额外空间的条件下完成。
    # Hint: 由于数组是有序的，比较相邻两个数是否相等。
    def RemoveDuplicateItems(nums = [1,1,2,2,3,3,3,5,6,6]):
        for index in range(len(nums) - 1, 0, -1):
            if nums[index - 1] == nums[index]:
                del(nums[index])
        print(len(nums))
        print(nums)

    # ~~~~~存在重复元素~~~~~
    # 给定一个整数数组，判断是否存在重复元素。
    # 如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false。
    # Hint：使用集合元素的唯一性，判断放入集合后元素数量和遍历的次数是否一致
    def ContainDuplicateItem1(nums = [1,2,3,1]):
        list = {nums[0]} 
        result = False
        for i in range(1, len(nums), 1):
            list.add(nums[i])
            if len(list) != i + 1:
                result = True
                break
        print(result)
    # Hint: 先排序再比较相邻 - **内存消耗较低
    def ContainDuplicateItem2(nums = [1,2,3,1]):
        nums.sort()
        result = False
        for i in range(1, len(nums), 1):
            if(nums[i - 1] == nums[i]):
                result = True
        print(result)

    # ~~~~~只出现一次的数字~~~~~
    # 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
    # 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
    # Hint: 由于只有一个元素唯一存在，其余均是成对出现，利用异或的位运算a^a=0, 0^b=b
    def SingleItem(nums = [1,2,1,3,3]):
        result = 0
        for i in range(0, len(nums), 1):
            result = result ^ nums[i]
        print(result)

    # ~~~~~移动零~~~~~
    # 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
    # 1.必须在原数组上操作，不能拷贝额外的数组。
    # 2.尽量减少操作次数
    # Hint: 反向遍历数组，删除0元素并在数组结尾添加。
    def MoveZero1(nums = [0,3,4,0,3,6,3,0]):
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
        print(nums)
    # Hint: 冒泡排序
    # count为0的个数，i为游标。遍历整个数组。
    # 当第i个值=0是count+1,
    # 当第i个值!=0且存在0元素时时，把该值赋予第i-count个元素并把第i个元素设为0。 [重要]
    def MoveZero2(nums = [0,3,4,0,3,6,3,0]):
        count = 0
        for i in range(0, len(nums), 1):
            if nums[i] == 0:
                count = count + 1
            elif count != 0:
                nums[i - count] = nums[i]
                nums[i] = 0
        print(nums)

    # ~~~~~旋转数组~~~~~
    # 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
    # 进阶：
    # 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
    # 你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？
    # Hint: 先判移动次数，再将前端数组截取拼接到数组后端
    def Rotate(nums = [1,2,3,4,5,6,7], k = 3):
        index = k%len(nums)
        nums[:] = nums[-index:] + nums[:-index]
        


        
    
    # 买卖股票的最佳时机
    # 给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。
    # 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
    # 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


        
# SolutionOfnumsay.RemoveDuplicateItems()

# SolutionOfnumsay.ContainDuplicateItem1()
# SolutionOfnumsay.ContainDuplicateItem2()

# SolutionOfnumsay.SingleItem()

# SolutionOfnumsay.MoveZero1()
# SolutionOfnumsay.MoveZero2()

# SolutionOfnumsay.Rotate()