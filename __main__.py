from tokenizer import tokenize
from evals import eval_prefix, eval_infix, eval_postfix

evals = {-1:eval_prefix, 0:eval_infix, 1:eval_postfix}

running = True
state = 0
debug = 1
prompt_text = 'INFIX'

# -------------------------------------------------------------------------
# c_exit - komanda za izlazak iz programa
# -------------------------------------------------------------------------
def c_exit():
    global running
    running = False

# -------------------------------------------------------------------------
# c_debug - komanda za prelazak u debug rezim rada
# -------------------------------------------------------------------------
def c_debug():
    global debug
    
    if debug == 1:
        debug = 0
    else:
        debug = 1

# -------------------------------------------------------------------------
# c_prefix - komanda za prelazak u prefiksni rezim rada
# -------------------------------------------------------------------------
def c_prefix():
    global prompt_text, state
    prompt_text = 'PREFIX'
    state = -1

# -------------------------------------------------------------------------
# c_infix - komanda za prelazak u infiksni rezim rada
# -------------------------------------------------------------------------
def c_infix():
    global prompt_text, state
    prompt_text = 'INFIX'
    state = 0

# -------------------------------------------------------------------------
# c_postfix - komanda za prelazak u postfiksni rezim rada
# -------------------------------------------------------------------------
def c_postfix():
    global prompt_text, state
    prompt_text = 'POSTFIX'
    state = 1

commands = {'prefix':c_prefix, 'infix':c_infix, 'postfix':c_postfix, 'exit':c_exit, 'debug':c_debug}

# -------------------------------------------------------------------------
# Glavna petlja programa, prihvata ulaz i poziva komande
# -------------------------------------------------------------------------
if __name__ == '__main__':
    while running:
        if debug == 1:
            print('[d]', prompt_text, '-->')
        else:
            print(prompt_text, '-->')
        s_raw = input()
        s = s_raw.lower().strip(' ')
        if s in commands.keys():
            commands[s]()
        else:
            expr = tokenize(s)
            if debug == 1:
                print('Tokenizovan izraz:', expr)
            
            print('Rezultat:', evals[state](expr))

# -------------------------------------------------------------------------
