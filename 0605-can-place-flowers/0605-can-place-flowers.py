class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0: return True
        cnt = 0
        flowerbed = [0] + flowerbed + [0]
        for f in flowerbed:
            if f == 0:
                cnt += 1
            else:
                cnt = 0
            if cnt == 3:
                n -= 1
                cnt = 1
            if n == 0 : return True
        return False