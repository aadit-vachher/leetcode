
import numpy as np

#numAccm = [0]

class RObj:
    def __init__(self, k, bucketBegin, bucketEnd):
        self.k = k
        self.bucketBegin = bucketBegin
        self.bucketEnd = bucketEnd
        self.mapMatrix = None
        self.localFreq = None
    
    def makeCopy(self):
        ret = RObj(self.k, self.bucketBegin, self.bucketEnd)

        ret.mapMatrix = [self.mapMatrix[r][:] for r in range(self.k)]
        ret.localFreq = self.localFreq[:]
        return ret

    def reCalculateDependentKernel(self, nums, start = -1):
        bStart = self.bucketBegin
        bEnd = self.bucketEnd
        if -1 != start:
            bStart = start

        mapMatrix = [[0]*self.k for _ in range(self.k)]
        for i in range(self.k):
            mapMatrix[i][i] = 1
        
        assert(bEnd >= bStart)

        for i in range(bEnd-1, bStart-1,-1):
            mapMatrix2 = [[0]*self.k for r in range(self.k)]
            for r in range(self.k):
                rrLeft = (r*nums[i])%self.k
                for c in range(self.k):
                    mapMatrix2[rrLeft][c] += mapMatrix[r][c]
            mapMatrix = mapMatrix2
            #print(i, nums[i], mapMatrix)

        return mapMatrix

    def reCalculateLocalKernel(self, nums, start = -1):
        bStart = self.bucketBegin
        bEnd = self.bucketEnd
        if -1 != start:
            bStart = start

 
        #memo = []
        localFreq = [0]*self.k
        for i in range(bEnd-1, bStart-1,-1):
            localFreq2 = [0]*self.k
            for r in range(self.k):
                rrLeft = (r*nums[i])%self.k
                localFreq2[rrLeft] += localFreq[r]
            localFreq = localFreq2
            localFreq[nums[i]%self.k] += 1
        return localFreq
    
    def reCalcFullKernel2(self, val):
        mapMatrix = [[0]*self.k for _ in range(self.k)]
        for r in range(self.k):
            rrLeft = (r*val)%self.k
            mapMatrix[rrLeft][r] += 1
        self.mapMatrix = mapMatrix

        localFreq = [0]*self.k
        localFreq[val%self.k] = 1
        self.localFreq = localFreq

    def reCalcFullKernel(self, nums):

        self.mapMatrix = self.reCalculateDependentKernel(nums)
        self.localFreq = self.reCalculateLocalKernel(nums)

    def accumulateKernel(self, other):
        output = [0]*self.k
        for r in range(self.k):
            for c in range(self.k):
                output[r] += self.mapMatrix[r][c]*other[c]
            output[r] += self.localFreq[r]
        
        return output
    
    def accumulateUpto(self, nums, other, startPos):


        mapMatrix = self.reCalculateDependentKernel(nums, startPos)
        localFreq = self.reCalculateLocalKernel(nums, startPos)
        output = [0]*self.k
        for r in range(self.k):
            for c in range(self.k):
                output[r] += mapMatrix[r][c]*other[c]
            output[r] += localFreq[r]
        
        #print(self, 'AccumulteUpto',startPos, other, output)
        return output
    
    def __repr__(self):

        return str((self.bucketBegin,self.bucketEnd,self.localFreq))
    
    @staticmethod
    def merge(a, b):

        if b is None:
            if a is None:
                return None
            #ret = a.makeCopy()
            ret = copy.deepcopy(a)
            return ret
        

        ret = RObj(a.k, a.bucketBegin, b.bucketEnd)

        mapMatrix = [[0]*ret.k for _ in range(ret.k)]
        for r in range(ret.k):
            for c in range(ret.k):
                for cb in range(ret.k):
                    mapMatrix[r][c] += a.mapMatrix[r][cb]*b.mapMatrix[cb][c]
        ret.mapMatrix = mapMatrix

        localFreq = [0]*ret.k
        for r in range(ret.k):
            for c in range(ret.k):
                localFreq[r] += a.mapMatrix[r][c]*b.localFreq[c]
            localFreq[r] += a.localFreq[r]
 
        ret.localFreq = localFreq
 
        return ret
 

class RObjNP:
    def __init__(self, k ):
        self.k = k
        self.mapMatrix = None
        self.localFreq = None
    
    def reCalcFullKernelNP(self, val):
        mapMatrix = np.zeros((self.k, self.k), dtype=np.uint32)
        for r in range(self.k):
            rrLeft = (r*val)%self.k
            mapMatrix[rrLeft][r] += 1
        self.mapMatrix = mapMatrix
        localFreq = np.zeros(self.k, dtype=np.uint32)
        localFreq[val] = 1
        self.localFreq = localFreq
   
    def accumulateKernelNP(self, other):
        output = np.dot(self.mapMatrix, other)
        output = np.add(output,self.localFreq)
        return output

    @staticmethod
    def mergeNP(a, b):

        if b is None:
            if a is None:
                return None
            ret = a
            return ret
        
        ret = RObjNP(a.k)

        ret.mapMatrix = np.matmul(a.mapMatrix,b.mapMatrix)

        ret.localFreq = a.accumulateKernelNP(b.localFreq)
 
        #ret.calcHashCode()
 
        return ret

