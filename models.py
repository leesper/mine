from datetime import datetime, time, timedelta
import pandas as pd

class ExtremumModel:
    def __init__(self, calculate_time, window, threshold):
        self.calculate_time = calculate_time
        self.window = window
        self.threshold = threshold
    def name(self):
        return '极值法'
    def calculate(self, data_set):
        dates = [item[0] for item in data_set]
        values = [item[1] for item in data_set]
        series = pd.Series(values, index=dates)

        day_averages = self.__get_window_average(series)
        max_minutes_averages = self.__get_10mins_average(series)
        daily_alarms = self.__get_alarms(day_averages, max_minutes_averages)

        return daily_alarms

    def __get_window_average(self, series):
        # 数据重采样到每天并计算均值
        daily_series = series.resample('D').mean()
        # 按天计算滑动窗口均值
        return daily_series.rolling(window='{}D'.format(self.window)).mean()

    def __get_10mins_average(self, series):
        ten_min_means = series.resample('10min').mean()
        daily_max_means = ten_min_means.resample('D').max()
        return daily_max_means
    
    def __get_alarms(self, day_means, min_means):
        difference = min_means - day_means
        alarms = (difference > self.threshold).astype(int)
        return [(date, value) for date, value in alarms.items()]