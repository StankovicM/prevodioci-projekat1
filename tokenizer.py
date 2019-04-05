from string import ascii_lowercase, digits
operators = ('+', '-', '*', '/', '>', '<', '=', '!')
whitespaces = (' ', '\t', '\n')

token_types = ('num', 'op', 'var', 'par', 'fun')
current_token_type = None

def tokenize(s):
    tokens = []
    token = ''
    n = len(s)
    i = 0
    while i < n:
        c = s[i]

        if c in whitespaces:
            token = ''
            continue
        
        if c in ascii_lowercase:
            if s[i + 1] == 'i' and s[i + 2] == 'm' and s[i + 3] == '(':
                # Token je funkcija rim(x)
                token += c
                while True:
                    i += 1
                    if i == n - 1:
                        token += s[i]
                        break

                    c = s[i]
                    token += c
                    if c == ')':
                        break

                tokens.append(token)
                token = ''
            else:
                # Token je promenljiva
                token += c
                while True:
                    i += 1
                    if i == n - 1:
                        token += s[i]
                        break

                    c = s[i]
                    if c in whitespaces or c in operators:
                        break
                    
                    token += c

                tokens.append(token)
                token = ''
        elif c in operators:
            # token is an operator
            pass
        elif c in digits:
            token += c
            while True:
                i += 1
                if i == n - 1:
                    token += s[i]
                    break

                c = s[i]
                if c in whitespaces or c in operators or c in ascii_lowercase:
                    break
                
                token += c

            tokens.append(token)
            token = ''
        
        i += 1

    return tokens
