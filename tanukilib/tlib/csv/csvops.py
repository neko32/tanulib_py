import pandas as pd


class CSVOps:
    """Provide CSV Ops through Pandas DataFrame"""

    def __init__(self, csv_file: str, row_key: str):
        self.csv_file = csv_file
        self.db = pd.read_csv(csv_file)
        self.db.set_index(row_key, inplace=True)

    def get_row_by_row_key(self, row_key: str):
        """Get row by row key index"""
        return self.db.loc[row_key]
