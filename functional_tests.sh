#! /bin/bash

# -e 采用极值模型计算数据
# -s 设置每日起始时间点
# -w 设置日滑动窗口大小
# -t 设置阈值
python mine.py -e -s 23:59:59 -w 5 -t 0.5 ./data.xlsx