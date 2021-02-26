#!/usr/bin/env python3
from appmodules.shortcode import *
clr()

def updatePrompt():
  global userPrompt
  userPrompt = color("[",yellow)+color(str(userName),blue)+color("@",green)+color(str(hostName),blue)+color("|",yellow)+color("(",green)+color(promptState,blue)+color(")",green)+color("]",yellow)+color("$ ",red)
def changePrompt(state):
  global userPrompt,promptState
  promptState = state
  updatePrompt()

pnt(color('''terminalPy 1.0

Made by Robert Furr
Type 'about' for details
''',green))
changePrompt('termPy')
while True:
  try:
    if promptState is not 'termPy':
      changePrompt('termPy')
    cmd = inpt(str(userPrompt))
    if cmd == "help-old":
      pnt("pkg                command for installing and removing packages")
      pnt("ls                 show files")
      pnt("python             python")
      pnt("exit               exit terminal!")
      pnt("whoami             show user in terminal")
      pnt("version            show version of terminal")
      pnt("credits            show credits")
      pnt("txt                txt command for text files")
      pnt("zip                zip command for zip files(NOTE:not in function")
    elif cmd == "help":
      changePrompt('¿Help?')
      pnt('''What kind of help do you want?

termPy     Shows a list of termPy commands    
python     Runs Python help() function
pythonmod  Prompts for help on a particular Python function or module
man        Access a manpage of your choice
  ''')
      cmd1 = inpt(str(userPrompt))
      if cmd1 == "python":
        system("python3 -c 'help()'")
      elif cmd1 == "pythonmod":
        changePrompt('¿py?')
        pnt("Which Module?")
        cmd2 = inpt(str(userPrompt))
        pnt('Opening help for module '+str(cmd2)+"...")
        help(str(cmd2))
        pnt('Exited help')
      elif cmd1 == "man":
        pnt("What do you want to view the manpage for?")
    elif cmd == "clear":
      clr()
    elif cmd == "exit":
      break
    elif cmd == "pkg":
      pnt(color('Package Menu',green))
    elif cmd == "version":
      pnt("version of console is 1.0")
    elif cmd == "credits":
        pnt('''made by luksi :)
  Forked and improved by Robert Furr (https://github.com/robtech21)''')
    elif cmd == "whoami":
        pnt(str(userName))
    elif cmd == "py":
      pnt('Starting the interpreter...\nPress CTRL-D or type exit() to exit the Python Interpreter\n')
      system("python3")
    elif cmd == "pycmd":
      changePrompt('Python')
      pnt('Enter python command (single line only)')
      inpt(str(userPrompt))
    else:
      if str(cmd) == '':
        None
      else:
        pnt(str(cmd)+": Invalid command or no such command found")
  except EOFError as e:
    print(e)
    break

pnt('exited')
exit()
