class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        count={}
        max_count=0
        answer=0

        for right in range(len(s)):
            char=s[right]
            count[char]=count.get(char,0)+1
            max_count=max(max_count, count[char])

            while(right-left+1)-max_count>k:
                left_char=s[left]
                count[left_char]-=1
                left+=1

            answer=max(answer,right-left+1)
        return answer                        
            
        