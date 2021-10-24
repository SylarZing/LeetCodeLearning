class SolutionOfArray:
    
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
        
    # ~~~~~两个数组的交集 II~~~~~
    # 给定两个数组，编写一个函数来计算它们的交集。
    # Hint: 先给数组排序，再双指针比较两个
    def Intersect(nums1=[1,2,3,4,5,4], nums2=[2,3,4,4]):
        list = []
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        while (i < len(nums1) and j < len(nums2)):
            if (nums1[i] < nums2[j]):
                i += 1
            elif (nums1[i] > nums2[j]):
                j += 1
            else:
                list.append(nums1[i])
                i += 1
                j += 1
        print(list)
        return list

    # ~~~~~加一~~~~~
    # 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
    # 最高位数字存放在数组的首位，数组中每个元素只存储单个数字。
    # 你可以假设除了整数 0 之外，这个整数不会以零开头。
    # Hint: 主要注意进位情况 [9,9] + 1 = [1,0,0]; 反向遍历数组，若需要进位，则赋0并判断下一位，否则直接加一
    def PlusOne(digits = [9]):
        index = 0
        for i in range(len(digits) - 1, -1, -1):
            print(digits[i])
            if (digits[i] == 9):
                digits[i] = 0
                index += 1
            else:
                digits[i] += 1
                break
        if (index == len(digits)):
            digits.insert(0, 1)
        print(digits)
    
    # ~~~~~两数之和~~~~~
    # 给定一个整数数组nums和一个整数目标值target，请你在该数组中找出和为目标值target的那两个整数，并返回它们的数组下标。
    # 你可以假设每种输入只会对应一个答案。但是数组中同一个元素在答案里不能重复出现。
    # 你可以按任意顺序返回答案。
    # Hint: 暴力破解 遍历就好
    def TwoSum1(nums = [1,2,3,4,5], target = 6):
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                    print([i, j])
                    return[i ,j]
    #Hint: 遍历一边nums[i],判断target - nums[i]是否在nums中
    def TwoSum2(nums = [1,2,3,4,5], target = 6):
        for i in range(len(nums) - 1, -1, -1):
            if (target - nums[i] in nums):
                index = nums.index(target - nums[i])
                print([i, index])
                return[i, index]

    # ~~~~~~旋转图像~~~~~~
    # 给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
    # 你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
    # Hint: 先上线调换，再以对角线数据调换
    def RotateImage1(matrix = [[1,2,3],[4,5,6],[7,8,9]]):
        matrix.reverse()
        for i in range(0, len(matrix)):
            for j in range(i, len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        print(matrix)
    # Hint: 根据题目要求按层一次旋转，前一个点坐标(i,j)，后一个点坐标(j,max-i)
    def RotateImage2(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]):
        max = len(matrix)
        row = int(max / 2)
        print(max)
        for i in range(0,row):
            j = i
            while (j < max - i - 1):
                times = 0
                cur_i = i
                cur_j = j
                temp = matrix[cur_i][cur_j]
                while(times<3):
                    pre_i = max - 1 - cur_j
                    pre_j = cur_i
                    matrix[cur_i][cur_j] = matrix[pre_i][pre_j]
                    cur_i = pre_i
                    cur_j = pre_j
                    times += 1
                matrix[cur_i][cur_j] = temp
                j += 1
        print(matrix)
        


        
    
    # 买卖股票的最佳时机
    # 给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。
    # 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
    # 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


        
# SolutionOfArray.RemoveDuplicateItems()

# SolutionOfArray.ContainDuplicateItem1()
# SolutionOfArray.ContainDuplicateItem2()

# SolutionOfArray.SingleItem()

# SolutionOfArray.MoveZero1()
# SolutionOfArray.MoveZero2()

# SolutionOfArray.Rotate()

# SolutionOfArray.Intersect()

# SolutionOfArray.PlusOne()

# SolutionOfArray.TwoSum1()
# SolutionOfArray.TwoSum2()

# SolutionOfArray.RotateImage1()
# SolutionOfArray.RotateImage2()