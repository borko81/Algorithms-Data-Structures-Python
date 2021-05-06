import multiprocessing as mp


def cube(x):
    return x ** 3


if __name__ == '__main__':
    pool = mp.Pool(processes=4)
    result = [pool.apply(cube, args=(10,))]
    result2 = pool.map(cube, range(1, 7))
    print(result)
    print(result2)


