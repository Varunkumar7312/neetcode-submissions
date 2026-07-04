from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        box = deque()
        ans = []

        for i in range(len(nums)):

            # remove out-of-window index
            if box and box[0] <= i - k:
                box.popleft()

            # remove smaller elements
            while box and nums[box[-1]] < nums[i]:
                box.pop()

            box.append(i)

            if i >= k - 1:
                ans.append(nums[box[0]])

        return ans