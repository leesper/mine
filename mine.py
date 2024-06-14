import sys
from miner import parse_arguments, Miner
import openpyxl
from datetime import datetime

if __name__ == '__main__':
    arguments = parse_arguments(sys.argv[1:])
    miner = Miner(arguments)
    result_set = miner.calculate()
    result_book = openpyxl.Workbook()
    result_sheet = result_book.active
    result_sheet.append(['日期', '{}计算结果(1表示报警)'.format(miner.model.name())])
    for item in result_set:
        result_sheet.append([item[0], item[1]])
    result_book.save('result_{}.xlsx'.format(datetime.now().strftime('%Y%m%d_%H%M%S')))
