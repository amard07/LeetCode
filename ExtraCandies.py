class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy_amount = max(candies)
        for index in range(len(candies)):
            if candies[index] + extraCandies >= max_candy_amount:
                yield True
            else:
                yield False
