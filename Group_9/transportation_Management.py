"""
Stephen Villagonzalo
Part 3: Transportation Management
"""

import collections

class Solution:
    def racecar(self, target: int) -> int:
        queue = collections.deque([(0, 0, 1)])
        visited = set()

        while queue:
            steps, position, speed = queue.popleft()

            if position == target:
                return steps

            if (position, speed) in visited:
                continue
            else:
                visited.add((position, speed))

                queue.append((steps+1,position+speed,speed*2))

                if (position + speed < target and speed < 0):
                    queue.append((steps + 1,position, 1))
                elif (position + speed > target and speed > 0):
                    queue.append((steps + 1, position, -1))
