### Course: Formal Languages & Finite Automata
### Author: Al Haj Ahmed FAF211

----

## Theory
* what's a FA? an FA is more of a checking mechanism and a better way to represent a formal language, it's a set of nodes(non-terminal var's) connected by            vertices(terminal variables) that represent the language's states,transetions,final states and initial state.
* to convert a FA into a grammer we need to look mainly on the transitions of the automaton, our non-terminal variables will be the states, the terminal will be the 
values in the transitions (the value on the vertice) and the initial state is indicated by the arrow, and final states by circles.
* the difference between DFA and NFA is very simple: in a DFA every node(nonterminal var) has one and only one transition for each terminal variable to a next state and NFA have more than one and epsilon transitions.
* The powerset construction algorithm is a method used to find all possible subsets of a given set. It works by iteratively building a new set of subsets, starting with the empty set, and adding each element of the original set to each existing subset to create new subsets.

## Objectives:

* Understand what an automaton is and what it can be used for.
* Implement conversion of a finite automaton to a regular grammar.
* Determine whether your FA is deterministic or non-deterministic.
* Implement some functionality that would convert an NDFA to a DFA.
* Represent the finite automaton graphically


## Implementation description
* first of all to classify the grammar acording to chomsky hierchy i created a function called classify_grammer(in the grammar file) that takes atr. the grammar(the production table) and classifies it by checking the grammer against every type's rule

first we check if the grammer is regular by checking the number of non-terminals on the left and if it matches we check the right side of the production to check if it's left or right side production
```
        for production in grammar[nonterminal]:
            if len(production) > 2:
                is_regular = False
                break
            if len(production) == 2:
                if (production[0].islower() and production[1].islower()) or (production[0].isupper() and production[1].isupper()):
                    is_regular = False
                    break
```
then we check if the grammer is a context free grammer by checking if the number of the nonterminals in the right side larger or equal to the left side
```
        for production in grammar[nonterminal]:
            if len(production) < len(nonterminal) or len(nonterminal) < 2:
                is_context_sensitive = False
                break
        if not is_context_sensitive:
            break
    if is_context_sensitive:
        return "Type 2: Context-free grammar"
```
then we Check if the grammar is a context-free grammar and after excluding that it can't be niether regular or context-free we just need to check that the left part non-terminals are more than one symbol
```
is_context_free = True
    for nonterminal in grammar:
        if len(nonterminal) > 1:
            is_context_free = False
    if is_context_free:
        return "Type 1: Context-sensitive grammar"
```
and if none of the above it's type 0
```
 If none of the above conditions are met, the grammar is an unrestricted grammar
    return "Type 0: Unrestricted grammar"
```

* to convert the FA back to a grammer i added a the function "fa_to_grammer"(in the automaton file) that takes the automaton as an atr and converts into a grammer by looking at the transactions and taking every state and deriving it to the production first and secound element and to just the first if it's a terminal state.
we take the transition table from the automaton as an attribute and use it to create the production table(grammer) as we take every nonterminal from the transitions and pair it with the left side one by one
```
grammer = []
    for state in automaton['transitions']:
        num = 0
        for transition in automaton['transitions'][state]:
            if automaton['transitions'][state][num][1] == None:
                grammer.append(state + " -> " + automaton['transitions'][state][num][0])
            else:
                grammer.append(state + " -> " + automaton['transitions'][state][num][0] + automaton['transitions'][state][num][1])
            num = num + 1

    return grammer
```

* after that i implemented the nfa to dfa conversion algorithm using the powerset construction alogrithm in the function nfa_to_dfa that takes the nfa and the start state as atributes and generates a dfa using the new class FA that constructs FA's for convinient use.
first we need to calculate epsilon closoure so we take the start symbol and look for any epsilon transaction in the nfa and return the start symbol or the combination(frozenset) of symbols
```
 closure = set(states)
    queue = list(states)
    while queue:
        curr_state = queue.pop(0)
        for next_state in nfa.transitions.get((curr_state, None), []):
            if next_state not in closure:
                closure.add(next_state)
                queue.append(next_state)
    return frozenset(closure)
```
then starting from the start symbol that we calculated with the epsilon closure we start to go through each symbol and go through the transitions adding every new symbol or frozenset to the symbols and checking every combination until the last symbol.
```
# Process the remaining states of the DFA
    queue = [dfa_start_state]
    while queue:
        curr_state = queue.pop(0)

        # Compute the transitions from the current state on each input symbol
        for symbol in nfa.alphabet:
            next_states = set()
            for state in curr_state:
                next_states |= set(nfa.transitions.get((state, symbol), []))
            next_states = epsilon_closure(nfa, next_states)

            if next_states:
                # Add the new state and transition to the DFA
                if next_states not in dfa_states:
                    dfa_states.add(next_states)
                    if any(state in nfa.accept_states for state in next_states):
                        dfa_accept_states.add(next_states)
                    queue.append(next_states)
                dfa_transitions[(curr_state, symbol)] = next_states
 ```
 then we construct the new DFA from the new transitions without the epsilon transitions
 ```
 # Create the DFA object
    dfa = FA(dfa_states, nfa.alphabet, dfa_transitions, dfa_start_state, dfa_accept_states)
    return dfa
```
* to determine if the FA is deterministic or not i implemented a methode in the automaton file that checks if the automaton has duplicated transitions or epsilon transition from each state.
```
    for state in automaton['transitions']:
        for production in automaton['transitions'][state]:
            if production[0][0] == '':
                return False
            num = 0
            for _ in automaton['transitions'][state]:
                if production[0][0] == _[0][0]:
                    num = num + 1
                    if num == 2:
                        return "the FA isn't deterministic"
    return "the FA is deterministic"
```
* i tried implementing the graphical presentation using visual_automata library but i kept giving me an infinite automaton error although it reaches all the end states normally so i just printed all the vertices and nodes in the terminal
```
digraph G {
rankdir=LR;
S [fillcolor="#66cc33", style=filled];
Q [peripheries=2];
P [peripheries=2];
S -> P  [label=a];
S -> Q  [label=b];
Q -> Q  [label=e];
Q -> Q  [label=f];
Q -> Q  [label=a];
P -> P  [label=b];
P -> P  [label=c];
P -> Q  [label=d];
P -> P  [label=e];
}
```

* for testing i created 4 additional grammers to check the classify methode and for the dfa to grammer methode i generated the new grammer and compared it to the original one in the main file should be all the testing code and the results presented in the terminal if run
```
nfa = FA(nfa_states, nfa_alphabet, nfa_transitions, nfa_start_state, nfa_accept_states)

dfa = nfa_to_dfa(nfa, 'q0')
print("the productions of the DFA")
print(dfa.transitions)
print("\nthe original grammer is: " + classify_grammar(grammar))
print("the first grammer is: " + classify_grammar(grammer))
print("the secound grammer is: " + classify_grammar(grammer1))
print("the third grammer is: " + classify_grammar(grammer2))

print("\n" + Is_DFA(automaton))
```

## Conclusions / Screenshots / Results
in this lab i learned more about the NFA and DFA automatons and the main defirences between them and how to convert an NFA into a DFA in code (which wasn't easy) and learned more about every type in the chomsky hierchy and some interesting external libraries that have all this implemented that can be easly used.

## reuslts:
i kept the results as is from last lab to keep proof that everything works still 

the automaton based on the given grammar
{'states': {'S', 'Q', 'P'}, 'transitions': {'S': [('a', 'P'), ('b', 'Q')], 'Q': [('e', 'Q'), ('f', 'Q'), ('a', None)], 'P': [('b', 'P'), ('c', 'P'), ('d', 'Q'), ('e', None)]}, 'start_state': 'S', 'accepting_states': {'Q', 'P'}}

here are 5 words from given grammer
ada
acdfa
adfea
ada
bfefea

ace is in this grammer
ohno is not in this grammer

 the set of productions of the generated grammer
['S -> aP', 'S -> bQ', 'Q -> eQ', 'Q -> fQ', 'Q -> a', 'P -> bP', 'P -> cP', 'P -> dQ', 'P -> e']
True
equal to the original

the productions of the DFA
{(frozenset({'q0'}), 'a'): frozenset({'q0', 'q1'}), (frozenset({'q0', 'q1'}), 'c'): frozenset({'q1'}), (frozenset({'q0', 'q1'}), 'a'): frozenset({'q0', 'q1'}), (frozenset({'q0', 'q1'}), 'b'): frozenset({'q2'}), (frozenset({'q1'}), 'c'): frozenset({'q1'}), (frozenset({'q1'}), 'b'): frozenset({'q2'}), (frozenset({'q2'}), 'b'): frozenset({'q3'}), (frozenset({'q3'}), 'a'): frozenset({'q1'})}

the original grammer is: Type 3: Regular grammar
the first grammer is: Type 2: Context-free grammar
the secound grammer is: Type 1: Context-sensitive grammar
the third grammer is: Type 0: Unrestricted grammar

the FA is deterministic

digraph G {
rankdir=LR;
S [fillcolor="#66cc33", style=filled];
Q [peripheries=2];
P [peripheries=2];
S -> P  [label=a];
S -> Q  [label=b];
Q -> Q  [label=e];
Q -> Q  [label=f];
Q -> Q  [label=a];
P -> P  [label=b];
P -> P  [label=c];
P -> Q  [label=d];
P -> P  [label=e];
}


Process finished with exit code 0

