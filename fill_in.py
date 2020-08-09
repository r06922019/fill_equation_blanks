import pprint
import random
from functools import reduce
from itertools import permutations
import time

def time_str():
    return time.strftime("%Y-%m-%d %H:%M:%S")

def solve(left_words, signs, right_word):
    chars = list(set("".join(left_words + [right_word])))
    chars.sort()
    assert len(chars) <= 10, "Too many chars: " + str(chars)

    table = { k:11 for k in chars }
    trials = 0
    print(time_str() + " chars: " + str(chars) )
    for digits in permutations(range(10)):
        if trials % 100000 == 0:
            print(time_str() + " trial %8d %s" % (trials, str(digits)))
        trials += 1

        for i, k in enumerate(chars):
            table[k] = digits[i]

        # check if
        if check_ans(left_words, signs, right_word, table):
            print(time_str() + " %8d " % (trials)+ pprint.pformat(table))


def check_ans(left_words, signs, right_word, table):
    left_ans = 0

    for i, word in enumerate(left_words):
        left = word_to_num(word, table)
        if len(left) != len(word):
            return False
        left_ans += signs[i] * int(left)

    right_ans = word_to_num(right_word, table)
    if len(right_ans) != len(right_word):
        return False

    return int(left_ans) == int(right_ans)


def word_to_num(word, table, verbose=False):
    ans = "".join([ str(table[c]) for c in word ])
    if verbose: print("%s => %s" % (word, ans))
    return ans

solve(["NANGANG", "HUILONG", "HAISHAN"], [1, 1, 1], "ZHISHAN")

# table = {'O':7, 'G':0, 'U':6, 'H':1, 'A':2, 'I':4, 'L':9, 'Z':8, 'N':5, 'S':3}
# print(check_ans(["NANGANG", "HUILONG", "HAISHAN"], [1, 1, 1], "ZHISHAN", table))




