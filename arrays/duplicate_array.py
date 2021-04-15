def find_duplicated_in_array(array):
    """
    Work onli with array with poitive indexes and max(element) == len of array!!!
    :param array:
    :return:
    """
    for n in array:
        if array[abs(n)] >= 0:
            array[abs(n)] = -array[abs(n)]
        else:
            return "Found duplicated %s" % abs(n)


print(find_duplicated_in_array([2, 1, 4, 5, 2, 3]))