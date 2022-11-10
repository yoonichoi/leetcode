class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def onechange(a,b):
            return sum([1 for i in range(len(a)) if a[i]!=b[i]])==1
        q = collections.deque([(start, 0)])
        seen = {start}
        while q:
            gene, cnt = q.popleft()
            if gene == end:
                return cnt
            for g in bank:
                if onechange(g, gene) and g not in seen:
                    q.append((g, cnt+1))
                    seen.add(g)
        return -1
        