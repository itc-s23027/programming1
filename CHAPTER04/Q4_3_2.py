def func_square(*args):
    result = []
    for n in args:
        results.append(n * n)
    return result


numbers = [1, 2, 3, 4]
func_square(*numbers)
