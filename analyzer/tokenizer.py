import re

classes = [  # ('Keyword', r'for|if|else|while|elif|def'),
    ('For', r'for'),
    ('If', r'if'),
    ('Else', r'else'),
    ('While', r'while'),
    ('Elif', r'elif'),
    ('Def', r'def'),
    ('Init', r'init'),
    ('Print', r'print'),
    ('Datatypes', r'int|str|complex|list|range|bool'),
    ('LeftParenthesis', r'\('),
    ('RightParenthesis', r'\)'),
    ('LeftCurly', r'\{'),
    ('RightCurly', r'\}'),
    ('LeftSquare', r'\['),
    ('RightSquare', r'\]'),
    ('SemiColon', r'\;'),
    ('Colon', r'\:'),
    ('Comma', r'\,'),
    ('RelOp', r'(<=)|(>=)|(<>)|(==)|or|and|not|(<)|(>)'),
    ('Assignment', r'='),
    # ('Or', r'or|and|not'),
    # ('And', r'and'),
    # ('Not', r'not'),
    ('MSO', r'\+|\-'),
    ('MFO', r'\%|\*|\/'),
    ('Literal', r'(\"(.+?)\")|([\d]+)|([\d]*.[\d]+)|(true)|(false)'),
    ('Increment', r'\+\+'), ('Decrement', r'\--'),
    ('Identifier', r'[A-Za-z_]+'),
    ('Whitespace', r'[\n]|[ \t]+'),
    ('Unknown', r'.')
]

tokens_join = '|'.join('(?P<%s>%s)' % x for x in classes)
# print(tokens_join)
lin_start = 0

token = []
lexeme = []
lexemeList = []
cleanCodeFile = open('analyzer/cleanCode.txt', 'r')
code = cleanCodeFile.read()
cleanCodeFile.close()

for m in re.finditer(tokens_join, code):
    print(m.lastgroup)
    token_type = m.lastgroup
    token_lexeme = m.group(token_type)
    # print(f"[{token_type}, {token_lexeme}]")

    if token_type == 'Whitespace':
        continue
    else:
        token.append(token_type)
        lexeme.append(token_lexeme)
        lexemeList.append(f"< {token_type},{token_lexeme} >")
        # lexemeList.append(token_lexeme)

        # return token, lexeme, row, column
lexemes = '\n'.join(lexemeList)
lexemesFile = open("lexemes.txt", 'w')
lexemesFile.write(lexemes)
lexemesFile.close()
