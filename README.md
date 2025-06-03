## Program that suggests best next guesses based on previous guesses in Wordle (https://www.nytimes.com/games/wordle/index.html)

## Usage
Fill out the following variables at the top of the file with your previous guess data (the `INCORRECT_PLACEMENT` variable can store multiple letters per place, just separate them with commas):

    INCORRECT_LETTERS = "es"
    CORRECT_LETTERS = "ai"
    CORRECT_PLACEMENT = ['a','','','i','']
    INCORRECT_PLACEMENT = [['m'],[''],['n'],[],[]]

and run the program:

    python wordlebot.py

output:

    possible solutions:
    ['again', 'audio', 'admin', 'avoid', 'audit', 'admit', 'avail', 'attic', 'alvin', 'alain', 'await', 'actin', 'anvil', 'affix', 'aphid', 'ambit', 'albin', 'anniv', 'aubin', 'auxin', 'antic', 'addio', 'antiq', 'amain', 'altin', 'admix', 'aalii', 'aboil', 'acmic', 'acoin', 'adfix', 'alcid', 'aldim', 'alfin', 'algic', 'algid', 'algin', 'alkin', 'aloid', 'aloin', 'alpid', 'alvia', 'amnia', 'amnic', 'andia', 'angia', 'anlia', 'anmia', 'anoia', 'anoil', 'apaid', 'apiin', 'atmid', 'attid', 'atwin', 'aulic', 'aumil', 'auxil', 'ax
    
    unknown letters: ['g', 'n', 'u', 'd', 'o', 'm', 'v', 't', 'l', 'c', 'w', 'f', 'x', 'p', 'h', 'b', 'q', 'k', 'z']
    
    To attempt solve you should guess one of: ['audio', 'admin', 'algin', 'algid', 'audit', 'aloin', 'avoid', 'acoin', 'admit', 'aloid', 'amnic', 'alvin', 'auxin', 'aumil', 'altin', 'aldim', 'actin', 'algic', 'atwin', 'aubin', 'axoid', 'aulic', 'again', 'alfin', 'alcid', 'admix', 'auxil', 'andia', 'anoia', 'antiq', 'albin', 'alpid', 'amain', 'addio', 'anniv', 'alkin', 'adfix', 'ambit', 'aboil', 'alain', 'attid', 'aphid', 'azoic', 'apiin', 'avail', 'acmic', 'attic', 'apaid', 'await', 'affix']
    
    To narrow solutions you should guess one of: ['mungo', 'mound', 'gluon', 'vodun', 'donut', 'dougl', 'fungo', 'novum', 'mount', 'mogul', 'wound', 'gconv', 'clung', 'found', 'mould', 'bungo', 'flung', 'count', 'pound', 'dough', 'contd', 'hound', 'thung', 'fount', 'bound', 'dungy', 'thong', 'moult', 'could', 'young', 'chung', 'gumbo', 'punto', 'tough', 'would', 'bonum', 'bundt', 'lough', 'locum', 'goudy', 'cough', 'clout', 'klong', 'pfund', 'month', 'doubt', 'blond', 'bunco', 'munch', 'mouth', 'flout', 'clown', 'guyot', 'punct', 'junto', 'blunt', 'muntz', 'gulch', 'gotch', 'pluto', 'flown', 'lunch', 'godly', 'unbox', 'cundy', 'notch', 'hoult', 'dutch', 'vouch', 'junco', 'bough', 'fudgy', 'touch', 'monty', 'boult', 'gowdy', 'gluck', 'mutch', 'louch', 'downy', 'clunk', 'gulph', 'bung, 'thumb', 'plonk', 'yukon', 'chunk', 'chump', 'blunk', 'kombu', 'plumb', 'bunty', 'bouch', 'whump', 'pouty', 'pylon', 'chomp', 'floyd', 'mycol', 'plomb', 'jumbo', 'youth', 'whomp', 'fultz', 'potch', 'octyl', 'butch', 'nobly', 'duchy', 'bucko', 'lumpy', 'muhly', 
    'comfy', 'botch', 'lofty', 'kutch', 'flock', 'pluck', 'howdy', 'jokul', 'funky', 'ducky', 'phony', 'lynch', 'phlox', 'butyl', 'wonky', 'plock', 'hotly', 'nymph', 'klutz', 'punky', 'mucky', 'hunky', 'block', 'humpy', 'chowk', 'tucky', 'glyph', 'bumpy', 'honky', 'lucky', 'zloty', 'locky', 'junky', 'jumpy', 'bothy', 'folky', 'lymph', 'jumby', 'bulky', 'pocky', 'bucky', 'hocky']
