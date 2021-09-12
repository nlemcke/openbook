def fibonacci(n):
    seq = [1, 1]

    for j in range(n - 1):
        seq.append(seq[-1] + seq[-2])

    return seq[-1]

print(fibonacci(4))
