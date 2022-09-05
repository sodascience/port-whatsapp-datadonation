from example import process
from pathlib import Path

import pandas as pd
from pandas.testing import assert_frame_equal

DATA_PATH = Path(__file__).parent / "data"

EXPECTED = [
    {'filename': 'hello/', 'compressed size': 0, 'size': 0},
    {'filename': 'hello/world.txt', 'compressed size': 267, 'size': 471}
]


def test_hello_world():
    df_expected = pd.DataFrame(EXPECTED)

    result = process(DATA_PATH.joinpath("hello.zip").open("rb"))
    assert len(result) == 1
    assert result[0]["id"] == 'overview'
    assert result[0]["title"] == 'The following files where read:'
    assert_frame_equal(result[0]["data_frame"], df_expected)
