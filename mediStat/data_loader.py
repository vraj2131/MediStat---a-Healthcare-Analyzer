import csv
from pathlib import Path
import pandas as pd

from mediStat.constants import (
    DATA_FILE,
    DATE_FORMAT,
    COL_ADMISSION_DATE,
    COL_DISCHARGE_DATE,
    COL_BILLING,
    COL_AGE,
)

class DataLoader:
    """
        Read the data from the csv file and convert to pandas dataframe
    """

    def __init__(self, file_path: Path = DATA_FILE):
        self.file_path = file_path

    def load_raw(self) -> list[dict]:
        with open(self.file_path, mode="r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            return [row for row in reader]

    def load_dataframe(self) -> pd.DataFrame:
        raw_rows = self.load_raw()
        df = pd.DataFrame(raw_rows)

        # Converting this columns to datetime
        if COL_ADMISSION_DATE in df.columns:
            df[COL_ADMISSION_DATE] = pd.to_datetime(
                df[COL_ADMISSION_DATE], format=DATE_FORMAT, errors="coerce"
            )
        if COL_DISCHARGE_DATE in df.columns:
            df[COL_DISCHARGE_DATE] = pd.to_datetime(
                df[COL_DISCHARGE_DATE], format=DATE_FORMAT, errors="coerce"
            )
        # Converting this columns to numeric
        if COL_BILLING in df.columns:
            df[COL_BILLING] = pd.to_numeric(df[COL_BILLING], errors="coerce")
        if COL_AGE in df.columns:
            df[COL_AGE] = pd.to_numeric(df[COL_AGE], errors="coerce", downcast="integer")

        return df
