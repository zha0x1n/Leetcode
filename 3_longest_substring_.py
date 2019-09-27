#--------------------------------------------------
class Solution:
    def lengthOfLongestSubstring(self, s):
        num_max=0
        i,j,k=0,0,0
        list=[]
        num=[]
        dic={}
        for i in range(len(s)):
            if s[i] not in list:
                dic[s[i]]=i
                num_max+=1
                list.append(s[i])
                num.append(num_max)
            else:
                num.append(num_max)
                num_max=i-dic[s[i]]
                list=list[dic[s[i]]-k+1:]
                k=dic[s[i]]+1
                dic[s[i]]=i         
                list.append(s[i])
        return max(num,default=0)

#---------------------------KEY1------------------------
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans;
#---------------------------KEY2-------------------------
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_number = 0
        number = 0
        test = ''
        for i in s:
            if i not in test:
                test += i
                number += 1
            else:
                if number >= max_number:
                    max_number = number
                index = test.index(i)
                test = test[(index+1):] + i
                number = len(test)
        if number > max_number:
            max_number = number
        return max_number
