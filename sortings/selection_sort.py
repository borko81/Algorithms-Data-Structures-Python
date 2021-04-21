# O(N2)
# Slow, but it fast on small array 5 to 10

def selection_sort(nums):
    # N - 1 search
    # N - 1 x O(N) = O(NxN)
    for i in range(len(nums) - 1):
        index = i

        # Linear search O(N)
        for j in range(i, len(nums)):
            if nums[j] < nums[index]:
                index = j

        if index != i:
            nums[index], nums[i] = nums[i], nums[index]


if __name__ == '__main__':
    arr = [-4, 2, 10, 9, 1, 5]
    test = selection_sort(arr)
    print(arr)
