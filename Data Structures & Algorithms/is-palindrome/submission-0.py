class Solution:
    def isPalindrome(self, s: str) -> bool:
    
    
        s = ''.join(char.lower() for char in s if char.isalnum())
      
        i=0
        for char in s:
            if s[i]!=s[-i-1]:
                return False
            i+=1    
        return True