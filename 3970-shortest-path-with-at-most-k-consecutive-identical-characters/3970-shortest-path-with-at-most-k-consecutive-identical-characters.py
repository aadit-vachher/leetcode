class Solution:
    def shortestPath(self, n, edges, labels, k):
        graph = defaultdict(list)

        for u,v,w in edges:
            graph[u].append([v,w])

        ans = [[0,0,1]]

        dict1 = defaultdict(int)

        for i in range(n):
            for j in range(k+1):
                dict1[(i,j)] = float("inf")

        dict1[(0,1)] = 0 

        while ans:
            w,node,cnt = heapq.heappop(ans)

            for neighbor,weight in graph[node]:
                if labels[node] == labels[neighbor]:
                    if cnt+1 <= k and dict1[(neighbor,cnt+1)] > weight + w:
                        dict1[(neighbor,cnt+1)] = weight + w 
                        heapq.heappush(ans,[dict1[(neighbor,cnt+1)],neighbor,cnt+1])
                else:
                    if dict1[(neighbor,1)] > weight + w:
                        dict1[(neighbor,1)] = weight + w 
                        heapq.heappush(ans,[dict1[(neighbor,1)],neighbor,1])

        min_val = min([dict1[(n-1,j)] for j in range(1,k+1)])

        return min_val if min_val != float("inf") else -1