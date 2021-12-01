class SolutionOfSortAndSearch:
    # ~~~~~ 合并两个有序数组 ~~~~~
    # Link: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnumcr/
    # Hint: 归并排序
    def Merge1(self, nums1=[2,0], m=1, nums2 = [1], n = 1):
        i = 0
        j = 0
        result = []
        while (i < m or j < n):
            if (len(nums2) == 0):
                result.append(nums1[i])
                i += 1
            elif (i == m):
                result.append(nums2[j])
                j += 1
            elif (j == n or nums1[i] < nums2[j]):
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        for index in range (0,len(result)):
            nums1[index] = result[index]
        print(nums1)
    # Hint: 先合并再排序
    def Merge2(self, nums1=[2,0], m=1, nums2 = [1], n = 1):
        if (len(nums2) != 0):
            for index in range(0, len(nums2)):
                nums1[m + index] = nums2[index]
            nums1.sort()
        print(nums1)

    # ~~~~~第一个错误的版本~~~~~
    # Link: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnto1s/
    # Hint: 二分法
    def isBadVersion(self, version:int):
        if (version >= 2):
            return True
        else:
            return False
    
    def firstBadVersion(self, n = 8):
        start = 1
        end = n
        while (start <= end):
            index = (start + end) // 2
            if (self.isBadVersion(index)):
                end = index - 1
            else:
                start = index + 1
        print(start)
        return start


solution = SolutionOfSortAndSearch()

# solution.Merge1()
# solution.Merge2()

solution.firstBadVersion()