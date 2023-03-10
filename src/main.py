from src.grammer.grammer import *
from src.automaton.automaton import *
from visual_automata.fa.dfa import VisualDFA
import visual_automata
from visual_automata.fa.nfa import *
from automata.fa.dfa import DFA
import os
os.environ["PATH"] += os.pathsep + 'D:/Program Files (x86)/Graphviz2.38/bin/'
# Define the regular grammar
grammar = {
    "S": ["aP", "bQ"],
    "P": ["bP", "cP","dQ","e"],
    "Q": ["eQ", "fQ","a"]
}
grammar1 = [("S","P","a"),("S","Q","b"),("P","P","b"),("P","P","c"),("P","Q","d"),
            ("P","","e"),("Q","Q","e"),("Q","Q","f"),("Q","","a")]

automaton = create_automaton(grammar1)
print("the automaton based on the given grammar")
print(automaton)

print("\nhere are 5 words from given grammer")
for _ in range(5):
    word = generate_word(grammar,"S")
    print(word)
print("")

accepts(automaton,"ace")
accepts(automaton,"ohno")

grammar2 = [
    "S -> aP",
    "S -> bQ",
    "P -> bP",
    "P -> cP",
    "P -> dQ",
    "P -> e",
    "Q -> eQ",
    "Q -> fQ",
    "Q -> a"
]
grammar3 = fa_to_grammar(automaton)
print("\n the set of productions of the generated grammer")
print(grammar3)

equal = True
for production in grammar3:
    if production in grammar2:
        equal = True
    else:
        equal = False
print(equal)
print("equal to the original\n")

nfa_states = {'q0', 'q1', 'q2'}
nfa_alphabet = {'0', '1'}
nfa_transitions = {
    ('q0', '0'): {'q0'},
    ('q0', '1'): {'q0', 'q1'},
    ('q1', '0'): {'q2'},
    ('q1', '1'): {'q2'},
    ('q2', '0'): {'q2'},
    ('q2', '1'): {'q2'}
}
nfa_start_state = 'q0'
nfa_accept_states = {'q2'}

nfa = FA(nfa_states, nfa_alphabet, nfa_transitions, nfa_start_state, nfa_accept_states)

dfa = nfa_to_dfa(nfa, 'q0')
print("the productions of the DFA")
print(dfa.transitions)

grammer = {
    "Sa": ["aaB","bS"],
    "aB": ["bB"]
}
grammer1 = {
    "S": ["aaB","Sb"],
    "B": ["bS","b"]
}
grammer2 = {
    "aa": ["aB","ss"],
    "BAs":["aaB","s"],
    "sA": ["a","bbs"]
}
print("\nthe original grammer is: " + classify_grammar(grammar))
print("the first grammer is: " + classify_grammar(grammer))
print("the secound grammer is: " + classify_grammar(grammer1))
print("the third grammer is: " + classify_grammar(grammer2))

print("\n" + Is_DFA(automaton))

new_dfa = DFA(
    states= {"S", "Q", "P"},
    input_symbols={'a', 'b', 'e', 'f', 'c', 'd'},
    transitions={
        "S": {'a': 'P', 'b': 'Q'},
        "Q": {'e': 'Q', 'f': 'Q', 'a': "Q"},
        "P": {'b': 'P', 'c': 'P', 'd': 'Q', 'e': "P"}
    },
    initial_state='S',
    final_states={"Q", "P"},
    allow_partial=True
)

print()
print(new_dfa.show_diagram())

