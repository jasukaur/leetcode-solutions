class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        
        graph = collections.defaultdict(list)

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        print(graph)

        seen = [False] * n

        def dfs(curr_node):
            if curr_node == destination:
                return True

            if not seen[curr_node]:
                seen[curr_node] = True
                for next_node in graph[curr_node]:
                    if dfs(next_node):
                        return True
            return False
        return dfs(source)
            
            
# This is with DFS