import argparse
from models import ExtremumModel, VarianceModel, MovingAverageModel, StaLtaModel
from datetime import datetime
import openpyxl

class Miner:
    def __init__(self, args):
        if args.ext:
            self.model = ExtremumModel(args.w, args.t)
        elif args.var:
            self.model = VarianceModel(args.w, args.t)
        elif args.mov:
            self.model = MovingAverageModel(args.w, args.t)
        elif args.sta:
            self.model = StaLtaModel(args.w, args.t)
        self.filename = args.f
    def calculate(self):
        data_sheet = openpyxl.load_workbook(self.filename).worksheets[0]
        data_set = [(datetime.fromisoformat(cells[0].value), cells[1].value) for cells in list(data_sheet.rows)[1:]]
        data_set.sort(key=lambda e: e[0])
        daily_alarms = self.model.calculate(data_set)
        return daily_alarms


class Arguments:
    pass

def parse_arguments(args):
    parser = argparse.ArgumentParser(
        prog='mine', 
        description='calculate data based on 5 different models')
    parser.add_argument('--ext', action='store_true')
    parser.add_argument('--var', action='store_true')
    parser.add_argument('--mov', action='store_true')
    parser.add_argument('--sta', action='store_true')
    parser.add_argument('-w', type=int)
    parser.add_argument('-t', type=float)
    parser.add_argument('-f', type=str)
    arguments = Arguments()
    parser.parse_args(args, namespace=arguments)
    return arguments