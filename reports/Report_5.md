# Parser & Building an Abstract Syntax Tree
### Course: Formal Languages & Finite Automata
### Author: Al Haj Ahmed
----

## Theory
The AST (Abstract Syntax Tree) is a hierarchical representation of the syntactic structure of the input code. It captures the essential components of the code, such as expressions, statements, declarations, and their relationships. Each node in the AST corresponds to a construct in the source code and contains information about the construct's type and its relationships with other constructs.

Parsers use a set of rules, often defined using a formal grammar, to analyze the input text and build the AST. These rules define the valid syntax and specify how the input should be structured. The parser processes the input according to these rules, and if the input adheres to the grammar, it constructs the corresponding AST. If the input violates the grammar, the parser usually produces an error or a diagnostic message indicating the issue.


## Objectives:

* Get familiar with parsing, what it is and how it can be programmed.
* Get familiar with the concept of AST.
* In addition to what has been done in the 3rd lab work do the following:
* Implement the necessary data structures for an AST that could be used for the text you have processed in the 3rd lab work.
* Implement a simple parser program that could extract the syntactic information from the input text.

## Implementation description
in this lab i implement a simple parser that parses any simple arithmic expressions partially using my previous lexer to tokenize the input strings 

First We define a class called Node that represents a node in the Abstract Syntax Tree (AST). Each node has a node_type attribute that represents the type of the node (e.g., "integer", "PLUS", "MINUS", etc.), a value attribute that holds the value of the node (for integer nodes), and a children list that stores the child nodes.
```
class Node:
    def __init__(self, node_type, value=None):
        self.node_type = node_type
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)
```
The Parser class is defined, which is responsible for parsing the input tokens and constructing the AST. It has several methods:

The __init__ method initializes the parser by setting the tokens, current token, and current index.
```
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.current_index = -1
        self.advance()
```
The advance method updates the current token and current index to move to the next token in the list.
```
 def advance(self):
        self.current_index += 1
        if self.current_index < len(self.tokens):
            self.current_token = self.tokens[self.current_index]
        else:
            self.current_token = None
```
The parse method is the entry point of the parser. It calls the expression method to parse the input and construct the AST.
```
    def parse(self):
        return self.expression()
```
The factor method handles parsing of factors, which can be integers or expressions enclosed in parentheses.
```
    def factor(self):
        token_type, token_value = self.current_token
        if token_type == "INTEGER":
            self.advance()
            return Node("integer", value=int(token_value))
        elif token_type == "LPAREN":
            self.advance()
            result = self.expression()
            if self.current_token[0] != "RPAREN":
                raise SyntaxError("Expected ')'")
            self.advance()
            return result
        else:
            raise SyntaxError("Invalid token")
 ```
 The term method handles parsing of terms, which consist of factors multiplied or divided by other factors.
 ```
     def term(self):
        result = self.factor()
        while self.current_token and self.current_token[0] in ('MULTIPLY', 'DIVIDE'):
            operator = self.current_token[0]  # Get the token type instead of the token value
            self.advance()
            right = self.factor()
            result_node = Node(operator)
            result_node.add_child(result)
            result_node.add_child(right)
            result = result_node
        return result
```
The expression method handles parsing of expressions, which consist of terms added or subtracted from other terms.
```
 def expression(self):
        result = self.term()
        while self.current_token and self.current_token[0] in ('PLUS', 'MINUS'):
            operator = self.current_token[0]  # Get the token type instead of the token value
            self.advance()
            right = self.term()
            result_node = Node(operator)
            result_node.add_child(result)
            result_node.add_child(right)
            result = result_node
        return result
```
The evaluate method is added to the Parser class to recursively evaluate the AST and compute the result of the expression.
It traverses the AST and performs the corresponding operations based on the node types.
```
    def evaluate(self, node):
        if node.node_type == "integer":
            return node.value
        elif node.node_type == "PLUS":
            return self.evaluate(node.children[0]) + self.evaluate(node.children[1])
        elif node.node_type == "MINUS":
            return self.evaluate(node.children[0]) - self.evaluate(node.children[1])
        elif node.node_type == "MULTIPLY":
            return self.evaluate(node.children[0]) * self.evaluate(node.children[1])
        elif node.node_type == "DIVIDE":
            return self.evaluate(node.children[0]) / self.evaluate(node.children[1])
        else:
            raise ValueError("Invalid node type: " + node.node_type)
```
## Conclusions / Screenshots / Results
i modified the lexer slightly as it was just printing the types of the tocken now i add them and classify them and add them to the 'tokens' list after which i construct the AST and calculate the arithmic expression at last
Results:
```
token: number Value: 5
token: Symbol Value: +
token: Symbol Value: (
token: number Value: 7
token: Symbol Value: -
token: number Value: 3
token: Symbol Value: )
token: Symbol Value: *
token: number Value: 3
token: Symbol Value: +
token: number Value: 17
token: Symbol Value: *
token: number Value: 3
[('INTEGER', '5'), ('PLUS', '+'), ('LPAREN', '('), ('INTEGER', '7'), ('MINUS', '-'), ('INTEGER', '3'), ('RPAREN', ')'), ('MULTIPLY', '*'), ('INTEGER', '3'), ('PLUS', '+'), ('INTEGER', '17'), ('MULTIPLY', '*'), ('INTEGER', '3')]
AST:
PLUS None
  PLUS None
    integer 5
    MULTIPLY None
      MINUS None
        integer 7
        integer 3
      integer 3
  MULTIPLY None
    integer 17
    integer 3

Result: 68
```
## Conclusions
during this lab i learned more about how a top down parser is build and how does it works, how all the different elements interact with eachother to complete the language which will be complied, i understood more about formal languages and how does our IDE's recognize different commands or "tokens" and how is it optimized and build in our software although what i did is a very simplified version it was very fun to learn more about formal language and parsing.
