# Chomsky Normal Form
### Course: Formal Languages & Finite Automata
### Author: Al Haj Ahmed (variant 1)
----

## Theory
Chomsky Normal Form(CNF) is the standard way to represent a context free language which easies the understanding and generating of string using this grammar type and it has two main restrictions: 
1. every production must be of the form N -> t or N -> NN in which "N" stands for a nonterminal and "t" for a terminal symbol
2.the grammar must be normalized first which means it has to have:
  a. no epsilon productions
  b. no unit productins
  c. no nonproductive or inaccesable symbols


## Objectives:

* Learn about Chomsky Normal Form (CNF) [1].
* Get familiar with the approaches of normalizing a grammar.
* Implement a method for normalizing an input grammar by the rules of CNF.
    The implementation needs to be encapsulated in a method with an appropriate signature (also ideally in an appropriate class/type).
    The implemented functionality needs executed and tested.
* A BONUS point will be given for the student who will have unit tests that validate the functionality of the project.
* Also, another BONUS point would be given if the student will make the aforementioned function to accept any grammar, not only the one from the student's variant.

## Implementation description

first we start by defining the grammar:
for that i created a class Grammar which takes all the grammar elements (Vn,Vt,S,P)
```
class Grammar:
    def __init__(self, S, Vn, Vt, productions):
        self.S = S
        self.Vn = Vn
        self.Vt = Vt
        self.productions = productions
```
i had the first variant so for me this will look like this:
```
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
```
now we need to normalize it, the first step in normalizing is to get rid of any epsilon production
so i made a loop that goes through the productions and check for any None production, delete them and then add that non-terminal to a list for the next step 
then we check if the epsilon production was the only one for this nonterminal which was in my case so we delete that as well
```
    for nonterminal in grammar.productions:
        index = 0
        for terminal in grammar.productions[nonterminal]:
            if terminal == None:
                del grammar.productions[nonterminal][index]
                epsilon.append(nonterminal)
            index += 1
    delete = []
    for nonterminal in grammar.productions:
        if len(grammar.productions[nonterminal]) == 0:
            delete.append(nonterminal)
    for nonterminal in delete:
        del grammar.productions[nonterminal]
```
next we need to add the new productions without the epsilon nonterminal 'C'
these if statements are all in a for loop that goes through the productions of the grammar (i implemented more than one thing in the same loop to reduce cost)
```
                if letter in epsilon:
                    grammar.productions[nonterminal].append(terminal.replace(letter,''))
```
here i check for elements if they're accesable or not and if yes i add them to a list to find the inaccesable symbols later
```
accesable = []
 if letter.isupper() and letter not in accesable:
     accesable.append(letter)
```
next we find the unit productions and mark them for deletion(cuz deleting them on the spot messes up with the indexes and results in skipping some symbols)
and add thier production to the initial symbol
i mark the symbol for deletion by adding it to a list as a tuple (nonterminal,index) *check tests for more info
```
                if len(terminal) == 1 and letter.isupper():
                    for item in grammar.productions[letter]:
                        grammar.productions[nonterminal].append(item)
                    if nonterminal == temp:
                        delete_T.append((nonterminal,index-n))
                        n += 1
                    else:
                        delete_T.append((nonterminal,index))
                        temp = nonterminal
                        n = 1
```
*the n is a solution for the indexes of the elements

