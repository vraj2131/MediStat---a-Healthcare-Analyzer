import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame

from mediStat.base_analyzer import BaseAnalyzer
from mediStat.structures import Queue
from mediStat.utils import save_to_txt, save_plot
from mediStat.constants import (
    COL_ADMISSION_DATE,
    COL_DISCHARGE_DATE,
    COL_ADMISSION_TYPE,
)

class AdmissionAnalyzer(BaseAnalyzer):
    """
        Analysis of admission data of the patients
    """

    def analyze(self) -> None:
        df: DataFrame = self.df.copy()
        
        df["LengthOfStay"] = (
            df[COL_DISCHARGE_DATE] - df[COL_ADMISSION_DATE]
        ).dt.days

        los: Queue = Queue()
        for l in df["LengthOfStay"].astype(int):
            los.enqueue(l)

        los_list = list(los)

        type_counts = df[COL_ADMISSION_TYPE].value_counts().to_dict()

        mean_los = float(np.mean(los_list)) if los_list else 0.0
        median_los = float(np.median(los_list)) if los_list else 0.0

        self.results = {
            "type_counts": type_counts,
            "mean_los": mean_los,
            "median_los": median_los,
            "los_list": los_list,
        }

    def export(self) -> None:
        name = "admission"

        res = ["Admission Type Counts:"]
        for admission_type, count in self.results["type_counts"].items():
            res.append(f"  {admission_type}: {count}")
        res.append("")
        res.append(f"Length of Stay (days):")
        res.append(f"  Mean  : {self.results['mean_los']:.2f}")
        res.append(f"  Median: {self.results['median_los']:.2f}")
        text = "\n".join(res)

        save_to_txt(name, text)
        print(text)  

        # Admission type bar chart
        fig1, ax1 = plt.subplots()
        ax1.bar(
            list(self.results["type_counts"].keys()),
            list(self.results["type_counts"].values()),
        )
        ax1.set_title("Admission Type Counts")
        ax1.set_ylabel("Count")
        ax1.set_xlabel("Admission Type")
        plt.xticks(rotation=45, ha="right")
        save_plot(fig1, name + "_types")

        # Length Of Stay histogram
        fig2, ax2 = plt.subplots()
        ax2.hist(self.results["los_list"], bins=20)
        ax2.set_title("Length of Stay Distribution")
        ax2.set_xlabel("Days")
        ax2.set_ylabel("Frequency")
        save_plot(fig2, name + "_los")
