class Solution:
    def trap(self, height: List[int]) -> int:
        water=0
      
        for i in range(len(height)):
            left_max  = max(height[:i+1])
            right_max = max(height[i:])
            water_at_i=min(left_max,right_max)-height[i]
            water+=max(0,water_at_i)
        return water    
