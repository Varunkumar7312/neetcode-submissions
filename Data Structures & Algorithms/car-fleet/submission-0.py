class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)  # Sort by position (closest to target first)

        stack = []

        for pos, spd in cars:
            time = (target - pos) / spd

            stack.append(time)

            # If the current car catches the fleet ahead,
            # merge it with that fleet.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)