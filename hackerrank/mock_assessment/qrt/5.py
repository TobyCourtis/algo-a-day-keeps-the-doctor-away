num = 2  # Example integer
binary_representation = bin(num)
print(binary_representation)

num = 6  # Example integer
binary_representation = bin(num)[2:]
print(binary_representation)


def generate_combinations(string, combinations, current='', index=0):
    if index == len(string):
        combinations.append(current)
        return

    if string[index] == '1':
        generate_combinations(string, combinations, current + string[index], index + 1)
    else:
        generate_combinations(string, combinations, current + '0', index + 1)
        generate_combinations(string, combinations, current + '1', index + 1)


# combinations = []
# generate_combinations("001", combinations)
# print(combinations)


def superBitstrings(n, bitStrings):
    # Write your code here
    print(n)
    print(bitStrings)

    combinations_set = set()
    for bitString in bitStrings:
        # 1. find binary representation "binary" of bitString length n e.g "10"
        # 2. gen all combinations

        binary = bin(bitString)[2:]
        for i in range(n - len(binary)):
            binary = "0" + binary

        if binary in combinations_set:
            continue

        # generate combinations
        combinations = []
        generate_combinations(binary, combinations)
        combinations_set.update(combinations)

    return combinations_set


print(superBitstrings(2, [1]))
