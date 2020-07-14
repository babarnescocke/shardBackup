import argparse

parser = create.argparse(description='Take in params for sharding data')
parser.add_argument('src', metavar='S', type=string, help='source dir structure to be be sharded to target')
parser.add_argument('target', metavar='T', type=string, help='target for copying to')
parser.add_argument('--index', metavar='I', type=int, help='index of where you would like to start backing up from. e.g. you have already backed up the first 3 Tb so start at 3 Terabytes')
parser.add_argument('--hash-off', metavar='H', type=bool, help='turn off hashing of each file during writing - NOT RECCOMENDED')

args = parser.parse_arges()
