import os, subprocess
print("YANE-py\ntype \'prgm\\walk\' for available programs")
while True:
    i = input('% ').split(" ")
    if i[0] in ['exit','x','quit','q','leave','l']:
        exit() # exit is not a seperate program because it is high priority
    try:
        subprocess.run(f'python -B {" ".join(i)}')
    except Exception as err:
        print('Something went wrong!\n'+err)
        print(f'Program {i[0]} not found!')