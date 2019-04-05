from string import ascii_lowercase, digits
op_signs = ('+', '-', '*', '/', '>', '<', '=', '!')
alphabet = (*ascii_lowercase, '_')
whitespaces = (' ', '\t', '\n')

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

                tokens.append(s[i:j])
                i = j - 2
            else:
                j = i
                while True:
                    if s[j] in whitespaces or s[j] in op_signs:
                        break

                    j += 1
                    if j > n - 1:
                        break

                tokens.append(s[i:j])
                i = j - 1
        elif s[i] in digits:
            j = i
            while True:
                if s[j] in whitespaces or s[j] in op_signs or s[j] in alphabet:
                    break

                j += 1
                if j > n - 1:
                    break

            tokens.append(s[i:j])
            i = j - 1
        elif s[i] in op_signs:
            j = i
            while True:
                if s[j] in whitespaces or s[j] in alphabet or s[j] in digits:
                    break

                j += 1
                if j > n - 1:
                    break

            tokens.append(s[i:j])
            i = j - 1

        i += 1
        if i > n - 1:
            break

    return tokens

def tokenize_2(s):
    tokens = []
    token = ''
    n = len(s)
    i = 0
    while i < n:
        c = s[i]

        if c in whitespaces:
            token = ''
            continue
        
        if c in alphabet:
            if s[i + 1] == 'i' and s[i + 2] == 'm' and s[i + 3] == '(':
                # Token je funkcija rim(x)
                token += c
                while True:
                    i += 1
                    if i == n - 1:
                        token += s[i]
                        break
                    elif i > n - 1:
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
                    elif i > n - 1:
                        break

                    c = s[i]
                    if c in whitespaces or c in op_signs:
                        break
                    
                    token += c

                tokens.append(token)
                token = ''
        elif c in op_signs:
            
            pass
        elif c in digits:
            token += c
            while True:
                i += 1
                if i == n - 1:
                    token += s[i]
                    break
                elif i > n - 1:
                    break

                c = s[i]
                if c in whitespaces or c in op_signs or c in alphabet:
                    break
                
                token += c

            tokens.append(token)
            token = c
        
        i += 1

    return tokens
