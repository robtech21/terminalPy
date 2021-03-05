from appmodules.shortcode import *
clr()

def updatePrompt():
  global userPrompt
  userPrompt = color("[",yellow)+color(str(userName),blue)+color("@",green)+color(str(hostName),blue)+color("|",yellow)+color("(",green)+color(promptState,blue)+color(")",green)+color("]",yellow)+color("$ ",red)
def changePrompt(state):
  global userPrompt,promptState
  promptState = state
  updatePrompt()
exitMessage = color("Exited.",green)
pnt(color('''terminalPy 1.6

Made by Robert Furr
Type 'about' for details
''',green))
changePrompt('termPy')
while True:
  try:
    if promptState != 'termPy':
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

  termpy     Shows a list of termPy commands
  python     Runs Python help() function
  pythonmod  Prompts for help on a particular Python function or module
  ''')
      if osName == 'posix':
        print('  man        Access a manpage of your choice')
      cmd1 = inpt(str(userPrompt))
      if cmd1 == "python":
        system("python3 -c 'help()'")
      elif cmd1 == "termpy":
        print('''termPy Commands:
  help:               view this help screen
  clear, cls, clr:    clears the screen
  ls, dir:            views the contents of the directory
  exit, leave:        exits commandPy
  py:                 runs the Python interpreter
  oscmd:              allows you to run a command through "os.system()" 
  version:            display version info
  ''')
        
      elif cmd1 == "pythonmod":
        changePrompt('¿py?')
        pnt("Which Module?")
        cmd2 = inpt(str(userPrompt))
        pnt('Opening help for module '+str(cmd2)+"...")
        help(str(cmd2))
        pnt('Exited help')
      elif cmd1 == "man":
        pnt("What do you want to view the manpage for?")
    elif cmd == "cls":
      clr()
    elif cmd == "clr":
      clr()
    elif cmd == "clear":
      clr()
    elif cmd == "exit":
      break
    elif cmd == "leave":
      break
    elif cmd == "scram":
      exitMessage = color("Get outta here!",red)
      break
    elif cmd == "version":
      pnt("terminalPy version 1.6")
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
    elif cmd == "ls":
      dols()
    elif cmd == "dir":
        dols()
    elif cmd == "cls":
      clr()
    elif cmd == "oscmd":
      changePrompt("oscmd")
      cmd1 = inpt(str(userPrompt))
      system(str(cmd1))

    elif cmd == "pkg":
      changePrompt('pkg')
      pnt('''Options:
  pip: Install Python packages through pip''')
      if osName == 'posix':
        pnt('  os: Use the package manager of your native OS')
      if osName == 'nt':
        pnt(' scoop (not working yet): Use the scoop package manager for Windows (you need to have scoop installed for this to work)')
      cmd1 = inpt(str(userPrompt))
      if cmd1 == "pip":
        changePrompt('pkg/pip')
        pnt('Which package?')
        cmd2 = inpt(str(userPrompt))
        system('python -m pip install '+str(cmd2))
      if osName == 'nt' and cmd1 == 'scoop':
        changePrompt('pkg/scoop')
        pnt('Arguments? (anything that goes after "scoop")')
        cmd2 = inpt(str(userPrompt))
        system('powershell -Command scoop '+str(cmd2))
      if osName == 'nt' and cmd1 == 'os':
        changePrompt('pkg/os')
        pnt('''Which package manager do you have?
  apt: Package manager for Debian or Ubuntu Linux
  pacman: Package manager for Arch Linux
  dnf: Package manager for Fedora Linux
  ''')
        cmd2 = inpt(str(userPrompt))
        if cmd2 == 'apt':
          changePrompt('pkg/apt')
          pnt('Arguments?')
          cmd3 = inpt(str(userPrompt))
          system('sudo apt '+str(cmd3))
        if cmd2 == 'pacman':
          changePrompt('pkg/pacman')
          pnt('Arguments?')
          cmd3 = inpt(str(userPrompt))
          system('sudo pacman '+str(cmd3))
        if cmd2 == 'dnf':
          changePrompt('pkg/dnf')
          pnt('Arguments?')
          cmd3 = inpt(str(userPrompt))
          system('sudo dnf '+str(cmd3))
    else:
      if str(cmd) == '':
        None
      else:
        pnt(str(cmd)+": Invalid command or no such command found")
  except EOFError as e:
    pnt(e)
    break

pnt(str(exitMessage))
exit()
