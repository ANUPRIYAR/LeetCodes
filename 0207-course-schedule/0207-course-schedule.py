from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # construct adj list
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[a].append(b)


        indegree = [0]* numCourses
        for i in range(numCourses):
            for prereq in adj[i]:
                indegree[prereq] += 1
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] ==0:
                queue.append(i)

        count = 0
        while queue:
            course = queue.popleft()
            count += 1

            for child in adj[course]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)

        
        if count== numCourses:
            return True

        return False