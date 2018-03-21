import multiprocessing as mp


def cube(x):
    return x ** 3


if __name__ == "__main__":

    n_processes = 2

    pool = mp.Pool(processes=n_processes)
    results = [pool.apply(cube, args=(x,)) for x in range(1, 10000)]

    print(results)
