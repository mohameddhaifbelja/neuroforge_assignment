"""
This solution utilizes numpy optimized matrix multiplication to
solve this problem

"""
import numpy as np


def solution(start, nbr_hops):
    if nbr_hops < 0 or start not in range(0, 10):
        print("verify that nbr of hops is positive and start position is between 0 and 9")
        return 0

    if nbr_hops == 0:
        return 0

    # Generate matrix containing all the possible moves with 1 hop
    moves = np.zeros((10, 10))
    neighbors = {
        0: (4, 6),
        1: (6, 8),
        2: (7, 9),
        3: (4, 8),
        5: (),  # impossible to move to any other number
        4: (3, 9, 0),
        6: (1, 7, 0),
        7: (2, 6),
        8: (1, 3),
        9: (2, 4)
    }
    for neighbor in neighbors:
        moves[neighbor, neighbors[neighbor]] = 1
    result = moves

    for i in range(nbr_hops - 1):
        result = np.matmul(result, moves)

    return int(np.sum(result[start]))

