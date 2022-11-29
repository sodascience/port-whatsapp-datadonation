""" Test script for the whatsapp_account_info script"""

from pathlib import Path
import pandas as pd
from pandas.testing import assert_frame_equal

import pytest

from whatsapp_account_info import process


DATA_PATH = Path(__file__).parent / "data/account_info"
FILES_TO_TEST = [p.name for p in DATA_PATH.glob("*.zip")]


EXPECTED = [
    {'Aantal groepen': 4,
     'Aantal contacten': 3
     }
]


@pytest.mark.parametrize("filename_to_test", FILES_TO_TEST)
def test_process(filename_to_test):
    """ Test process function.
        compares the expected dataframe with the output of the process function
        to check if all the columns are matched.
        Raises
        -------
        AssertionError: When provided expected dataframe could not match the participants dataframe
        """
    df_expected = pd.DataFrame(EXPECTED)
    file_to_test = DATA_PATH.joinpath(filename_to_test)

    flow = process()

    file_prompt = flow.send(None)
    assert file_prompt["cmd"] == 'prompt'
    assert file_prompt["prompt"]["type"] == 'file'

    file_prompt = flow.send(str(file_to_test))
    assert_frame_equal(file_prompt["result"][0]['data_frame'], df_expected)
