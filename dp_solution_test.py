import random
import unittest
from dp_solution import solution


class DpSolutionTestCase(unittest.TestCase):

    def setUp(self):
        self.neighbors = {
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

    def test_invalid_entries(self):
        possible_numbers = solution(1, -10)
        self.assertEqual(possible_numbers, -1)
        possible_numbers = solution(10, 1)
        self.assertEqual(possible_numbers, -1)
        possible_numbers = solution(-1, -1)
        self.assertEqual(possible_numbers, -1)

    def test_zero_hop(self):
        start = random.randint(0, 9)
        possible_numbers = solution(start, 0)
        self.assertEqual(possible_numbers, 1)

    def test_start_at_five(self):
        nbr_hops = random.randint(0, 100)
        possible_numbers = solution(5, nbr_hops)
        self.assertEqual(possible_numbers, 1)

    def test_single_hop(self):
        start = random.randint(0, 9)
        possible_numbers = solution(start, 1)
        self.assertEqual(possible_numbers, len(self.neighbors[start]))

    def test_more_than_one_hop(self):
        start = random.randint(0, 9)
        nbr_hops = random.randint(2, 100)
        previous = 0

        for neighbor in self.neighbors[start]:
            previous += solution(neighbor, nbr_hops-1)

        self.assertEqual(previous, solution(start, nbr_hops))


if __name__ == '__main__':
    unittest.main()
