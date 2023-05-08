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

* About 2-3 sentences to explain each piece of the implementation.


* Code snippets from your files.

* first of all to classify the grammar acording to chomsky hierchy i created a function called classify_grammer(in the grammar file) that takes atr. the grammar(the production table) and classifies it by checking the grammer against every type's rule

* to convert the FA back to a grammer i added a the function "fa_to_grammer"(in the automaton file) that takes the automaton as an atr and converts into a grammer by looking at the transactions and taking every state and deriving it to the production first and secound element and to just the first if it's a terminal state.

* after that i implemented the nfa to dfa conversion algorithm using the powerset construction alogrithm in the function nfa_to_dfa that takes the nfa and the start state as atributes and generates a dfa using the new class FA that constructs FA's for convinient use.

* to determine if the FA is deterministic or not i implemented a methode in the automaton file that checks if the automaton has duplicated transitions or epsilon transition from each state.

* i tried implementing the graphical presentation using visual_automata library but i kept giving me an infinite automaton error although it reaches all the end states normally so i just printed all the vertices and nodes in the terminal

* for testing i created 4 additional grammers to check the classify methode and for the dfa to grammer methode i generated the new grammer and compared it to the original one in the main file should be all the testing code and the results presented in the terminal if run

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

