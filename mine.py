import sys
from miner import parse_arguments, Miner

if __name__ == '__main__':
    arguments = parse_arguments(sys.argv[1:])
    miner = Miner(arguments)
    print(miner.model)
    print(miner.start_time)