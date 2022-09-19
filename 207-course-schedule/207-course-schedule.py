class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visitSet.remove(crs)
            preMap[crs] = []
            
            return True
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
    
    """ Here is the explanation for the code above:
1. create a dictionary to record the prerequisites of each course
2. create a set to record the visited courses in the dfs process
3. create a dfs function to explore the prerequisites of the current course
4. for each course, if it is in the visited set, that means it is a loop, return False
5. if the current course does not have any prerequisites, return True
6. if the current course has prerequisites, go to the dfs function and explore the prerequisites
7. if the dfs function returns False, that means there is a loop in the prerequisites, return False
8. if the dfs function returns True, that means the current course is valid, remove it from the visited set, and remove it from the prerequisites dictionary
9. for each course, do the dfs and check if it is valid
10. if there is a loop in the prerequisites, the dfs will return False, so return False
11. if there is no loop in the prerequisites, the dfs will return True for each course, so return True """