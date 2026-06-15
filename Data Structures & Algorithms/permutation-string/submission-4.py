class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Step 1: Length check
        if len(s1) > len(s2):
            return False

        # Step 2: Frequency arrays (26 lowercase letters)
        s1_count = [0] * 26
        window_count = [0] * 26

        # Step 3: Fill frequency of s1 and first window of s2
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1

        # Step 4: Check initial window
        if s1_count == window_count:
            return True

        # Step 5: Slide the window
        left = 0
        for right in range(len(s1), len(s2)):
            # add new character (right)
            window_count[ord(s2[right]) - ord('a')] += 1

            # remove old character (left)
            window_count[ord(s2[left]) - ord('a')] -= 1
            left += 1

            # check match
            if s1_count == window_count:
                return True

        return False