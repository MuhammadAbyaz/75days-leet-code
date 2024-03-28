def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    kids_with_max_candies: list[bool] = []
    for i in range(len(candies)):
        if candies[i] + extraCandies >= max(candies):
            kids_with_max_candies.append(True)
        else:
            kids_with_max_candies.append(False)
    return kids_with_max_candies


print(kidsWithCandies([2, 3, 5, 1, 3], 3))
