class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[]

        for i in range(len(nums)):
            val =1

            for j in range(len(nums)):

                if i!=j:
                    val=val*nums[j]
            result.append(val)
        return result    


        