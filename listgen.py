#!/usr/bin/env python3
from itertools import combinations, permutations

words = []
passwords = []
CHANGE_CASE = True
L337 = True
COMBINATIONS = 3


def l337(s: str):
    dic = {'a': '4', 'e': '3', 'g': '6', 'o': '0', 's': '5', 't': '7'}
    for leet in dic:
        s = s.replace(leet, dic[leet])
    return s


def generate(ar, c):
    combi = []
    for x in range(1, c + 1):
        combi += combinations(ar, x)
    passes = []
    for x in combi:
        passes += [''.join(p) for p in permutations(x)]
    return passes


def ask(s):
    inp = input(s)
    if inp.lower().startswith('n'):
        return False
    return True


def get_input():
    global words, L337, CHANGE_CASE
    L337 = ask("Use l337? (y/n): ")
    CHANGE_CASE = ask("Change first letter case? (y/n): ")
    while True:
        inp = input("Enter words to use (press enter to finish): ")
        if not inp:
            break
        new_words = [x.lower() for x in inp.split(' ')]
        words += new_words
        if L337:
            words += [l337(s) for s in new_words]
        if CHANGE_CASE:
            words += [s.capitalize() for s in new_words]
        print("Added %s word(s)." % len(new_words))


def finish():
    global COMBINATIONS, passwords
    inp = input("\nMaximum no. of words to combine (default 3): ")
    if isinstance(inp, int):
        COMBINATIONS = inp
    print("Using max %s word combinations.\n" % COMBINATIONS)
    passwords = generate(words, COMBINATIONS)
    f = input("\nEnter file name to save wordlist to (enter to not save): ")
    if f:
        file = open(f, "w+")
        for password in passwords:
            file.write(password + '\n')
        file.close()
    p = ask("\nPrint generated passwords? (y/n): ")
    if p:
        for password in passwords:
            print(password)


if __name__ == '__main__':
    get_input()
    finish()
