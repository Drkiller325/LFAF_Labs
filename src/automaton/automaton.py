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

    # Check if the final state is accepting


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


def fa_to_grammar(automaton):
    """
    Converts a finite automaton to a regular grammar in Chomsky normal form.

    Args:
    - the automaton

    Returns:
    - grammar (list): the set of productions of the regular grammar in Chomsky normal form
    """
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

def nfa_to_dfa(nfa, start_state):
    """Converts an NFA to a DFA using the powerset construction algorithm."""
    dfa_states = set()
    dfa_transitions = {}
    dfa_start_state = frozenset([start_state])
    dfa_accept_states = set()

    # Compute the epsilon closure of the start state
    start_closure = epsilon_closure(nfa, dfa_start_state)

    # Add the start state and its epsilon closure to the DFA
    dfa_states.add(dfa_start_state)
    if any(state in nfa.accept_states for state in start_closure):
        dfa_accept_states.add(dfa_start_state)

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

    # Create the DFA object
    dfa = FA(dfa_states, nfa.alphabet, dfa_transitions, dfa_start_state, dfa_accept_states)
    return dfa


def epsilon_closure(nfa, states):
    """Computes the epsilon closure of a set of NFA states."""
    closure = set(states)
    queue = list(states)
    while queue:
        curr_state = queue.pop(0)
        for next_state in nfa.transitions.get((curr_state, None), []):
            if next_state not in closure:
                closure.add(next_state)
                queue.append(next_state)
    return frozenset(closure)

class FA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states


def Is_DFA(automaton):
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
