class Solution:
    def isPalindrome(self,str, i, j):
        while i <= j:
            if str[i]!=str[j]:
                return False
            i+=1
            j-=1
        return True
    def addMinChar (self, str1):
        n = len(str1)
        for i in range(n - 1, -1, -1):
            if str1[0] == str1[i] and self.isPalindrome(str1, 0, i):
                return n - i - 1
        return 0