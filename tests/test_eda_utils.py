import pytest
from model_dev import eda_utils


def test_count_values():
    df = eda_utils.load_data('model_dev/raw/train.csv')
    count_gender = eda_utils.count_values(df, 'Gender')
    count_response = eda_utils.count_values(df, 'Response')
    # print(count_gender[count_gender['Gender']=='Female']['count'])
    assert count_gender[count_gender['Gender']=='Female']['count'].item() == 175020

test_count_values()

