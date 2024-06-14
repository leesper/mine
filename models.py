from datetime import datetime, time, timedelta
import pandas as pd

class Model:
    def __init__(self, window, threshold):
        self.window = window
        self.threshold = threshold
    def name(self):
        raise NotImplemented
    def calculate(self, data_set):
        raise NotImplemented
    def _calculate_time_series(self, data_set):
        dates = [item[0] for item in data_set]
        values = [item[1] for item in data_set]
        series = pd.Series(values, index=dates)
        return series

class ExtremumModel(Model):
    def __init__(self, window, threshold):
        Model.__init__(self, window, threshold)
    def name(self):
        return '极值法'
    def calculate(self, data_set):
        series = self._calculate_time_series(data_set)

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
    
class VarianceModel(Model):
    def __init__(self, window, threshold):
        Model.__init__(self, window, threshold)
    def name(self):
        return "方差变异法"
    def calculate(self, data_set):
        series = self._calculate_time_series(data_set)
        daily_vars = series.resample('D').mean()\
            .rolling('{}D'.format(self.window)).var().dropna()
        daily_alarms = (daily_vars > self.threshold).astype(int)
        return [(date, value) for date, value in daily_alarms.items()]
    
class MovingAverageModel(Model):
    def __init__(self, window, threshold):
        Model.__init__(self, window, threshold)
    def name(self):
        return "移动均线爬坡法"
    def calculate(self, data_set):
        series = self._calculate_time_series(data_set)
        daily_means = series.resample('D').mean()\
            .rolling('{}D'.format(self.window)).mean()
        rolling_windows = daily_means.rolling('{}D'.format(self.window), closed='both')
        def calculate_alarm(window):
            if len(window) > 0:
                first_value = window.iloc[0]
                last_value = window.iloc[-1]
                return ((last_value - first_value) > self.threshold).astype(int)
            else:
                return None
        daily_alarms = rolling_windows.apply(calculate_alarm)
        return [(date, value) for date, value in daily_alarms.items()]