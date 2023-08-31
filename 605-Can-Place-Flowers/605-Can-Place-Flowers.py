class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                # 첫번째거나
                if i == 0 and len(flowerbed) > 1 and flowerbed[i+1] == 0:
                    n -= 1
                    flowerbed[i] = 1
                    if n == 0:
                        return True
                # 제일 마지막이거나
                elif i == len(flowerbed) - 1 and flowerbed[i-1] == 0:
                    n -= 1
                    flowerbed[i] = 1
                    if n == 0:
                        return True
                # 그 외
                elif flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    n -= 1
                    flowerbed[i] = 1
                    if n == 0:
                        return True
            
        return False
