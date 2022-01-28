def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) == 0 or abs(state[i] - nextX) == nextY - i:
            return True
    return False


def queens(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            # 最后一个皇后位置摆放
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result


print(list(queens(8)))
