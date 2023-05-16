
def tokenize(string):
    symbols = ['{', '}', '(', ')', '[', ']', '.', '*', ':', ',', '=', '+', '-', ';'] # single-char keywords
    punctiuation = ["'", '"']
    long_comment = ['/*', '*/'] # multi-char keywords
    short_comment = ['#','//']
    keywords = ['public', 'main','static', 'void','for','System', 'out', 'print']
    oprerators = ['String', 'int', 'double', 'float', 'bool', 'list', 'class']
    KEYWORDS = symbols + long_comment + keywords + short_comment + oprerators

    white_space = ' '
    lexeme = ''
    lexems = []
    for i,char in enumerate(string):
        if char == '*':
            if string[i-1] == '/':
                lexeme += '/*'
            elif string[i+1] == '/':
                lexeme += '*/'
            else:
                lexeme += '*'
        elif char == '/':
            if string[i+1] != '*' and string[i-1] != '*':
                lexeme += '/'
            else:
                continue
        elif char == '\n':
            lexems.append(lexeme)
            lexeme = ''
        else:
            if char != white_space:
                lexeme += char # adding a char each time
        if (i+1 < len(string)): # prevents error
            if string[i+1] == white_space or string[i+1] in KEYWORDS or lexeme in KEYWORDS: # if next char == ' '
                if lexeme != '':
                    #print(lexeme.replace('\n', '<newline>'))
                    lexems.append(lexeme)
                    lexeme = ''
    isComment = False
    longComment = False
    isOperator = False
    isPunct = False
    definers = []
    for string in lexems:
        if string in long_comment:
            print(f"token: comment_Operator Value: {string}")
            longComment = not longComment
        if string in short_comment:
            print(f"token: comment_Operator Value: {string}")
            isComment = True
        if (isComment == True) and (string == '\n') or (string == '!'):
            print(f"token: comment Value= !")
            print(f"token: <newLine>")
            isComment = False
        if isOperator == True and string not in symbols:
            print(f"token: Definer Value: {string}")
            isOperator = False
            definers.append(string)
        elif longComment == True or isComment == True:
            print(f"token: comment Value: {string}")
        elif string == '\n':
            print(f"token: <newline>")
        elif string in symbols:
            print(f"token: Symbol Value: {string}")
        elif string.isdigit():
            print(f"token: number Value: {string}")
        elif string in keywords:
            print(f"token: keyword Value: {string}")
        elif string in punctiuation:
            print(f"token: punctuation Value: {string}")
            isPunct = True
        elif string in oprerators:
            print(f"token: operator Value: {string}")
            isOperator = True
        elif string in definers:
            print(f"token: Definer Value: {string}")

    print(lexems)

