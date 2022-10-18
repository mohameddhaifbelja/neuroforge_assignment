"""
This solution uses dynamic programming for  to produce an algorithm with:
a linear time complexity: o(n)
and a constant space complexity: o(1)
"""


def solution(start, nbr_hops):
    # test validity of parameters
    if nbr_hops < 0 or start not in range(0, 10):
        print("verify that nbr of hops is positive and start position is between 0 and 9")
        return 0
    # map each possible move for all starting points
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
    # base case for 0 hops
    prev = [1] * 10
    current = [0] * 10

    for i in range(nbr_hops):
        current = [0] * 10

        for position in range(0, 10):
            for neighbor in neighbors[position]:
                current[position] += prev[neighbor]

        # Update for next hop
        prev = current

    return current[start]
