# The title of the work

### Course: Formal Languages & Finite Automata
### Author: Al Haj Ahmed FAF211

----

## Theory
what's a formal language? It's a set of rules, an alphabet and a bunch of transactions which define how the letters/symboles interact with each other to create a word 
in this lab-work we were tasked to learn more about the regular grammer and there's two kinds of it: left side and right, the difference between the is that the Non-terminal variable is on the left in the left one and on the right in the right one.

the main rules in this grammer is that you have to have one non-terminal variable on the left which can derevate to a terminal variable or a terminal var with a non terminal on it's right in order to get longer words, it's the most restricted grammer and used to model the human language and normal speech.

what do you need in a grammer ? first of all you need the alphabet(that's the symboles you'll use in your words) then you'll need to identify the terminal and non terminal variable, they're usually denoted by size so the big letters for non-terminal vars and the small for the terminal ones, next you'll need your production table in this table you need to put the rules and which non-terminal var goes to what terminal one and the different comboes that can be formed from this, you can try to imagine all the posabilites but usualy they're displayed in a derivation tree to be easly understood and modeled.

and lastly we have the automaton, what's an automaton? you wonder, well to put it simply it's a checking mechanism that checks different words if they belong in the grammer or language or not and it's done by the graph i mentioned earlier in which we check every symbol if it has a coresponding non terminal variable and if the whole word can be produced by our grammer, and automaton scans every symbol and compares it to the list of tuples that he has as the transactions of that grammer.


## Objectives:

* to create a git repository
* to choose a programming language
* create a prgrame that generates 5 word from the grammer 
* create a finite automaton that checks if a word belongs to the grammer


## Implementation description

* About 2-3 sentences to explain each piece of the implementation.


* Code snippets from your files.
the word generating function
```
grammar = {
    "S": ["aP", "bQ"],
    "P": ["bP", "cP","dQ","e"],
    "Q": ["eQ", "fQ","a"]

def generate_word(grammar, start_symbol):
    word = "S"
    current_symbol = start_symbol
    while True:
        if current_symbol not in grammar:  # if current symbol is terminal
            word += current_symbol  # add to the word
            current_symbol = "end"
            if not word:  # if the word is empty, return None
                return None
            if len(word) > 10:  # if word is too long, return None
                return None
            if current_symbol == "end":  # if end symbol is reached, return the word
                word = word.replace("end","")
                return word[:-1]  # remove the end symbol

        else:
            rhs = random.choice(grammar[current_symbol])  # choose a random rule
            word = word.replace(current_symbol,rhs[0])
            for symbol in rhs[1:]:
                word += symbol
            current_symbol = word[-1]  # set current symbol to the last character in the word
 ```
 the automaton creating code 
 ```
 def create_automaton(grammar):
    # Step 1: Define the states of the automaton
    states = set([rule[0] for rule in grammar])

    # Step 2: Define the transitions between states
    transitions = {}
    for state in states:
        for rule in grammar:
            if rule[0] == state:
                if rule[1] == "":
                    # Epsilon transition
                    if state in transitions:
                        transitions[state].append((rule[2], None))
                    else:
                        transitions[state] = [(rule[2], None)]
                else:
                    # Regular transition
                    if state in transitions:
                        transitions[state].append((rule[2], rule[1]))
                    else:
                        transitions[state] = [(rule[2], rule[1])]

    # Step 3: Identify the start state of the automaton
    start_state = grammar[0][0]

    # Step 4: Identify the accepting states of the automaton
    accepting_states = set()
    for state in states:
        for rule in grammar:
            if rule[0] == state and rule[1] == "":
                accepting_states.add(state)

    # Construct the automaton
    automaton = {"states": states,
                 "transitions": transitions,
                 "start_state": start_state,
                 "accepting_states": accepting_states}

    return automaton
```
 
 
 the checking mechanism that checks the word to the automaton created
```
def accepts(automaton, word):
    current_state = automaton['start_state']
    for char in word:
        exists = False
        for symbol in automaton['transitions'][current_state]:
            if char == symbol[0]:
                current_state = symbol[1]
                exists = True

        if current_state is None:
            print(f"{word} is in this grammer")

        elif exists == False:
            # The current state does not have a transition on the current character
            print(f"{word} is not in this grammer")
            break
```



## Conclusions / Screenshots / Results
in this laboratory work i learned what's an automaton and how to implement them in code which was the most diffecult part and how to generate words in code and how to create it, i had some help and had to rewrite the code a couple of times but i got it working eventually, i hope i learned smth at least and looking forword to next lab.

## reuslts:
the automaton created:
{'states': {'S', 'P', 'Q'}, 'transitions': {'S': [('a', 'P'), ('b', 'Q')], 'P': [('b', 'P'), ('c', 'P'), ('d', 'Q'), ('e', None)], 'Q': [('e', 'Q'), ('e', 'Q'), ('f', 'Q'), ('a', None)]}, 'start_state': 'S', 'accepting_states': {'P', 'Q'}}

here are 5 words from given grammer
ace
befa
accbbbdea
None
ae

ace is in this grammer
ohno is not in this grammer
