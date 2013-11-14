from os.path import realpath, dirname, join as pjoin

ROOT_PATH = dirname(realpath(__file__))
DATA_PATH = pjoin(ROOT_PATH, 'data')
DB_PATH = pjoin(DATA_PATH, 'maddb')
