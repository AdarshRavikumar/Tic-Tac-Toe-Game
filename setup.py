import sys
from cx_Freeze import setup,Executable

setup(name='Game',version='0.1',description='2 Players',executables=[Executable('tictactoe_new.py')])
