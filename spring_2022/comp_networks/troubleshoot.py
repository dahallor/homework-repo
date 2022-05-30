import pdb
import subprocess

var1 = "hello there"
var2 = "general kenobi"
print(var1)

def print_resp(var2):
    print(var2)

subprocess.Popen('print_resp(var2)', shell=True)

