import random
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
