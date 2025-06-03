INCORRECT_LETTERS = ""
CORRECT_LETTERS = ""
CORRECT_PLACEMENT = ['','','','','']
INCORRECT_PLACEMENT = [[],[],[],[],[]]

############################################################


import itertools
import json
import os
import csv
os.chdir(os.path.dirname(os.path.abspath(__file__)))

freq = {}
with open('unigrams_freq_5let.csv') as f:
    r = csv.reader(f)
    for row in r:
        freq[row[0]] = int(row[1])

with open('dictionary_5let.json', 'r') as f:
    dictionary = json.load(f)

def generate_permutations(iterable):
  p = list(itertools.permutations(iterable, 5))
  joined = set()
  for pe in p:
    joined.add(''.join(pe))
  return joined

letter_freq = {
"e":127,
"t":91,
"a":82,
"o":75,
"i":70,
"n":67,
"s":63,
"h":61,
"r":60,
"d":43,
"l":40,
"c":28,
"u":28,
"m":24,
"w":24,
"f":22,
"g":20,
"y":20,
"p":19,
"b":15,
"v":9.8,
"k":7.7,
"j":1.5,
"x":1.5,
"q":0.95,
"z":0.74
}

solutions=[]
for p in dictionary.keys():
    match = True
    for cl in INCORRECT_LETTERS:
        if cl in p:
            match = False
            break
    for cl in CORRECT_LETTERS:
        if cl not in p:
            match = False
            break
    if match:
        for i, cp in enumerate(CORRECT_PLACEMENT):
            if cp == '':
                continue
            if p[i] != cp:
                match = False
                break
        if match:
            for i, icp in enumerate(INCORRECT_PLACEMENT):
                if not match:
                    break
                for l in icp:
                    if p[i] == l:
                        match = False
                        break
            if match:    
                solutions.append(p)
print()

print("\rpossible solutions:                                      ")
list.sort(solutions, key=lambda w: freq.get(w, -100000000), reverse=True)
print(solutions)

if (len(solutions)>1):
    unknown_letters = list(dict.fromkeys(''.join(solutions)))
    unknown_letters = [s for s in unknown_letters if s not in CORRECT_LETTERS]
    # unknown_letters = list(unknown_letters)
    # list.sort(unknown_letters, key=lambda l: letter_freq[l], reverse=True)
    print(f"\nunknown letters: %s"%unknown_letters)
    # unknown_letters = unknown_letters[:5]
    # print(f"\n5 most common unknown letters: %s"%unknown_letters)
    def generate_guesses(words = solutions):
        guess_set = set()
        best_guesses = []
        for w in words:
            count = 0
            weight = 0
            for c in INCORRECT_LETTERS:
                if c in w:
                    count=-100
            if words != solutions:
                for c in CORRECT_LETTERS:
                    if c in w:
                        count=-100
            for i, c in enumerate(unknown_letters):
                if c in w:
                    count += 1
                    weight += len(unknown_letters)-i
            if count > 1:
                letter_comb_l=list(w)
                letter_comb_l.sort()
                letter_comb = ''.join(letter_comb_l)
                if (letter_comb not in guess_set):
                    guess_set.add(letter_comb)
                    best_guesses.append((count, weight, w))
        if len(best_guesses) == 0:
            best_guesses = [(1,1,solutions[0])]
        if (words!=solutions):
            unique_char_guesses = []
            for s in best_guesses:
                if len(set(s[2]))==len(s[2]):
                    unique_char_guesses.append(s)
            best_guesses = unique_char_guesses
        list.sort(best_guesses, key=lambda g: sum(list(map(lambda c: letter_freq[c], [f for f in g[2]])))/5, reverse=True)
        list.sort(best_guesses, key=lambda g: g[1], reverse=True)
        return [g[2] for g in best_guesses]
    
    print(f"\nTo attempt solve you should guess one of: %s"%generate_guesses())
    print(f"\nTo narrow solutions you should guess one of: %s"%generate_guesses(freq.keys()))


