def countBetween(arr, low, high):
    arr.sort()
    out = []
    for i in range(len(low)):
        low_index = None
        high_index = None
        for j in range(len(arr)):
            if arr[j] >= low[i] and low_index is None:
                low_index = j
            if arr[- (j + 1)] <= high[i] and high_index is None:
                high_index = - (j + 1)
            if high_index is not None and low_index is not None:
                break

        out.append(len(arr[low_index:len(arr) + high_index + 1]))

    return out


# print(countBetween([1, 3, 5, 6, 8], [2], [6]))
print(countBetween([4, 8, 7], [2, 4], [8, 4]))

print([1, 2, 3, 4][0:len([1, 2, 3, 4]) - 1 + 1])
