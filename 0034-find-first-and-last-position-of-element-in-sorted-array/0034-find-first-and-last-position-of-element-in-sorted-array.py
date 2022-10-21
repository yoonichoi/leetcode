class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binsearch(nums, target, find_start=True):
            l, r, res = 0, len(nums)-1, -1
            while l <= r:
                mid = l + (r-l) // 2
                if nums[mid] == target:
                    res = mid
                    if find_start:
                        r = mid - 1
                    else:
                        l = mid + 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return res
        return [binsearch(nums, target), binsearch(nums, target, False)]