from string import ascii_lowercase, digits
op_signs = ('+', '-', '*', '/', '>', '<', '=', '!')
parenthesis = ('(', ')')
alphabet = (*ascii_lowercase, '_')
whitespaces = (' ', '\t', '\n')

class Token():

    def __init__(self, t_value, t_type):
        self.value = t_value
        self.type = t_type

    def __repr__(self):
        return f'{self.value} <{self.type}>'

    def __str__(self):
        return f'{self.value} <{self.type}>'

def tokenize(s):
    tokens = []
    n = len(s)
    i = 0
    j = 0

    while True:
        if s[i] in whitespaces:
            i += 1
            continue

        if s[i] in alphabet:
            if s[i:i + 4] == 'rim(':
                j = i + 4
                while True:
                    if s[j] == ')':
                        j += 1
                        break

                    j += 1
                    if j > n - 1:
                        if s[n - 1] != ')':
                            return -1

                        break

                tokens.append(Token(s[i:j], 'fun'))
                i = j - 1
            else:
                j = i
                while True:
                    if s[j] in whitespaces or s[j] in op_signs or s[j] in parenthesis:
                        break

                    j += 1
                    if j > n - 1:
                        break

                tokens.append(Token(s[i:j], 'var'))
                i = j - 1
        elif s[i] in digits:
            j = i
            while True:
                if s[j] in whitespaces or s[j] in op_signs or s[j] in alphabet or s[j] in parenthesis:
                    break

                j += 1
                if j > n - 1:
                    break

            tokens.append(Token(s[i:j], 'num'))
            i = j - 1
        elif s[i] in op_signs:
            j = i
            while True:
                if s[j] in whitespaces or s[j] in alphabet or s[j] in digits or s[j] in parenthesis:
                    break

                j += 1
                if j > n - 1:
                    break

            tokens.append(Token(s[i:j], 'op'))
            i = j - 1
        elif s[i] in parenthesis:
            tokens.append(Token(s[i], 'par'))

        i += 1
        if i > n - 1:
            break

    return tokens
