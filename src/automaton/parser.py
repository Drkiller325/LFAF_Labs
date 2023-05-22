class Node:
    def __init__(self, node_type, value=None):
        self.node_type = node_type
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.current_index = -1
        self.advance()

    def advance(self):
        self.current_index += 1
        if self.current_index < len(self.tokens):
            self.current_token = self.tokens[self.current_index]
        else:
            self.current_token = None

    def parse(self):
        return self.expression()

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
