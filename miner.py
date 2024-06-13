import argparse
from models import ExtremumModel
import datetime

class Miner:
    def __init__(self, args):
        if args.e:
            self.model = ExtremumModel()
        self.start_time = args.s
        self.window = args.w
        self.threshold = args.t
        self.filename = args.f

class Arguments:
    pass

def parse_arguments(args):
    parser = argparse.ArgumentParser(
        prog='mine', 
        description='calculate data based on 5 different models')
    parser.add_argument('-e', action='store_true')
    parser.add_argument('-s', type=lambda s: datetime.time.fromisoformat(s))
    parser.add_argument('-w', type=int)
    parser.add_argument('-t', type=float)
    parser.add_argument('-f', type=str)
    arguments = Arguments()
    parser.parse_args(args, namespace=arguments)
    return arguments