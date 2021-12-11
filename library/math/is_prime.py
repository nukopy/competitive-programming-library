def is_prime(num: int) -> bool:
    """入力された整数が「素数であるか」を判定する関数
    時間計算量：O(N)

    Args:
        num (int): 素数判定の対象となる数

    Returns:
        bool: 入力が素数なら True、素数でなければ False
    """

    # 1 以下は素数でない
    if num <= 1:
        return False

    # 2 は素数
    if num == 2:
        return True

    # 2 より大きい偶数は素数でない
    if num % 2 == 0:
        return False

    for j in range(2, num):  # num == 2 のときはループは回らない
        if num % j == 0:  # 1 と自身以外の数で割り切れてしまったら素数でないと判定
            return False

    return True
