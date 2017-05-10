vowels = 'AEIOU'
def minion_game(string):
    kevin_s = 0
    stuart_s = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevin_s += len(string)-i
        else:
            stuart_s += len(string)-i

    if kevin_s > stuart_s:
        print("Kevin", kevin_s)
    elif kevin_s < stuart_s:
        print("Stuart", stuart_s)
    else:
        print("Draw")