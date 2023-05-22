from src.grammer.grammer import *
from src.automaton.automaton import *
from src.grammer.lexer import *
from src.automaton.parser import *
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

nfa_states = {'q0', 'q1', 'q2', 'q3'}
nfa_alphabet = {'a', 'b', 'c'}
nfa_transitions = {
    ('q0', 'a'): {'q0', 'q1'},
    ('q1', 'c'): {'q1'},
    ('q1', 'b'): {'q2'},
    ('q2', 'b'): {'q3'},
    ('q3', 'a'): {'q1'}
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

string = '''
public class Test {

   public static void main(String args[]) {
      int [] numbers = {10, 20, 30, 40, 50};
      // printing !
      for(int x : numbers ) {
         System.out.print( x );
         System.out.print(",");
      }
      System.out.print("\n");
      String [] names = {"James", "Larry", "Tom", "Lacy"};
      /*
      looping over 
      */
      for( String name : names ) {
         System.out.print( name );
         System.out.print(",");
      }
   }
}
'''

tokenize(string)

Vn = ['S','A','B','C','D','E']
Vt = ['a','b']
S = 'S'
P = {
    "S": ["aB", "AC"],
    "A": ["a", "ASC", "BC", "aD"],
    "B": ["b", "bS"],
    "C": [None],
    "D": ["abC"],
    "E": ["aB"]
}
grammar_1 = Grammar(S,Vn,Vt,P)

normalize(grammar_1)

string2 = '5+(7-3)*3+17*3 '
tokens = tokenize(string2)

parser = Parser(tokens)
ast = parser.parse()
def print_ast(node, indent=''):
    print(indent + str(node.node_type), node.value)
    for child in node.children:
        print_ast(child, indent + '  ')

print("AST:")
print_ast(ast)
result = parser.evaluate(ast)
print("\nResult:", result)