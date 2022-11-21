""" Test script for the whatsapp_chat script"""
from pathlib import Path
from typing import Tuple
import itertools

import pytest
import pandas as pd

from whatsapp_chat import process
from whatsapp_chat import anonymize_participants

DATA_PATH = Path(__file__).parent / "data"
FILES_TO_TEST = [p.name for p in DATA_PATH.glob("*_chat*.txt")]


EXPECTED = [
    {'username': 'person1', 'Aantal woorden': 21, 'Aantal websites': 1,
     'Aantal locaties': 1, 'Aantal foto’s en bestanden': 0, 'Aantal berichten': 3,
     'Datum eerste bericht': pd.to_datetime('2022-03-16 15:20:25'),
     'Datum laatste bericht': pd.to_datetime('2022-03-24 20:19:38'),
     'Op wie reageert u het meest?': 'person2',
     'Wie reageert het meest op u?': 'person2'},

    {'username': 'person2', 'Aantal woorden': 7, 'Aantal websites': 1,
     'Aantal locaties': 0, 'Aantal foto’s en bestanden': 0, 'Aantal berichten': 3,
     'Datum eerste bericht': pd.to_datetime('2022-03-16 15:25:38'),
     'Datum laatste bericht': pd.to_datetime('2022-03-26 18:52:15'),
     'Op wie reageert u het meest?': 'person1',
     'Wie reageert het meest op u?': 'person1'},

    {'username': 'person3', 'Aantal woorden': 1, 'Aantal websites': 0,
     'Aantal locaties': 0, 'Aantal foto’s en bestanden': 0, 'Aantal berichten': 1,
     'Datum eerste bericht': pd.to_datetime('2022-03-16 15:26:48'),
     'Datum laatste bericht': pd.to_datetime('2022-03-16 15:26:48'),
     'Op wie reageert u het meest?': 'person2',
     'Wie reageert het meest op u?': 'person2'},

    {'username': 'person4', 'Aantal woorden': 22, 'Aantal websites': 0,
     'Aantal locaties': 0, 'Aantal foto’s en bestanden': 0, 'Aantal berichten': 2,
     'Datum eerste bericht': pd.to_datetime('2020-07-14 22:05:54'),
     'Datum laatste bericht': pd.to_datetime('2022-03-20 20:08:51'),
     'Op wie reageert u het meest?': 'person1',
     'Wie reageert het meest op u?': 'person1'}
]


def process_data(filename: str, person_index: int) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Returns a tuple contaning the excepted output dataframe,
    and the dataframe from the process function
    """
    donor_user_name = "person2"

    df_expected = pd.DataFrame(EXPECTED)
    df_expected = anonymize_participants(df_expected, donor_user_name)
    df_expected['Aantal berichten'] = df_expected['Aantal berichten'].astype('int64')
    df_expected['Aantal websites'] = df_expected['Aantal websites'].astype('int32')
    df_expected['Aantal locaties'] = \
        df_expected['Aantal locaties'].astype('int32')
    df_expected['Aantal foto’s en bestanden'] = \
        df_expected['Aantal foto’s en bestanden'].astype('int32')

    results = []
    df_melt = pd.melt(df_expected, id_vars=["username"],
                      value_vars=["Aantal woorden",
                                  "Aantal berichten",
                                  "Datum eerste bericht",
                                  "Datum laatste bericht",
                                  "Aantal websites",
                                  "Aantal foto’s en bestanden",
                                  "Aantal locaties",
                                  "Op wie reageert u het meest?",
                                  "Wie reageert het meest op u?"],
                      var_name='Omschrijving', value_name='Gegevens')

    usernames = sorted(set(df_melt["username"]))
    usernames.insert(0, usernames.pop(usernames.index('u')))

    for user in usernames:
        df_user = df_melt[(df_melt["username"] == user) & df_melt["Gegevens"] != 0]
        results.append(df_user)

    expected_results = []
    for df_chat in results:
        user_name = pd.unique(df_chat["username"])[0]
        expected_results.append(
            {
                "id": user_name,  # "overview",
                "title": user_name,  # "The following data is extracted from the file:",
                "data_frame": df_chat[["Omschrijving", "Gegevens"]].reset_index(drop=True)
            }
        )

    file_to_test = DATA_PATH.joinpath(filename)
    flow = process()
    # start flow and handle first prompt
    file_prompt = flow.send(None)
    assert file_prompt["cmd"] == 'prompt'
    assert file_prompt["prompt"]["type"] == 'file'

    radio_prompt = flow.send(str(file_to_test))
    assert radio_prompt["cmd"] == 'prompt'
    assert radio_prompt["prompt"]["type"] == 'radio'

    result = flow.send(donor_user_name)

    return result["result"][person_index], expected_results[person_index]


# Generate test conditions
conditions = list(itertools.product(FILES_TO_TEST, range(4), range(7)))


@pytest.mark.parametrize("filename,person_index,condition_index", conditions)
def test_process(filename: str, person_index: int, condition_index: int):
    """
    Compares the expected dataframe with the output of the process function
    """

    df_result, expected_results = process_data(filename, person_index)
    df_expected_results = expected_results["data_frame"]
    df_result = expected_results["data_frame"]

    # check whether the condition can be tested
    try:
        description, expected_value =\
            tuple(df_expected_results[["Omschrijving", "Value"]].iloc[condition_index])
        description_result, value = tuple(df_result[["Omschrijving", "Gegevens"]].iloc[condition_index]) # pylint: disable=w0612

    except:  # pylint: disable=w0702

        return
    assert value == expected_value, f"In {filename} for person {person_index}," \
                                    f" test: {description} FAILED, {value} != {expected_value}"
