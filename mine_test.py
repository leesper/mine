import argparse
from miner import parse_arguments, Miner
from models import ExtremumModel

def test_should_use_extremum_model_when_e_specified():
    arguments = parse_arguments()
    miner = Miner(arguments)
    assert isinstance(miner.model, ExtremumModel)
    

