import os
import pandas as pd
import pytest

CSV_FILE = "data/reviews-per-country.csv"

def test_file_exists():
    assert os.path.exists(CSV_FILE) == True, "csv file does not exist"

def test_columns_exist():
    expected_columns = ['country','count','points']
    try:
        df = pd.read_csv(CSV_FILE)
        for col in expected_columns:
            assert col in df.columns
    except Exception as e:
        assert False, e

@pytest.mark.parametrize("country_name,expected_count,expected_points",
                        [['US', 54504, 88.6],
                        ['France', 22093, 88.8],
                        ['Italy', 19540, 88.6],
                        ['Spain', 6645, 87.3],
                        ['Israel', 505, 88.5],
                        ['Egypt',1,84.0]
                        ])
def test_values_exist(country_name, expected_count, expected_points):
    try:
        df = pd.read_csv(CSV_FILE)
        assert df.loc[df['country'] == country_name]['count'].iloc[0] == expected_count
        assert df.loc[df['country'] == country_name]['points'].iloc[0] == expected_points
    except Exception as e:
        assert False, e