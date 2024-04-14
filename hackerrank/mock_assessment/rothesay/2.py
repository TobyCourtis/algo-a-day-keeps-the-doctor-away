# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    a_sum = sum(A)
    b_sum = sum(B)

    if a_sum > b_sum:
        largest = sorted(A, reverse=True)
        smallest = sorted(B)
    else:
        largest = sorted(B, reverse=True)
        smallest = sorted(A)

    diff = abs(a_sum - b_sum)

    changes = 0
    large_index = 0
    small_index = 0
    while diff > 0 and small_index < len(smallest) and large_index < len(largest):
        if (largest[large_index] - 1) > (6 - smallest[small_index]):
            # making cur value in larger list equal to 1
            diff -= (largest[large_index] - 1)
            large_index += 1
        else:
            diff -= (6 - smallest[small_index])
            small_index += 1
        changes += 1

    if diff < 0:
        return changes

    while diff > 0 and large_index < len(largest):
        diff -= (largest[large_index] - 1)
        large_index += 1
        changes += 1

    while diff > 0 and small_index < len(smallest):
        diff -= (6 - smallest[small_index])
        small_index += 1
        changes += 1

    return -1 if diff > 0 else changes


def solution1(A, B):
    n = len(A)  # 5
    m = len(B)  # 3

    if m < n:  # n greater
        min_n = n
        max_m = m * 6
        if min_n > max_m:
            return - 1  # not possible

        n_sum = sum(A)
        m_sum = sum(B)
        diff = abs(n_sum - m_sum)

    pass


solution([2, 3, 1, 1, 2],
         [5, 4, 6])
