# O(N2)
# Slow, but it fast on small array 10 to 20

def insertion_sort(nums):
    for i in range(len(nums)):
        temp = i
        while temp > 0 and nums[temp - 1] > nums[temp]:
            nums[temp - 1], nums[temp] = nums[temp], nums[temp - 1]
            temp -= 1


if __name__ == '__main__':
    arr = [-4, 2, 10, 9, 1, 5]
    test = insertion_sort(arr)
    print(arr)
