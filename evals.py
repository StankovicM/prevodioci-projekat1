from tokenizer import Token
from utils import rim
import __main__

operators = ('+', '-', '*', '/', '=', '<', '<=', '>', '>=', '==', '!=')
operators_test = ('+', '-', '*', '/')
variables = {}

# -------------------------------------------------------------------------
# "Evaluacija" prefiksnog izraza
# -------------------------------------------------------------------------
def eval_prefix(expr):
    # TODO pretvoriti prefiksni izraz u postfiksni
    pass

# -------------------------------------------------------------------------
# "Evaluacija" infiksnog izraza
# -------------------------------------------------------------------------
def eval_infix(expr):
    return eval_postfix(__infix_to_postfix(expr))    

# -------------------------------------------------------------------------
# Evaluacija postfiksnog izraza
# -------------------------------------------------------------------------
# applyOp - primenjuje zadatau operaciju na dva prosledjena argumenta
# -------------------------------------------------------------------------
def applyOp(t1, t2, op):
    if t1.type == 'var' and op != '=':
        val1 = variables[t1.value]
    
    if t2.type == 'var':
        try:
            val2 = variables[t2.value]
        except KeyError:
            print(f'Promenljiva {t2.value} ne postoji.')
            return None

    if t1.type == 'fun':
        val1 = rim(t1.value[4:-1])

    if t2.type == 'fun':
        val2 = rim(t2.value[4:-1])

    if t1.type == 'num':
        val1 = int(t1.value)

    if t2.type == 'num':
        val2 = int(t2.value)

    if op == '+':
        return Token(val1 + val2, 'num')

    if op == '-':
        return Token(val1 - val2, 'num')

    if op == '*':
        return Token(val1 * val2, 'num')
        
    if op == '/':
        return Token(val1 // val2, 'num')

    if op == '=':
        variables[t1.value] = int(val2)
        return Token(variables[t1.value], 'num')

    if op == '<':
        res = False
        t_new = Token(val2, 'num', is_bool=True)
        if val1 < val2:
            if t1.is_bool:
                res = t1.bool_val
            else:
                res = True

        t_new.bool_val = res
        return t_new

    if op == '<=':
        res = False
        t_new = Token(val2, 'num', is_bool=True)
        if val1 <= val2:
            if t1.is_bool:
                res = t1.bool_val
            else:
                res = True

        t_new.bool_val = res
        return t_new

    if op == '>':
        res = False
        t_new = Token(val2, 'num', is_bool=True)
        if val1 > val2:
            if t1.is_bool:
                res = t1.bool_val
            else:
                res = True

        t_new.bool_val = res
        return t_new

    if op == '>=':
        res = False
        t_new = Token(val2, 'num', is_bool=True)
        if val1 >= val2:
            if t1.is_bool:
                res = t1.bool_val
            else:
                res = True

        t_new.bool_val = res
        return t_new
    
    if op == '==':
        res = False
        t_new = Token(val2, 'num', is_bool=True)
        if val1 == val2:
            if t1.is_bool:
                res = t1.bool_val
            else:
                res = True

        t_new.bool_val = res
        return t_new

    if op == '!=':
        res = False
        t_new = Token(val2, 'num', is_bool=True)
        if val1 != val2:
            if t1.is_bool:
                res = t1.bool_val
            else:
                res = True

        t_new.bool_val = res
        return t_new

# -------------------------------------------------------------------------
# eval_postfiks - proverava da li postoji odgovarajuci broj tokena, a zatim
#                 vrsi evaluaciju izraza koriscenjem funkcije applyOp
# -------------------------------------------------------------------------
def eval_postfix(expr):
    ce = check_expr(expr)
    if ce[0] == -1:
        return -1
    elif ce[0] == 0:
        return ce[1]
    
    if __main__.debug == 1:
        print('Postfiksni izraz:', expr)

    s = []

    for token in expr:
        if isid(token):
            s.insert(0, token)
        else:
            try:
                val2 = s.pop(0)
                val1 = s.pop(0)
                val = applyOp(val1, val2, token.value)
                if val is None:
                    return -1
                else:
                    s.insert(0, val)
            except IndexError:
                print('Nevalidan izraz.')
                return -1

    return s[0]

# -------------------------------------------------------------------------
# Konverezija infiksnog izraza u postfiksni
# -------------------------------------------------------------------------
# isid - proverava da li je token neki od sledecih identifikatora:
#        broj, funkcija ili promenljiva 
# -------------------------------------------------------------------------
def isid(token):
    if token.type in ('num', 'fun', 'var'):
        return True
    
    return False

# -------------------------------------------------------------------------
# precedence - vraca prioritet racunskih operacija i zagrada, pri cemu 
#              mnozenje i deljenje imaju najvisi, a zagrade najnizi
#              prioritet
# -------------------------------------------------------------------------
def precedence(token):
    if token.value in '+-':
        return 1
    elif token.value in '*/':
        return 2
    
    return 0

# -------------------------------------------------------------------------
# __infix_to_postfix - vrsi konverziju infiksnog izraza u postfiksni
#                      i vraca novu listu tokena u
# -------------------------------------------------------------------------
def __infix_to_postfix(expr):
    postfix = []
    opstack = []
    
    for token in expr:
        if isid(token):
            postfix.append(token)
        elif token.value == '(':
            opstack.append(token)
        elif token.value == ')':
            temp = opstack.pop()
            while temp.value != '(':
                postfix.append(temp)
                temp = opstack.pop()
        else: 
            while (len(opstack) > 0) and (precedence(opstack[-1]) >= precedence(token)): # and isid(token):
                postfix.append(opstack.pop())
                
            opstack.append(token)
                
    while len(opstack) > 0:
        postfix.append(opstack.pop())
            
    return postfix

# -------------------------------------------------------------------------
# Provera ipsravnosti argumenata
# -------------------------------------------------------------------------
def check_expr(expr):
    if len(expr) in (0, 2):
        print('Nevalidan izraz.')
        return -1, None
    
    if len(expr) == 1:
        t = expr[0]
        if t.type == 'num':
            return 0, int(t.value)
        elif t.type == 'var':
            try:
                val = variables[t.value]
                return 0, val
            except KeyError:
                return 0, 'Promenljiva ne postoji.'
        elif t.type == 'fun':
            val = rim(t.value[4:-1])
            return 0, val
        else:
            return -1, None

    return 1, None

# -------------------------------------------------------------------------d
