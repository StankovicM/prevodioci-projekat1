from tokenizer import tokenize
from evals import eval_prefix, eval_infix, eval_postfix, eval_infix2

evals = {-1:eval_prefix, 0:eval_infix2, 1:eval_postfix}

running = True
state = 0
prompt_text = 'INFIX'

def c_exit():
    global running
    running = False

def c_prefix():
    global prompt_text, state
    prompt_text = 'PREFIX'
    state = -1

def c_infix():
    global prompt_text, state
    prompt_text = 'INFIX'
    state = 0

def c_postfix():
    global prompt_text, state
    prompt_text = 'POSTFIX'
    state = 1

commands = {'prefix':c_prefix, 'infix':c_infix, 'postfix':c_postfix, 'exit':c_exit}

if __name__ == '__main__':
    while running:
        print(prompt_text, '-->')
        s_raw = input()
        s = s_raw.lower().strip(' ')
        if s in commands.keys():
            commands[s]()
        else:
            expr = tokenize(s)
            print('Tokenizovan izraz:', expr)
            print('Rezultat:', evals[state](expr))
