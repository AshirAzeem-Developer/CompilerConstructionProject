from analyzer import tokenizer


def validate(s, c, n, currentIndex):
    print(f"\n{s},{currentIndex}", end=" ")
    if len(s) < 1:
        return False
    if s[-1] == "$":
        if currentIndex == len(n) - 1:
            return True
    if s[-1] in c.keys():  # c.keys() to check if non-terminal
        x = c[s[-1]]
        s.pop()
        for y in x:
            j = len(y) - 1
            i = len(y) - 1
            while i >= 0:
                ch = y[i]
                s.append(ch)
                i = i - 1
            if validate(s, c, n, currentIndex):
                return True
            else:
                for k in range(j):
                    if len(s) > 1:
                        s.pop()
                        # s.pop()
        return False
    else:
        terminal = s.pop()
        if terminal == n[currentIndex]:
            currentIndex = currentIndex + 1
            return validate(s, c, n, currentIndex)
    return False


c = dict()
c["<Body>"] = [["<Statement>", "<Body>"], []]
c['<Statement>'] = [["<Initialize>"], ["<Operation>"], ["<CondStat>"], ["<Loop>"], ["<Print>"]]  # , ["<FunctionCall>"]

c["<Initialize>"] = [["Init", "Identifier", "Assignment", "<Expr>"]]
c["<Operation>"] = [["Identifier", "Assignment", "<Expr>"]]
c["<Expr>"] = [["<Term>", "<Expr2>"]]
c["<Expr2>"] = [["MSO", "<Term>", "<Expr2>"], []]
c["<Term>"] = [["<Factor>", "<Term2>"]]
c["<Term2>"] = [["MFO", "<Factor>", "<Term2>"], []]
c["<Factor>"] = [["LeftParenthesis", "<Expr>", "RightParenthesis"], ["Identifier"], ["Literal"]]

c["<CondStat>"] = [["<If>", "<Else>"]]
c["<If>"] = [["If", "LeftParenthesis", "<RelExpr>", "RightParenthesis", "LeftCurly", "<Body>", "RightCurly"]]
c["<Else>"] = [["Else", "LeftCurly", "<Body>", "RightCurly"], []]

c["<Bool>"] = [['<RelExpr>'], ['True'], ['False']]
c["<RelExpr>"] = [['<Expr>', 'RelOp', '<Expr>'], ["<Expr>"]]

c["<Loop>"] = [['For', "LeftParenthesis", '<Y2>', "RightParenthesis", "LeftCurly", "<Body>", "RightCurly"]]
c["<Y2>"] = [['<Initialize>', 'SemiColon', '<RelExpr>', 'SemiColon', '<Operation>']]

c["<Print>"] = [["Print", "LeftParenthesis", "<Expr>", "RightParenthesis"]]
tok = open("lexemes.txt", "r").read()
tok = tok.split('\n')
tokArray = []

for i in range(len(tok)):
    x = tok[i][2:-2].split(r",")
    tokArray.append(x)
lexSeq = []
for t in tokArray:
    lexSeq.append(t[0])
print(lexSeq)
lexSeq.append("$")
inp = [lexSeq]  #

ans = []
for n in inp:
    s = ["$", "<Body>"]
    currentIndex = 0
    try:
        ans.append((n, validate(s, c, n, currentIndex)))
    except RecursionError:
        print("\nDepth Exceeded \n Invalid Code\nSyntax Error")

for a in ans:
    print(a)
