def canPlaceFlowers(flowersbed: list[int], n: int) -> bool:
    for i in range(len(flowersbed)):
        if (
            flowersbed[i] == 0
            and (i == 0 or flowersbed[i - 1] == 0)
            and (i == len(flowersbed) - 1 or flowersbed[i + 1] == 0)
        ):
            n -= 1
            flowersbed[i] = 1

    return True if n <= 0 else False
