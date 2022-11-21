""" Test script for the whatsapp_account_info script"""
from pathlib import Path
import pytest
import itertools
from typing import Tuple
import pandas as pd

from whatsapp_chat import process
from whatsapp_chat import anonymize_participants

from pandas.testing import assert_frame_equal


DATA_PATH = Path(__file__).parent / "data"
FILES_TO_TEST = [ p.name for p in DATA_PATH.glob("*_chat*.txt")]

EXPECTED = [
    {'username': 'person1', 'Total number of words': 20, 'Number of URLs': 1,
     'Number of shared locations': 1, 'file_no': 0, 'Number of messages': 3,
     'Date first message': pd.to_datetime('2022-03-16 15:20:25'),
     'Date last message': pd.to_datetime('2022-03-24 20:19:38'),
     'Who do you most often reply to?': 'person2',
     'Who replies to you the most often?': 'person2'},

    {'username': 'person2', 'Total number of words': 7, 'Number of URLs': 1,
     'Number of shared locations': 0, 'file_no': 0, 'Number of messages': 3,
     'Date first message': pd.to_datetime('2022-03-16 15:25:38'),
     'Date last message': pd.to_datetime('2022-03-26 18:52:15'),
     'Who do you most often reply to?': 'person1',
     'Who replies to you the most often?': 'person1'},

    {'username': 'person3', 'Total number of words': 1, 'Number of URLs': 0,
     'Number of shared locations': 0, 'file_no': 0, 'Number of messages': 1,
     'Date first message': pd.to_datetime('2022-03-16 15:26:48'),
     'Date last message': pd.to_datetime('2022-03-16 15:26:48'),
     'Who do you most often reply to?': 'person2',
     'Who replies to you the most often?': 'person2'},

    {'username': 'person4', 'Total number of words': 21, 'Number of URLs': 0,
     'Number of shared locations': 0, 'file_no': 0, 'Number of messages': 2,
     'Date first message': pd.to_datetime('2020-07-14 22:05:54'),
     'Date last message': pd.to_datetime('2022-03-20 20:08:51'),
     'Who do you most often reply to?': 'person1',
     'Who replies to you the most often?': 'person1'}
]



def process_data(filename: str, person_index: int) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """ 
    Returns a tuple contaning the excepted output dataframe, 
    and the dataframe from the process function
    """

    df_expected = pd.DataFrame(EXPECTED)
    df_expected = anonymize_participants(df_expected)
    df_expected['Number of messages'] = df_expected['Number of messages'].astype('int64')
    df_expected['Number of URLs'] = df_expected['Number of URLs'].astype('int32')
    df_expected['Number of shared locations'] = \
        df_expected['Number of shared locations'].astype('int32')
    df_expected['file_no'] = df_expected['file_no'].astype('int32')

    results = []
    df_melt = pd.melt(df_expected, id_vars=["username"],
                      value_vars=["Total number of words",
                                  "Number of messages",
                                  "Date first message",
                                  "Date last message",
                                  "Number of URLs",
                                  "file_no",
                                  "Number of shared locations",
                                  "Who replies to you the most often?",
                                  "Who do you most often reply to?"],
                      var_name='Description', value_name='Value')

    usernames = df_melt["username"].unique()
    for user in usernames:
        df_user = df_melt[(df_melt["username"] == user) & df_melt["Value"] != 0]
        results.append(df_user)

    expected_results = []
    for df_chat in results:
        user_name = pd.unique(df_chat["username"])[0]
        expected_results.append(
            {
                "id": user_name,  # "overview",
                "title": user_name,  # "The following data is extracted from the file:",
                "data_frame": df_chat[["Description", "Value"]].reset_index(drop=True)
            }
        )

    file_to_test = DATA_PATH.joinpath(filename)
    df_result = process(file_to_test)

    return df_result[person_index], expected_results[person_index]


# Generate test conditions
conditions = list(itertools.product(FILES_TO_TEST, range(4), range(7)))

@pytest.mark.parametrize("filename,person_index,condition_index", conditions)
def test_process(filename: str, person_index: int, condition_index: int):
    """ 
    Compares the expected dataframe with the output of the process function
    """

    df_result, expected_results =  process_data(filename, person_index)
    df_expected_results = expected_results["data_frame"]
    df_result = expected_results["data_frame"]

    # check whether the condition can be tested
    try:
        description, expected_value = tuple(df_expected_results[["Description", "Value"]].iloc[condition_index])
        description_result, value = tuple(df_result[["Description", "Value"]].iloc[condition_index])
    except:

        return
    assert value == expected_value, f"In {filename} for person {person_index}, test: {description} FAILED, {value} != {expected_value}"



