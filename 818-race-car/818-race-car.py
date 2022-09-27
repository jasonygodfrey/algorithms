class Solution:
    def racecar(self, target: int) -> int:
        queue = collections.deque([(0, 0, 1)])
        visited = set()
        
        while queue:
            moves, position, speed = queue.popleft()
            
            if position == target:
                return moves
            if (position, speed) in visited:
                continue
            else:
                visited.add((position, speed))
                queue.append((moves + 1, position + speed, speed * 2))
                if (position + speed > target and speed > 0) or (position + speed < target and speed < 0):
                    speed = -1 if speed > 0 else 1
                    queue.append((moves + 1, position, speed))
                
        """ Here is the explanation for the code above:
1. The code uses a BFS algorithm to find the optimal path.
2. The queue is used to store the moves, position, and speed.
3. The visited set is used to prevent the code from entering an infinite loop.
4. The first while loop is used to iterate through the queue until it is empty.
5. The second while loop is used to iterate through the queue until it is empty.
6. The first if statement checks if the current position is equal to the target. If it is, then the function returns the number of moves.
7. The second if statement checks if the current position and speed has been visited. If it has, then the code continues to the next iteration.
8. The else statement adds the current position and speed to the visited set and appends the number of moves, position, and speed * 2 to the queue.
9. The third if statement checks if the current position and speed is greater than the target and if the speed is positive or if the current position and speed is less than the target and if the speed is negative. If it is, then the speed is changed to negative.
10. The fourth if statement appends the number of moves, position, and the new speed to the queue.
11. The function returns -1 if the target is not found.
12. The time complexity of the code above is O(n^2) where n is the target.
13. The space complexity of the code above is O(n^2) where n is the target. """