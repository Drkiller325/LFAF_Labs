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
