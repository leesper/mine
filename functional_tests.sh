#! /bin/bash

# --ext 采用极值模型计算数据
# -w 设置日滑动窗口大小
# -t 设置阈值
# -f 设置excel数据文件
# python mine.py --ext -w 5 -t 0.5 -f ./data.xlsx

# --var 采用方差变异法计算数据
# -w 设置日滑动窗口大小
# -t 设置阈值
# -f 设置excel数据文件
# python mine.py --var -w 15 -t 0.35 -f ./data.xlsx

# --mov 采用移动均线爬坡法计算数据
# -w 设置日滑动窗口大小
# -t 设置阈值
python mine.py --mov -w 5 -t 0.001 -f ./data.xlsx