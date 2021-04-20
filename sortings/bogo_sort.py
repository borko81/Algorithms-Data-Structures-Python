'''
shotgun, or permutation sorting algorithm.
Generate permutation untill find sorting list
'''

# O(!N)
import random


class BogoSort:

    def __init__(self, nums):
        self.nums = nums

    @property
    def len_nums(self):
        return len(self.nums)

    def is_sorted(self):
        for i in range(self.len_nums - 1):
            if self.nums[i] > self.nums[i + 1]:
                return False
        return True

    def shuffle(self):
        random.shuffle(self.nums)

    def sort(self):
        count_of_shuffle = 0
        while not self.is_sorted():
            self.shuffle()
            count_of_shuffle += 1
        return f"List {self.nums} sorted with {count_of_shuffle} tries"


if __name__ == '__main__':
    bogo = BogoSort([1, 3, 2, 4, 0, 10])
    print(bogo.sort())
