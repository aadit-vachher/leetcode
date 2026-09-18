from collections import defaultdict
from typing import List

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        posLocation = defaultdict(list)
        
        # Step 1: record first and last occurrence
        for i, ch in enumerate(s):
            if len(posLocation[ch]) >= 2:
                posLocation[ch].pop()
            if not posLocation[ch]:
                posLocation[ch].append(i)
            posLocation[ch].append(i)
        
        setResult = set()
        
        # Step 2: build candidate intervals
        for key, val in posLocation.items():
            st, ed = val[0], val[1]
            beg = st
            isValid = True
            while beg <= ed:
                if posLocation[s[beg]][0] < st:
                    isValid = False
                    break
                ed = max(posLocation[s[beg]][1], ed)
                beg += 1
            if isValid:
                setResult.add((st, ed))
        
        # Step 3: greedy selection
        setResult = list(setResult)
        setResult.sort(key=lambda x: x[1])
        
        result = []
        prevEnd = -1
        for st, ed in setResult:
            if st > prevEnd:
                result.append(s[st:ed+1])
                prevEnd = ed
        return result