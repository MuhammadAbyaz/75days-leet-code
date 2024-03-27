def mergeAlternately(word1: str, word2: str) -> str:
    n1 = len(word1)
    n2 = len(word2)
    max_arr = word1 if n1 > n2 else word2
    result = ""
    for i in range(max(n1, n2)):
        if i < min(n1, n2):
            result += f"{word1[i]}{word2[i]}"
        else:
            result += f"{max_arr[i]}"
    return result
