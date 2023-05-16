def migratoryBirds(arr):
    # Write your code here
    birdCounts = {}
    for i in arr:
        if i not in birdCounts.keys():
            birdCounts[i] = 1
        else:
            birdCounts[i] += 1

    birdKey = None
    maxCount = 0
    for k, v in birdCounts.items():
        if v > maxCount:
            birdKey = k
            maxCount = v
        elif v == maxCount:
            if birdKey > k:
                birdKey = k
    return birdKey


print(migratoryBirds([1, 1, 2, 2, 3]))
