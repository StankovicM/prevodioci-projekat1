from tokenizer import tokenize

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
            print(tokenize(s))