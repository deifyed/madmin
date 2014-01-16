import sys
sys.path.append('./src')

from os.path import realpath, dirname, join as pjoin
from colors import Color

CFG_PATH = 'config'

def parseLine(line):
    line = line.strip().split()

    return(line[0],line[2])

class Context():
    def __init__(self):
        self.attributes = {}

        for line in open(CFG_PATH, 'r'):
            key, value = parseLine(line)

            self.attributes[key] = eval(value)
