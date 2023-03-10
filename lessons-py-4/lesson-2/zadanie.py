def sum(a, b):
    if a < 0 or b < 0:
        raise ValueError("Функция работает только с неотрицательными числами.")
    if b == 0:
        return a
    else:
        return sum(a+1, b-1)