class RObjNPVector:
    def __init__(self, k ):
        self.k = k
        self.localFreq = None
    
    def reCalcFullKernelNP(self, val):
        self.val = val
        localFreq = np.zeros(self.k, dtype=np.uint32)
        localFreq[val] = 1
        self.localFreq = localFreq
    
    def accumulateKernelNP(self, other):
        output = self.localFreq.copy()
        for r in range(self.k):
            rrLeft = (r*self.val)%self.k
            output[rrLeft] += other[r]
        return output
     
    @staticmethod
    def mergeNP(a, b):

        if b is None:
            if a is None:
                return None
            ret = a
            return ret
        
        ret = RObjNPVector(a.k)
        ret.localFreq = a.accumulateKernelNP(b.localFreq)
        ret.val = (a.val*b.val)%ret.k
 
        return ret
 
MEMOT = RObj
MEMOT = RObjNP
MEMOT = RObjNPVector
class SegmentTreeMtrx:
    def __init__(self, N, k):

        depth = 1
        while (1<<depth) < N:
            depth+=1

        self.leafBegin = 1<<depth 
        self.leafEnd = self.leafBegin+N
        NN = self.leafBegin+N
        self.nodes = [None]*NN
        self.N = N
        self.k = k
        self.leftMost = [None]*NN
        self.rightMost = [None]*NN
        #print(self.N, NN)

    def fill(self, nums, factory):

        for i in range(self.N):
            self.nodes[self.leafBegin+i] = factory[nums[i]]
            self.leftMost[self.leafBegin+i] = self.leafBegin+i
            self.rightMost[self.leafBegin+i] = self.leafBegin+i
        
        for i in range(self.leafBegin-1,0,-1):
            left = i<<1
            right = left+1
            if right < self.leafEnd:
                self.nodes[i] = MEMOT.mergeNP(self.nodes[left], self.nodes[right])
                self.leftMost[i] = self.leftMost[left]
                self.rightMost[i] = self.rightMost[right]
            elif left < self.leafEnd:
                self.nodes[i] = self.nodes[left]
                self.leftMost[i] = self.leftMost[left]
                self.rightMost[i] = self.leafEnd
            else:
                self.nodes[i] = None
                self.leftMost[i] = self.leafEnd
                self.rightMost[i] = self.leafEnd

        
        self.nums = nums
        self.factory = factory

    def __setitem__(self, ii, val):

        k = self.nodes[self.leafBegin].k
        if self.nums[ii] == val:
            return

        self.nums[ii] = val

        cur = self.leafBegin+ii
        self.nodes[cur] = self.factory[val]

        cur = cur>>1
        while cur > 0:
            left = cur<<1
            right = left+1
            if right < self.leafEnd:
                self.nodes[cur] = MEMOT.mergeNP(self.nodes[left], self.nodes[right])
            else:
                self.nodes[cur] = self.nodes[left]
            cur = cur>>1

    def query(self, startPos):

        memo = []
        stack = [1]
        leftPos = self.leafBegin+startPos
        while stack:
            cur = stack.pop()
            if self.nodes[cur] is None:
                continue
            if self.leftMost[cur] >= leftPos:
                if self.nodes[cur] is not None:
                    memo.append(  (self.leftMost[cur],cur ) ) 
            elif self.rightMost[cur] < leftPos:
                continue
            else: 
                left = cur<<1
                right = left+1
                if right < (self.leafEnd):
                    stack.append(right)
                if left < (self.leafEnd):
                    stack.append(left)

        #memo.sort()
        kern = [0]*self.nodes[self.leafBegin].k
        for unused,idx in reversed(memo):
            kern = self.nodes[idx].accumulateKernelNP(kern)
            #numAccm[0] += 1

        return kern

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:

        N = len(nums)

        nums = [(x%k) for x in nums]
        factory = [None]*k
        for i in range(k):
            factory[i] = MEMOT(k)
            factory[i].reCalcFullKernelNP(i)

        tree = SegmentTreeMtrx(N, k)
        tree.fill(nums, factory)
        
        result = np.zeros(len(queries), dtype=np.uint32)
        for qidx,(ci,v,prestart,qx) in enumerate(queries):

            tree[ci] = v%k

            kern = tree.query(prestart)
            result[qidx] = kern[qx]

        return result.astype(int).tolist()
