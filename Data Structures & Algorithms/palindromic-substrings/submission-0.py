class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.isPalindrome(s[i:j+1]):
                    count += 1
                    print(s[i:j])
        return count 
    
    def isPalindrome(self,str):
        if len(str) == 1:
            return True
        
        i,j = 0, len(str)-1
        while i < j:
            if str[i] != str[j]:
                return False
            i += 1
            j -= 1
        return True


        