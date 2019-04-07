from tokenizer import Token
from utils import rim

operators = ('+', '-', '*', '/', '=', '<', '<=', '>', '>=', '==', '!=')
operators_test = ('+', '-', '*', '/')
variables = {}

def eval_prefix(expr):
    pass

# -------------------------------------------------------------------------
# Evaluacija infiksnog izraza
# -------------------------------------------------------------------------
def priority(op):
    if op in '+-':
        return 1
    elif op in '*/':
        return 2

    return 0

def calc(val1, val2, op):
    if op == '+': return val1 + val2
    if op == '-': return val1 - val2
    if op == '*': return val1 * val2
    if op == '/': return val1 // val2

def eval_infix(expr):
    if len(expr) < 3:
        # Nedovoljan broj operanada i operatora u izrazu
        return -1

    expr.reverse()
    num_stk, ops_stk = [], []

    while len(expr) > 0:
        t = expr.pop()

        if t.value == '(':
            ops_stk.append(t.value)
        elif t.type == 'num':
            num_stk.append(int(t.value))
        elif t.value == ')':
            while len(ops_stk) != 0 and ops_stk[-1] != '(':
                val2 = num_stk.pop()
                val1 = num_stk.pop()
                op = ops_stk.pop()
                num_stk.append(calc(val1, val2, op))

            ops_stk.pop()
        elif t.type == 'op':
            if t.value in operators_test:
                # TODO: Promeniti na operators
                while len(ops_stk) != 0 and priority(ops_stk[-1]) >= priority(t.value):
                    val2 = num_stk.pop() 
                    val1 = num_stk.pop() 
                    op = ops_stk.pop() 
                  
                    num_stk.append(calc(val1, val2, op))
            else:
                # Ne postojeci operator
                return -1
        elif t.type == 'var':
            var_name = t.value
            if expr[-1].value == '=':
                expr.pop()
                if expr[-1].type == 'num':
                    variables[var_name] = int(expr.pop().value)
                    num_stk.append(variables[var_name])
                else:
                    # Nepravilno upotrebljena promenljiva
                    return -1
            else:
                num_stk.append(variables[var_name])
        else:
            # Ne postojeci token, ignorisati za sad
            # TODO: omoguciti sve tipove tokena
            continue
    
    while len(ops_stk) != 0: 
          
        val2 = num_stk.pop() 
        val1 = num_stk.pop() 
        op = ops_stk.pop() 
                  
        num_stk.append(calc(val1, val2, op)) 
    
    if len(num_stk) == 0:
        return 0
    elif len(num_stk) == 1:
        return num_stk[0]
    else:
        return -1

def eval_infix2(expr):
    return eval_postfix(__infix_to_postfix(expr))

    if len(expr) < 3:
        print('Izraz nema dovoljan broj operanada i operatora.')
        return -1

    expr.reverse()

    var_name = ''
    var_val = 0
    var_assing = False

    bool_val = False
    is_bool = False

    vals, ops = [], []

    while len(expr) > 0:
        token = expr.pop()

        if token.type == 'num':
            vals.append(int(token.value))
            continue
        elif token.type == 'op':
            if not token.value in operators:
                print(f'Operator {token.value} ne postoji.')
                return -1
            
            if token.value in operators[:4]:
                pass
            elif token.value in operators[5:]:
                pass
            else:
                pass
        elif token.type == 'var':
            pass
        elif token.type == 'fun':
            pass
        elif token.type == 'par':
            if token.value == '(':
                ops.append(token.value)
            else:
                pass
        else:
            print(f'Neipravan token {token}.')
            return -1

    if is_bool: 
        return bool_val
    else:
        return vals[-1]

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
        return val1 + val2
    if op == '-':
        return val1 - val2
    if op == '*':
        return val1 * val2
    if op == '/':
        return val1 // val2
    if op == '=':
        variables[t1.value] = int(val2)
        return variables[t1.value]
    

def eval_postfix(expr):
    ce = check_expr(expr)
    if ce[0] == -1:
        return -1
    elif ce[0] == 0:
        return ce[1]
    
    print('Postfiksni izraz:', expr)
    s = []

    for token in expr:
        if isid(token):
            s.insert(0, token)
        else:
            val2 = s.pop(0)
            val1 = s.pop(0)
            val = applyOp(val1, val2, token.value)
            if val is None:
                return -1
            else:
                s.insert(0, Token(val, 'num'))

    return s[0]

# -------------------------------------------------------------------------
# Konverezija infiksnog izraza u postfiksni
# -------------------------------------------------------------------------
def isid(token):
    if token.type in ('num', 'fun', 'var'):
        return True
    
    return False

def precedence(token):
    if token.value in '+-':
        return 1
    elif token.value in '*/':
        return 2
    
    return 0

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
