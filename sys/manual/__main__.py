from sys import argv
from os import listdir
if len(argv) < 2 or argv[1] in ['?','help']:
    print(f'''manual [command name]
-----
BASIC
- The `manual` command prints a
  description of commands. The
  manual is updated frequently.
TECHNICAL
- This command creates a subprocess
  which ./sys/manual directory and
  according to the command name,
  displays the output of a file with
  the same name.
-----
All pages: {", ".join([i.replace('.mnl','') for i in listdir("./sys/manual") if '.mnl' in i])}''')
    exit()
with open("./sys/manual/"+argv[1]+".mnl",'r') as file:
    print(file.read())
    file.close()