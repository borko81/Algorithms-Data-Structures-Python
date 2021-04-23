file = '1^doc_line^^01/09/2019^2000^^^1000040237^^^^^^1^ФАКТУРА^^^^ANDREY  PETRUNIN^999999999999999^999999999999999^^^^^RU^^^^^^^^^АВАНС 9%^АВАНС 9%^1.00^-1213.76^-1213.7600^^-109.240000^9.0000^^PERSON: ANDREY  PETRUNIN / res. HD.3180^ANDREY  PETRUNIN-412^412^6478^1000040190'

for enum, word in enumerate(file.split('^'), start=1):
    print(enum, word)