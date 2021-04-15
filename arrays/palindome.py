from arrays.reverse_array_in_list import reversed_array


def check_is_palindrome(word):
    return word == word[::-1]


def check_palidnome2(word):
    original = word
    rev_word = reversed_array(list(word))
    return original == "".join(rev_word)

print('madam is palidnrome', check_is_palindrome('madam'))
print('car is palidnrome', check_is_palindrome('car'))

print('madam is palidnrome', check_palidnome2('madam'))
print('car is palidnrome', check_palidnome2('car'))