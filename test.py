import string

running = True
ops = ['+', '-', '*', '/', '>', '<', '>=', '<=', '==', '!=']

# 0 = infix
# -1 = prefix
# 1 = postfix
state = 0

prompt_text = 'INFIX'

# Shell komande
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

# Funkcije za izracunavanje izraza
def eval_prefix(args):
    args.reverse()
    s = []
    for el in args:
        if el.isdigit():
            s.insert(0, int(el))
        else:
            if el == '+':
                s.insert(0, (s.pop(0) + s.pop(0)))
            elif el == '-':
                s.insert(0, (s.pop(0) - s.pop(0)))
            elif el == '*':
                s.insert(0, (s.pop(0) * s.pop(0)))
            elif el == '/':
                s.insert(0, (s.pop(0) / s.pop(0)))
            else:
                prompt(arrow=False, ln_end='\n', text='Invalid input.')
                return

    prompt(arrow=False, ln_end='\n', text=s[0])

def eval_infix(args):
    res = 0

    prompt(arrow=False, ln_end='\n', text=res)

def eval_postfix(args):
    s = []
    for el in args:
        if el.isdigit():
            s.insert(0, int(el))
        else:
            if el == '+':
                s.insert(0, (s.pop(0) + s.pop(0)))
            elif el == '-':
                s.insert(0, (s.pop(0) - s.pop(0)))
            elif el == '*':
                s.insert(0, (s.pop(0) * s.pop(0)))
            elif el == '/':
                s.insert(0, (s.pop(0) / s.pop(0)))
            else:
                prompt(arrow=False, ln_end='\n', text='Invalid input.')
                return

    prompt(arrow=False, ln_end='\n', text=s[0])
    

commands = {'exit': c_exit, 'prefix': c_prefix, 'infix': c_infix, 'postfix': c_postfix}
evals = {-1: eval_prefix, 0: eval_infix, 1:eval_postfix}

def prompt(arrow=True, ln_end='', text=None):
    if arrow:
        if text is not None:
            print(text, ' -> ', end=ln_end)
        else:
            print(prompt_text, ' -> ', end=ln_end)
    else:
        if text is not None:
            print(text, end=ln_end)
        else:
            print(prompt_text, end=ln_end)


def shell():

    while running:
        prompt()
        user_input_r = input()
        user_input = str(user_input_r).lower()
        if user_input in commands.keys():
            commands[user_input]()
        else:
            evals[state](user_input.split(' '))
            

    return

if __name__ == '__main__':
    shell()