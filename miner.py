import argparse
from models import ExtremumModel
from datetime import time, datetime
import openpyxl

class Miner:
    def __init__(self, args):
        if args.e:
            self.model = ExtremumModel(args.s, args.w, args.t)
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
    parser.add_argument('-e', action='store_true')
    parser.add_argument('-s', type=lambda s: time.fromisoformat(s))
    parser.add_argument('-w', type=int)
    parser.add_argument('-t', type=float)
    parser.add_argument('-f', type=str)
    arguments = Arguments()
    parser.parse_args(args, namespace=arguments)
    return arguments