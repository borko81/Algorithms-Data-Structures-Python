# O(N2)
from typing import List, Union


class BubbleSort:

    def __init__(self, nums: List[Union[int, float]]):
        self.nums = nums

    @property
    def nums_lenght(self) -> int:
        return len(self.nums)

    def __acd_sort(self, j):
        return self.nums[j] > self.nums[j + 1]

    def __des_sort(self, j):
        return self.nums[j] < self.nums[j + 1]

    def __swap(self, i: int, j: int):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

    def __check(self, key):
        if key == 0:
            return lambda x: self.__acd_sort(x)
        if key == 1:
            return lambda x: self.__des_sort(x)

    def sort(self, key=0):
        """
        :param key: if key == 0 use asc sort, elif key == 1 use desc sort
        :return: sorted nums
        """
        temp = self.__check(key)
        for i in range(self.nums_lenght - 1):
            for j in range(self.nums_lenght - i - 1):
                if temp(j):
                    self.__swap(j, j + 1)
        return self.nums


if __name__ == '__main__':
    bubble = BubbleSort([-2, 10, 3, 2, 9])
    print(bubble.sort())
