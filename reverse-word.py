def reverseWords(s: str) -> str:
    str_list: list[str] = s.strip().split(" ")
    return " ".join([val for val in str_list if val != ""][::-1])


print(reverseWords("a good   example"))
