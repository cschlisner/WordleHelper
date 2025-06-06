INCORRECT_LETTERS = "esirclokhn"
CORRECT_LETTERS = "atu"
CORRECT_PLACEMENT = ['','a','','','']
INCORRECT_PLACEMENT = [['a'],[''],['u'],['a'],['t']]

############################################################
import json
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# import csv
# freq = {}
# with open('unigrams_freq_5let.csv', 'r') as f:
#     r = csv.reader(f)
#     for row in r:
#         freq[row[0]] = int(row[1])
# sol_freq = {}
# with open('wordle_possibles.csv', 'r') as f:
#     wp = csv.reader(f)
#     for w in wp:
#         sol_freq[w[0]] = int(freq.get(w[0],9000))
# with open('solution_freq.json', 'w') as f:
#     json.dump(sol_freq, f)
# exit()

with open('solution_freq.json', 'r') as f:
    dictionary = json.load(f)

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

print("possible solutions:")
list.sort(solutions, key=lambda w: dictionary[w], reverse=True)
print(solutions)

if (len(solutions)>1):
    unknown_letters = list(dict.fromkeys(''.join(solutions)))
    unknown_letters = [s for s in unknown_letters if s not in CORRECT_LETTERS]
    if len(solutions) > 10:
        list.sort(unknown_letters, key=lambda l: letter_freq[l], reverse=True)
    print(f"\nunknown letters: %s"%unknown_letters)
    def generate_guesses(words = solutions):
        guess_set = set()
        best_guesses = []
        for w in words:
            count = 0
            weight = 0
            for c in INCORRECT_LETTERS:
                if c in w:
                    count=-100
            for c in CORRECT_LETTERS:
                if c in w:
                    if words != solutions:
                        count += -100
                    else: 
                        count += 1
                        weight += len(unknown_letters)
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
    print(f"\nTo narrow solutions you should guess one of: %s"%generate_guesses(dictionary.keys()))


