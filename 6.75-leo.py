import cupy as np
import time

nums = [int(x) for x in open(r"6.txt", "r").read().strip().split(",")]


def day6(data: list, days: int) -> int:
    start = time.time()
    mat = np.array(
        [
            [0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
    )
    veigen = np.linalg.matrix_power(mat.astype(np.uint64),days).sum(axis=0)
    o = sum(veigen[el] for el in data)
    t = time.time() - start
    return "\niter: " + str(days) + "\ntime: " + str(t) + "\n"


if __name__ == "__main__":
    print(day6(nums, 80))
    print(day6(nums, 256))
    print(day6(nums, 100000))
    print(day6(nums, 3650000))
