import multiprocessing as mp


def cube(x):
    return x ** 3


if __name__ == "__main__":

    n_processes = 3

    pool = mp.Pool(processes=n_processes)
    results = pool.map(cube, range(1, 10000))

    print(results)
