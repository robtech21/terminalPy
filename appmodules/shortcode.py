#!/usr/bin/env python3
import os,time,termcolor,readline
from os import system
from socket import gethostname
from getpass import getuser
readline.read_init_file('myreadline.rc')
def clr():
  system('clear')

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