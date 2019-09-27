#------------------------------FirstTry-----------------------超出时间限制（4000ms）->暴力不可取！
class Solution:
    def longestPalindrome(self, s: str) -> str:
        leng=len(s)
        if leng==0:
            return s
        for i in range(leng):
            for j in range(i+1):
                new_s=s[j:j+leng-i]
                if self.isPalindrome(new_s):
                    return new_s
                                
    def isPalindrome(self,s:str):
        i=0
        j=len(s)-1
        while i<j:
            if s[i]!=s[j]:
                return False
            i=i+1
            j=j-1
        return True
#--------------------------SecondTry,DP--------------------------超出时间限制（450ms)
import numpy as np

class Solution:
    def longestPalindrome(self, s: str) -> str:
        length=len(s)
        max_len=0
        start=0
        end=1
        if length==0:
            return s
        else:
            pal=np.zeros((length,length),dtype=bool)
        if length>=1:
            for i in range(length):
                pal[i][i]=True
        if length>=2:
            for i in range(length-1):
                pal[i][i+1]=(s[i]==s[i+1])
                if pal[i][i+1]:max_len,start,end=2,i,i+1+1
        if length>=3:
            for i in range(length-2):
                pal[i][i+2]=(s[i]==s[i+2])
                if pal[i][i+2]:max_len,start,end=3,i,i+2+1
        if length>=4:
            for k in range(length):
                for i in range(length-3-k):
                    pal[i][i+3+k]=(s[i]==s[i+3+k])and pal[i+1][i+2+k]
                    if 3+k+1>max_len and pal[i][i+3+k]:max_len,start,end=4+k,i,i+3+k+1
        return s[start:end]

#-----------------------------------Key-----------------------------------------
class Solution:
    def longestPalindrome(self,s):
        str_length = len(s)
        max_length = 0
        start = 0
        for i in range(str_length):
            if i - max_length >= 1 and s[i - max_length - 1:i + 2] == s[i - max_length - 1:i + 2][::-1]:
                start = i - max_length - 1
                max_length += 2
                continue
            if i - max_length >= 0 and s[i - max_length:i + 2] == s[i - max_length:i + 2][::-1]:
                start = i - max_length
                max_length += 1
        return s[start:start + max_length+1]

