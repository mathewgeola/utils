import pandas as pd

import utils


def test_pandas():
    df = pd.DataFrame({"A": range(1, 101), "B": range(101, 201)})
    dfs = utils.pandas.split(df, num_parts=2)
    dfs = utils.pandas.split(df, part_size=50)
    for df in dfs:
        print(df)


if __name__ == '__main__':
    test_pandas()
