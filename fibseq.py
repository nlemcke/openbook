def fibonacci(n):
    """return the nth number in Fibonacci's sequence"""

    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return 'Not Defined'
    else:
        seq = [1, 1]

        for j in range(n - 1):
            seq.append(seq[-1] + seq[-2])

        return seq[-1]
