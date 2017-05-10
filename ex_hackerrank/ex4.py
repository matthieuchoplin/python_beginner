size = 17
a="""--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------"""

from string import ascii_lowercase

def print_rangoli(size):
    l_letters = ascii_lowercase[:size]
    L = []
    for i, j in enumerate(ascii_lowercase[:size]):
        L.append(''.join(reversed(list(l_letters[i:size])))+l_letters[i+1:size])
    for l in list(reversed(L))+L[1:]:
        print('-'.join(list(l)).center(4*size-3, '-'))

print_rangoli(size)