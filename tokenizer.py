from string import ascii_lowercase, digits

op_signs = ('+', '-', '*', '/', '>', '<', '=', '!')
parenthesis = ('(', ')')
alphabet = (*ascii_lowercase, '_')
whitespaces = (' ', '\t', '\n')

# -------------------------------------------------------------------------
# Klasa token sadrzi sve potrebne informacije o tokenu
# -------------------------------------------------------------------------
class Token():

    def __init__(self, t_value, t_type, is_bool=False, bool_val=False):
        self.value = t_value
        self.type = t_type
        self.is_bool = is_bool
        self.bool_val = bool_val

    def __repr__(self):
        if self.is_bool:
            return f'{self.value} [{self.bool_val}] <{self.type}>'

        return f'{self.value} <{self.type}>'

    def __str__(self):
        if self.is_bool:
            return f'{self.value} [{self.bool_val}] <{self.type}>'
        
        return f'{self.value} <{self.type}>'

# -------------------------------------------------------------------------
# tokenize - parsira ulaz i pretvara ga u listu tokena
# -------------------------------------------------------------------------
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
    
# -------------------------------------------------------------------------
