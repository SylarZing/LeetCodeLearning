class SolutionOfString:
    # ~~~~~翻转字符串~~~~~
    # 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。
    # 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
    # Hint: 不使用库函数，收尾交换
    def ReverseString(s = ["H","a","n","n","a"]):
        
        length = len(s)
        count = (int)(length / 2)
        
        for index in range(0, count):
            tmp = s[index]
            s[index] = s[length - 1 - index]
            s[length - 1 - index] = tmp
        print(s)
        return

    # ~~~~~整数翻转~~~~~
    # Link: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnx13t/
    # Hint: 利用求余,反算每一位数字
    def ReverseInt1(x = -12) -> int:
        result = 0
        flag = x > 0
        if (not flag):
            x = x * -1

        while(x != 0):
            a = x % 10
            x = (int)(x / 10)
            result = result * 10 + a
            
        if (not flag):
            result = result * -1

        if -2**31 <= result <= 2**31 - 1:
            return result
        else:
            return 0
    # Hint: 利用字符串转换
    def ReverseInt2(x = -12) -> int:
        flag = x > 0
        if (not flag):
            x = x * -1
        strInt = str(x)
        strInt = strInt[::-1]
        result = int(strInt)
        if (not flag):
            result = result * -1
        
        if -2**31 <= result <= 2**31 - 1:
            return result
        else:
            return 0

    # ~~~~~字符串中的第一个唯一字符~~~~~
    # Link: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn5z8r/
    # Hint: 使用find和rfind
    def FirstUniqChar(s = "loveleetcode") -> int:
        for c in s:
            if s.find(c) == s.rfind(c):
                return s.find(c)
        return -1

    # ~~~~~验证回文串~~~~~
    # Link: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xne8id/
    # Hint: 双指针，同时正向反向对比字符
    def IsPalindrome(s = "Level") -> bool:
        if len(s) == 0:
            return True
        left = 0
        right = len(s) - 1
        while(left < right):
            while(left < right and s[left].isalnum() == False):
                left += 1
            while(left < right and s[right].isalnum() == False):
                right -= 1
            if (s[left].lower() != s[right].lower()):
                return False
            left += 1
            right -= 1
        return True
     
    # ~~~~~ 有效的字母异位词 ~~~~~
    # Link: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn96us/
    # Hint: 利用Dictionary整理字符出现次数并比较
    def IsAnagram(s = "aabc", t = "ccba") -> bool:
        if (len(s) != len(t)):
            return False
        sDic = {}
        tDic = {}
        for i in range(0, len(s), 1):
            if s[i] in sDic.keys():
                sDic[s[i]] += 1
            else:
                sDic[s[i]] = 1
        for i in range(0, len(t), 1):
            if t[i] in tDic.keys():
                tDic[t[i]] += 1
            else:
                tDic[t[i]] = 1
        return sDic == tDic
    
    # ~~~~~ 字符串转换整数 (atoi) ~~~~~
    # Link: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnoilh/
    # Hint: 按照题目要求依次判断
    def MyAtoi(s = "42") -> int:
        s = s.strip()
        if (len(s) == 0):
            return 0
        str = ""
        flag = True
        index = 0

        if (s[0] == '-'):
            flag = False
            index = 1
        elif(s[0] == '+'):
            flag = True
            index = 1

        for i in range(index, len(s)):
            if (s[i].isnumeric()):
                str = str + s[i]
            else:
                break
        if (str == ""):
            r = 0
        else:
            r = int(str)
        print(str)
        if flag:
            if r > (2 ** 31) - 1:
                return (2 ** 31) - 1
            return r
        else:
            if r > 2 ** 31:
                return 0 - (2 ** 31)
            return 0 - r
        


# SolutionOfString.ReverseString()

# SolutionOfString.ReverseInt1()
# SolutionOfString.ReverseInt2()

# SolutionOfString.FirstUniqChar()

# SolutionOfString.IsPalindrome()

# SolutionOfString.IsAnagram()

# SolutionOfString.MyAtoi()