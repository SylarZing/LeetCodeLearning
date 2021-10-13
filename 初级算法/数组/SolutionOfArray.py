class SolutionOfArray:
    
    # 删除排序数组中的重复项
    # 给你一个有序数组 nums ，请你删除重复出现的元素，使每个元素只出现一次 ，返回删除后数组的新长度。
    # 不要使用额外的数组空间，你必须修改输入数组,并在使用 O(1) 额外空间的条件下完成。
    def RemoveDuplicateItems(arr = [1,1,2,2,3,3,3]):
        index = len(arr) - 1
        pointer = len(arr) - 2
        
