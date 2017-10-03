import hashlib
import manipulate2 as manipulate
import sys
import time
import glob

def printSHA256(filename):
    with open(filename, "rb") as binfile:
        bytez = binfile.read()
    print(filename + ": " + hashlib.sha256(bytez).hexdigest())
    return bytez

def mutateAgain(pattern):
    for f in list(glob.glob(pattern)):
        bytez = printSHA256(f)
        mm = manipulate.MalwareManipulator(bytez)
        for act in actions:
            if act in f: #skip repeated action on same file
                continue
            func = getattr(mm,act)
            with open(f.replace(".exe","." + act + ".exe"), "wb") as binfile:
                binfile.write(func())
            printSHA256(f.replace(".exe","." + act + ".exe")) 

if(len(sys.argv) == 0):
    print("please provide a PE filename")

filename = sys.argv[1]
bytez = printSHA256(filename)
actions = ["break_optional_header_checksum",'overlay_append',\
           'section_rename','section_append']

mutateAgain(filename)
mutateAgain(filename.replace(".exe",".*.exe")) # 2 different actions per file
# mutateAgain(filename.replace(".exe",".*.*.exe")) # 3 different actions per file