next i mark all the other items that had the 'C' nonterminal in them for deletion as well(because we deleted it as it had no more production)
i add the deleted nonterminal to a list call delete and then compare
```
                if letter in delete:
                    if nonterminal == temp:
                        delete_T.append((nonterminal,index-n))
                        n += 1
                    else:
                        delete_T.append((nonterminal,index))
                        temp = nonterminal
                        n = 1
```
next i delete the inaccesable symbols ( i don't need to mark these ones as we delete the whole production group and because they're inaccesable that means they're not in any other production)
```
index = 0
    for nonterminal in grammar.Vn:
        if nonterminal not in accesable:
            del grammar.Vn[index]
            del grammar.productions[nonterminal]
        if nonterminal in delete:
            del grammar.Vn[index]
        index += 1
```
next we check for non productve symbols (by my understanding a non-productive symbol is one that as soon as you enter it's production group you cant exit and you stay in a loop)
and that's what i check for
```
productive = False
    delete_N = []
    for nonterminal in grammar.productions:
        for terminal in grammar.productions[nonterminal]:
            if nonterminal not in terminal:
                productive = True
        if productive == False:
            delete_N.append(nonterminal)
```
and if one is found we need to delete it an all the terms that has that non-terminal in it
```
temp = ''
    for item in delete_N:
        del grammar.productions[item]

        for nonterminal in grammar.productions:
            index = 0
            for terminal in grammar.productions[nonterminal]:
                if item in terminal:
                    if temp == nonterminal:
                        delete_T.append((nonterminal,index-n))
                        n += 1
                    else:
                        delete_T.append((nonterminal,index))
                        n = 1
```
*the temp is for the same index issue mentioned earlier

and now i delete all the marked terms
```
 for symbol in delete_T:
        del grammar.productions[symbol[0]][symbol[1]]
```
now we got rid of everything so we need to transform the productions to the normal form
in my case i had the terms in pairs of letters so i wrote the code just for that
it works by finding the terms that are not in the normal form and adding a new production for the terminal symbol and transforming the term into the normal form
```
n = 1
    temp = {}
    for nonterminal in grammar.productions.copy():
        index = 0
        for terminal in grammar.productions[nonterminal]:
            done = False
            if terminal.isupper() or terminal.islower():
                index += 1
                continue
            else:
                if len(terminal) == 2:
                    for letter in terminal:
                        if letter.islower():
                            for key in temp:
                                for val in temp[key]:
                                    if val == letter:
                                        grammar.productions[nonterminal][index] = grammar.productions[nonterminal][index].replace(letter,key)
                                        done = True
                                        break
                                if done == True:
                                    break
                            if done == False:
                                grammar.productions[f'X{n}'] = [letter]
                                temp[f'X{n}'] = [letter]
                                grammar.productions[nonterminal][index] = grammar.productions[nonterminal][index].replace(letter,f'X{n}')
                                n += 1
```
## Conclusions / Screenshots / Results
Results:
i show what happens to the productions after each step to test the functionallity of each piece of code
so the results look smth like this:
```
the grammar
{'S': ['aB', 'AC'], 'A': ['a', 'ASC', 'BC', 'aD'], 'B': ['b', 'bS'], 'C': [None], 'D': ['abC'], 'E': ['aB']}
eliminate epsilon production
{'S': ['aB', 'AC'], 'A': ['a', 'ASC', 'BC', 'aD'], 'B': ['b', 'bS'], 'D': ['abC'], 'E': ['aB']}
add the unit productions and epsilon substitutions
{'S': ['aB', 'AC', 'A', 'a', 'ASC', 'BC', 'aD', 'AS', 'B', 'b', 'bS'], 'A': ['a', 'ASC', 'BC', 'aD', 'AS', 'B', 'b', 'bS'], 'B': ['b', 'bS'], 'D': ['abC', 'ab'], 'E': ['aB']}
mark the unit and empty productions (C) for deletion and add them here in form (nonterminal,index)
[('S', 1), ('S', 1), ('S', 2), ('S', 2), ('S', 4), ('A', 1), ('A', 1), ('A', 3), ('D', 0)]
delete inaccesable oroductions
{'S': ['aB', 'AC', 'A', 'a', 'ASC', 'BC', 'aD', 'AS', 'B', 'b', 'bS'], 'A': ['a', 'ASC', 'BC', 'aD', 'AS', 'B', 'b', 'bS'], 'B': ['b', 'bS'], 'D': ['abC', 'ab']}
delete marked productions
{'S': ['aB', 'a', 'aD', 'AS', 'b', 'bS'], 'A': ['a', 'aD', 'AS', 'b', 'bS'], 'B': ['b', 'bS'], 'D': ['ab']}
transform into normal form(CNF)
{'S': ['X1B', 'a', 'X1D', 'AS', 'b', 'X2S'], 'A': ['a', 'X1D', 'AS', 'b', 'X2S'], 'B': ['b', 'X2S'], 'D': ['ab'], 'X1': ['a'], 'X2': ['b']}
```


