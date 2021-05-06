import multiprocessing as mp
import string
import random

output = mp.Queue()


def rand_string(length, output):
    rand_str = ''.join(random.choice(
        string.ascii_lowercase
        + string.ascii_uppercase
        + string.digits)
                       for _ in range(length))
    output.put(rand_str)


process = [mp.Process(target=rand_string, args=(5, output)) for i in range(4)]

if __name__ == '__main__':
    for p in process:
        p.start()

    # for p in process:
    #     p.join()

    [print(output.get()) for _ in process]