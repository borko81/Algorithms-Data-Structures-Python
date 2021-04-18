import threading
import os
from abc import abstractmethod

from sqlalchemy.testing.plugin.plugin_base import ABC


class Shape(ABC):

    @abstractmethod
    def __init__(self, *args):
        self.num = args[0]

    @property
    @abstractmethod
    def print_shape(self):
        return f"[{threading.current_thread().name} with pid {os.getpid()}] "


class Cube(Shape):

    def __init__(self, num):
        super().__init__(num)
        self.num = num

    @property
    def print_shape(self):
        return super().print_shape + "Cube format is : %d" % (self.num * self.num * self.num)


class Square(Shape):
    def __init__(self, num):
        super().__init__(num)
        self.num = num

    @property
    def print_shape(self):
        return super().print_shape + "Square format is : %d" % (self.num * self.num)


def main(shape, n):
    print(shape(n).print_shape)


if __name__ == '__main__':
    t1 = threading.Thread(target=main, args=(Cube, 10, ))
    t2 = threading.Thread(target=main, args=(Square, 10))
    t1.start()
    t2.start()
    t1.join()
    t2.join()