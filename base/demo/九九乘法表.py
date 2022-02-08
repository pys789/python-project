for i in range(1, 10):
    for j in range(1, 10):
        if i >= j:
            print('{0:1d}*{1:1d}={2:<2d}'.format(j, i, i * j), end="  ")
    print()
