class Solution:
    def minEatingSpeed(self, piles, h):

        # Minimum possible eating speed
        low = 1

        # Maximum possible eating speed
        # (No need to eat faster than the biggest pile)
        high = max(piles)

        # Store the minimum valid answer
        ans = high

        # Binary Search
        while low <= high:

            # Middle eating speed
            mid = (low + high) // 2

            # Calculate total hours needed with speed = mid
            hours = 0

            for pile in piles:

                # Ceiling division
                # Example:
                # pile = 7, mid = 3
                # 7/3 = 2.33 -> needs 3 hours
                hours += (pile + mid - 1) // mid

            # If Koko can finish within h hours
            if hours <= h:

                # mid is a possible answer
                ans = mid

                # Try to find an even smaller speed
                high = mid - 1

            else:
                # Too slow, increase eating speed
                low = mid + 1

        return ans