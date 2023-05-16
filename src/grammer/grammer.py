import random
import math
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

# Classify the grammar according to the Chomsky hierarchy
def classify_grammar(grammar):
    # Check if the grammar is a regular grammar
    is_regular = True
    for nonterminal in grammar:
        if len(nonterminal) > 1:
            is_regular = False
        for production in grammar[nonterminal]:
            if len(production) > 2:
                is_regular = False
                break
            if len(production) == 2:
                if (production[0].islower() and production[1].islower()) or (production[0].isupper() and production[1].isupper()):
                    is_regular = False
                    break
        if not is_regular:
            break
    if is_regular:
        return "Type 3: Regular grammar"

    # Check if the grammar is a context-sensitive grammar
    is_context_sensitive = True
    for nonterminal in grammar:
        for production in grammar[nonterminal]:
            if len(production) < len(nonterminal) or len(nonterminal) < 2:
                is_context_sensitive = False
                break
        if not is_context_sensitive:
            break
    if is_context_sensitive:
        return "Type 2: Context-free grammar"

    # Check if the grammar is a context-free grammar
    is_context_free = True
    for nonterminal in grammar:
        if len(nonterminal) > 1:
            is_context_free = False
    if is_context_free:
        return "Type 1: Context-sensitive grammar"

    # If none of the above conditions are met, the grammar is an unrestricted grammar
    return "Type 0: Unrestricted grammar"


class Grammar:
    def __init__(self, S, Vn, Vt, productions):
        self.S = S
        self.Vn = Vn
        self.Vt = Vt
        self.productions = productions


def normalize(grammar):
    epsilon = []
    print("the grammar")
    print(grammar.productions)
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

    print("eliminate epsilon production")
    print(grammar.productions)


    accesable = []
    delete_T = []
    temp = ''
    n = 0
    for nonterminal in grammar.productions:
        index = 0
        for terminal in grammar.productions[nonterminal]:
            for letter in terminal:

                if letter.isupper() and letter not in accesable:
                    accesable.append(letter)
                if letter in epsilon:
                    grammar.productions[nonterminal].append(terminal.replace(letter,''))

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

                if letter in delete:
                    if nonterminal == temp:
                        delete_T.append((nonterminal,index-n))
                        n += 1
                    else:
                        delete_T.append((nonterminal,index))
                        temp = nonterminal
                        n = 1
            index += 1

    print("add the unit productions and epsilon substitutions")
    print(grammar.productions)
    print('mark the unit and empty productions (C) for deletion and add them here in form (nonterminal,index)')
    print(delete_T)






    index = 0
    for nonterminal in grammar.Vn:
        if nonterminal not in accesable:
            del grammar.Vn[index]
            del grammar.productions[nonterminal]
        if nonterminal in delete:
            del grammar.Vn[index]
        index += 1

    print('delete inaccesable oroductions')
    print(grammar.productions)

    productive = False
    delete_N = []
    for nonterminal in grammar.productions:
        for terminal in grammar.productions[nonterminal]:
            if nonterminal not in terminal:
                productive = True
        if productive == False:
            delete_N.append(nonterminal)
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



    for symbol in delete_T:
        del grammar.productions[symbol[0]][symbol[1]]

    print('delete marked productions')
    print(grammar.productions)

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





            index += 1

    print('transform into normal form(CNF)')
    print(grammar.productions)




