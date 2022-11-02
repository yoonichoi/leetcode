class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def ifonechanged(a,b):
            return sum([1 for i in range(len(a)) if a[i]!=b[i]]) == 1
        q = collections.deque([(start, 0)])
        seen = {start}
        while q:
            gene, cnt = q.popleft()
            if gene == end:
                return cnt
            for g in bank:
                if g not in seen and ifonechanged(gene, g):
                    seen.add(g)
                    q.append((g, cnt + 1))
        return -1
            
        