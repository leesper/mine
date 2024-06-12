import argparse
from models import ExtremumModel

class Miner:
    def __init__(self, args):
        self.model = ExtremumModel()

class Arguments:
    pass

def parse_arguments():
    parser = argparse.ArgumentParser(
        prog='mine', 
        description='calculate data based on 5 different models')
    parser.add_argument('-e', action='store_true')
    arguments = Arguments()
    parser.parse_args(namespace=arguments)
    return arguments