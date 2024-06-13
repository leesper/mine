import datetime
from miner import parse_arguments, Miner
from models import ExtremumModel

class TestMiner:
    def test_should_use_extremum_model_when_e_specified(self):
        arguments = parse_arguments('-e')
        miner = Miner(arguments)
        assert isinstance(miner.model, ExtremumModel)
    def test_should_set_time_when_s_specified(self):
        arguments = parse_arguments('-s 23:59:59')
        miner = Miner(arguments)
        assert miner.start_time == datetime.time(23, 59, 59)
    def test_should_set_day_window_when_w_specified(self):
        arguments = parse_arguments('-w 5')
        miner = Miner(arguments)
        assert miner.window == 5
    def test_should_set_threshold_when_t_sepcified(self):
        arguments = parse_arguments('-t 0.5')
        miner = Miner(arguments)
        assert abs(miner.threshold - 0.5) < 0.001
    def test_should_set_input_file_when_f_specified(self):
        arguments = parse_arguments('-f data.xlsx')
        miner = Miner(arguments)
        assert miner.filename == 'data.xlsx'