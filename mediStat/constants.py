# mediStat/constants.py

import os
from pathlib import Path

# ─── Data Paths ────────────────────────────────────────────────────────────────
# Directory containing raw data
DATA_DIR: Path = Path("data")
# Full path to the healthcare dataset CSV
DATA_FILE: Path = DATA_DIR / "healthcare_dataset.csv"

# Directory where analysis outputs (stats files & plots) will be saved
RESULTS_DIR: Path = Path("results")

# ─── Column Names ─────────────────────────────────────────────────────────────
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

# ─── Date Formatting ──────────────────────────────────────────────────────────
# Format used in 'Date of Admission' and 'Discharge Date'
DATE_FORMAT: str = "%Y-%m-%d"

# ─── Thresholds & Domain Settings ─────────────────────────────────────────────
# Any billing amount above this is considered "high cost"
BILLING_THRESHOLD: float = 5_000.0

# Age threshold for defining senior patients
AGE_SENIOR: int = 65

# Default number of bins to use in histogram plots
DEFAULT_PLOT_BINS: int = 20

# ─── File Naming Templates ────────────────────────────────────────────────────
# Use .format(name="billing") → "billing_stats.txt"
STATS_FILE_TEMPLATE: str = "{name}_stats.txt"
# Use .format(name="billing") → "billing_plot.png"
PLOT_FILE_TEMPLATE: str = "{name}_plot.png"
