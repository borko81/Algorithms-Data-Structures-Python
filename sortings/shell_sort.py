def shell_sort(nums):

    gap = len(nums) // 2

    while gap > 0:

        for i in range(gap, len(nums)):
            j = i

            while j >= gap and nums[j - gap] > nums[j]:
                nums[j], nums[j - gap] = nums[j - gap], nums[j]
                j -= gap

        gap = gap // 2


if __name__ == '__main__':
    arr = [-2, 10, 3, 2, 9]
    shell_sort(arr)
    print(arr)