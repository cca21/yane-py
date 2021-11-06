import os, subprocess
print('''YANE-py
type \'help\' for help''')
# i hope to add an editor, probably start working on it when you work on the graphics mode
while True:
    inp = input("[ --- ] ").split(' ')
    if inp[0] in ['exit','x','quit','q','leave','l']:
        exit() # exit is not a seperate program because it is high priority
    elif inp[0] in os.listdir('./sys'):
        try:
            subprocess.run(f'python ./sys/{" ".join(inp)}')
        except Exception as err:
            print('Something went wrong!\n'+err)
    else: # make this less confusing
        print(f'Program {inp[0]} not found!')