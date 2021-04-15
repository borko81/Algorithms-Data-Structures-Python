def check_is_anagram_or_not(str1, str2):
    len_one = len(str1)
    len_two = len(str2)

    if not len_one == len_two:
        return False

    str1, str2 = sorted(str1), sorted(str2)
    for i in range(len_one):
        if not str1[i] == str2[i]:
            return False

    return True


if __name__ == '__main__':
    print(check_is_anagram_or_not('car', 'rac'))
