class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        reqs_list = {}
        self.numCourses = numCourses            
        self.taken = set()


        for course in prerequisites:
            if course[0] not in reqs_list:
                reqs_list[course[0]] = set()
            if course[1] not in reqs_list:
                reqs_list[course[1]] = set()
            reqs_list[course[0]].add(course[1])

        self.visited = set()
        for course in range(0, numCourses):
            if not self.dfs(course, reqs_list, prerequisites):
                return False

        return True
        
    def dfs(self, course, reqs_list, prerequisites):
        
        if course in self.visited:
            return False

        if course in self.taken:
            return True 

        self.visited.add(course)

        for prereq in reqs_list.get(course, set()):
            if not self.dfs(prereq, reqs_list, prerequisites):
                return False
        self.visited.remove(course)
        self.taken.add(course)

        return True