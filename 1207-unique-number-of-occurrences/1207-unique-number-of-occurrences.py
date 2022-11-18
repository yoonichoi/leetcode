class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen = set()
        for cnt in collections.Counter(arr).values():
            if cnt in seen: return False
            else:
                seen.add(cnt)
        return True