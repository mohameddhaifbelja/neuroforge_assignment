import dp_solution as dp
import matmul_solution as matmul
import time


def test_performance():
    start = 4
    nbr_hops = 20
    iterations = 100

    start_time = time.time()
    for i in range(iterations):
        dp.solution(start, nbr_hops)

    dp_time = (time.time() - start_time)

    start_time = time.time()

    for i in range(iterations):
        matmul.solution(start, nbr_hops)

    matmul_time = (time.time() - start_time)

    print(f'The dp algorithm generated the solution in {dp_time}s')
    print(f'whereas the matmul based on numpy did it in {matmul_time}s ')

if __name__ == "__main__":

    test_performance()
