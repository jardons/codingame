# A more common solution with far less code is possible with a coplexity level of O(N * D) where N is the Number of char to parse and D the size of the Dictionary.
# The current solution is proposing a complexity of O(N * P) where P is the number of simultaneous word in Progress.
# Even if calculating a value for P, this value will always be a subset of D, and is evaluated to 25 for the last test case of codigame.
# When comparing using benchamrk, this solution was 10 time faster that the O(N * D) one.

import sys
import math
import itertools

# Class generating a graph representation of the dictionary, allowing validation through graph navigation.
class Word:
    def __init__(self, words=None):
        self.content, self.isWord = {}, False

        if words is None: return

        for w in words:
            node = self
            for c in w:
                if c not in node.content: node.content[c] = Word()
                node = node.content[c]
            node.isWord = True

MORSE = {
    '.': 'E', '-': 'T',
    '..': 'I', '-.': 'N',  '.-': 'A', '--': 'M',
    '...': 'S', '-..': 'D', '.-.': 'R', '--.': 'G',
    '..-': 'U', '-.-': 'K',  '.--': 'W', '---': 'O',
    '....': 'H', '-...': 'B', '.-..': 'L', '--..': 'Z',
    '..-.': 'F', '-.-.': 'C',  '.--.': 'P', '...-': 'V',
    '-..-': 'X',  '--.-': 'Q', '-.--': 'Y', '.---': 'J'
}

# Parse inputs
data = input()
dictionary = Word((input() for i in range(int(input()))))

# Parse string
state = [ [[1, dictionary]], [], [], [] ]
for i in range(len(data)):
    present,empty = [], None
    for j in range(min(len(state), i+1)):
        m = data[(i-j):(i+1)]
        if m not in MORSE: continue

        c = MORSE[m]

        for entry in (e for e in state[j] if c in e[1].content):

            # Move down in graph.
            next = entry[1].content[c]

            # If we have a final word, restart from beginning of dictionary for new word.
            if next.isWord:
                if empty is None:
                    empty = [entry[0], dictionary]
                    present.append(empty)
                else:
                    empty[0] += entry[0]
            
            present.append([entry[0], next])
    
    # Move state further in past or next iteration.
    # The one that didn't match any morse code will disapear after the fourth attempt.
    state[0], state[1], state[2], state[3] = present, state[0], state[1], state[2]

print(sum( (t[0] for t in state[0] if t[1].isWord) ))
