import os,time,termcolor
osName = os.name
if osName == 'nt':
  print('detected nt')
  from pyreadline import Readline
  readline = Readline()
if osName == 'posix':
  print('detected posix')
  import readline
from os import system
from socket import gethostname
from getpass import getuser
readline.read_init_file('myreadline.rc')
def clr():
  if osName == 'posix':
    system('clear')
  if osName == 'nt':
    system('cls')


#ls command
def dols():
  if osName == 'nt':
    system('dir')
  if osName == 'posix':
    system('ls')


#def changePrompt(state):
#  global userPrompt,promptState
#  promptState = state
#  updatePrompt()
#  print(userPrompt)
userName    = getuser()
hostName    = gethostname()
userName    = getuser()
pnt         = print
inpt        = input
color       = termcolor.colored
green       = 'green'
yellow      = 'yellow'
blue        = 'blue'
red         = 'red'
promptState = 'termPy'
userPrompt  = "["+str(userName)+"@"+str(hostName)+"|("+str(promptState)+")"+"]$ "