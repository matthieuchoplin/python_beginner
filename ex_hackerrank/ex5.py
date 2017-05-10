from string import ascii_uppercase
vowels = 'AEIOU'
CONSONANTS = ''.join([l for l in ascii_uppercase if l not in vowels])

def minion_game(string):
    # stuart starts with consonants
    for i, l in enumerate(string):
        if l in CONSONANTS:
            w = string[i:]
    # kevin starts with vowels

minion_game('BANANA')