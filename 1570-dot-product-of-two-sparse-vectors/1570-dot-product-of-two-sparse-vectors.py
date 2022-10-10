class SparseVector:
    def __init__(self, nums: List[int]):
        self.seen = {}
        for idx,v in enumerate(nums):
            if v != 0:
                self.seen[idx] = v

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        summ = 0
        for idx, v in vec.seen.items():
            if idx in self.seen:
                summ += v * self.seen[idx]
        return summ
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)