class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        prereqs_to_courses = defaultdict(list)
        courses_to_prereqs = defaultdict(list)

        for course, prereq in prerequisites:
            courses_to_prereqs[course].append(prereq)
            prereqs_to_courses[prereq].append(course)


        taken = []
        q = deque()
        for course in range(numCourses):
            if course not in courses_to_prereqs:
                taken.append(course)
                q.append(course)

        while q:
            for i in range(len(q)):
                course = q.popleft()
                
                for i in prereqs_to_courses[course]:
                    courses_to_prereqs[i].remove(course)
                    if len(courses_to_prereqs[i]) == 0:
                        q.append(i)
                        taken.append(i)
            
        if len(taken) == numCourses:
            return taken
        return []
            