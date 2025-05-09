import os
from pathlib import Path


DATA_DIR: Path = Path("data")

DATA_FILE: Path = DATA_DIR / "healthcare_dataset.csv"

RESULTS_DIR: Path = Path("results")

COL_NAME: str             = "Name"
COL_AGE: str              = "Age"
COL_GENDER: str           = "Gender"
COL_BLOOD_TYPE: str       = "Blood Type"
COL_CONDITION: str        = "Medical Condition"
COL_ADMISSION_DATE: str   = "Date of Admission"
COL_DOCTOR: str           = "Doctor"
COL_HOSPITAL: str         = "Hospital"
COL_INSURANCE: str        = "Insurance Provider"
COL_BILLING: str          = "Billing Amount"
COL_ROOM: str             = "Room Number"
COL_ADMISSION_TYPE: str   = "Admission Type"
COL_DISCHARGE_DATE: str   = "Discharge Date"
COL_MEDICATION: str       = "Medication"
COL_TEST_RESULTS: str     = "Test Results"

DATE_FORMAT: str = "%Y-%m-%d"

BILLING_THRESHOLD: float = 5000.0

AGE_SENIOR: int = 65

DEFAULT_PLOT_BINS: int = 20

STATS_FILE_TEMPLATE: str = "{name}_stats.txt"
PLOT_FILE_TEMPLATE: str = "{name}_plot.png"
