def is_palindrome(s: str) -> bool:
    len_s = len(s)
    half = len_s // 2  # 回文を調べるには文字列の半分の長さで良い

    for i in range(half):
        if s[i] != s[(len_s - 1) - i]:
            return False

    return True
