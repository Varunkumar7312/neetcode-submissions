class Solution:
    def findMin(self, nums):
        
        # Left pointer starts at the beginning
        left = 0
        
        # Right pointer starts at the end
        right = len(nums) - 1

        # Continue until both pointers meet
        while left < right:

            # Find the middle index
            mid = (left + right) // 2

            # If middle element is greater than the rightmost element,
            # the minimum must be in the right half.
            if nums[mid] > nums[right]:
                left = mid + 1

            # Otherwise, the minimum is at mid or in the left half.
            else:
                right = mid

        # When left == right, it points to the minimum element.
        return nums[left]