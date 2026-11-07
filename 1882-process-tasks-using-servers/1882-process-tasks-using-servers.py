class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        n,m=len(servers),len(tasks)
        ans=[]
        hsmall=[]
        hlarge=[]
        for idx, weight in enumerate(servers):
            heappush(hsmall, (weight, idx, 0)) 

        for i, task in enumerate(tasks):
            while hlarge and hlarge[0][0]<=i:
                time,weight,index=heappop(hlarge) 
                heappush(hsmall,(weight,index,time))
            
            if hsmall:
                weight,index,time=heappop(hsmall)
                ans.append(index)
                heappush(hlarge,(i+task,weight,index))
            else:
                time, weight, index = heappop(hlarge)
                ans.append(index)
                heappush(hlarge, (time + task, weight, index))
        
        return ans