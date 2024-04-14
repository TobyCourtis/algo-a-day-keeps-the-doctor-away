# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, S, T):
    # Implement your solution here

    ships_split = S.split(",")
    ships = []
    for ship in ships_split:
        ship_coord = []
        for coord in ship.split(" "):
            ship_coord.append(coordinate_to_index(coord))
        ships.append(ship_coord) # did not have time to make this a grid of all coords

    hits = set([coordinate_to_index(coord) for coord in T.split(" ")])

    hit_count = 0
    sunk_count = 0

    for ship in ships:
        length = len(ship)
        cur_hits = 0
        for coord in ship:
            if coord in hits:
                cur_hits += 1
        if cur_hits == length:
            sunk_count += 1
        elif cur_hits > 0:
            hit_count += 1

    return f"{sunk_count},{hit_count}"


def coordinate_to_index(co_ord):
    return (int(co_ord[0:-1]) - 1,
            ord(co_ord[-1]) - ord("A"))


print(solution(4,
               "1B 2C,2D 4D",
               "2B 2D 3D 4D 4A"))
