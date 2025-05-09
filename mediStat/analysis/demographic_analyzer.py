# mediStat/analysis/demographic_analyzer.py

import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame

from mediStat.base_analyzer import BaseAnalyzer
from mediStat.structures import Queue
from mediStat.utils import save_to_txt, save_plot
from mediStat.constants import COL_AGE, COL_GENDER, DEFAULT_PLOT_BINS

class DemographicAnalyzer(BaseAnalyzer):
    """
        Analyzing demographic data.
    """

    def analyze(self) -> None:
        df: DataFrame = self.df.copy()

        gender_counts = df[COL_GENDER].value_counts().to_dict()

        age: Queue = Queue()
        for a in df[COL_AGE].astype(float):
            age.enqueue(a)
        age_list = list(age)

        total_count = len(age_list)
        mean_age = float(np.mean(age_list)) if total_count else 0.0
        median_age = float(np.median(age_list)) if total_count else 0.0

        gender_age_stats = {}
        grp = df.dropna(subset=[COL_AGE, COL_GENDER]).groupby(COL_GENDER)
        for gender, sub_df in grp:
            ages = sub_df[COL_AGE].astype(float).tolist()
            gender_age_stats[gender] = {
                "count": len(ages),
                "mean": float(np.mean(ages)) if ages else 0.0,
                "median": float(np.median(ages)) if ages else 0.0,
                "ages": ages
            }

        self.results = {
            "gender_counts": gender_counts,
            "age_list": age_list,
            "mean_age": mean_age,
            "median_age": median_age,
            "gender_age_stats": gender_age_stats
        }

    def export(self) -> None:
        name = "demographic"

        res = [
            f"Total Patients Analyzed : {len(self.results['age_list'])}",
            f"Overall Mean Age         : {self.results['mean_age']:.2f}",
            f"Overall Median Age       : {self.results['median_age']:.2f}",
            "",
            "Gender Distribution:"
        ]
        for gender, count in self.results["gender_counts"].items():
            res.append(f"  {gender}: {count}")
        res.append("")
        res.append("Age Stats by Gender:")
        for gender, stats in self.results["gender_age_stats"].items():
            res.append(
                f"  {gender} -> count: {stats['count']}, "
                f"mean: {stats['mean']:.2f}, median: {stats['median']:.2f}"
            )
        text = "\n".join(res)

        save_to_txt(name, text)
        print(text)

        # Gender distribution bar chart
        fig1, ax1 = plt.subplots()
        ax1.bar(
            list(self.results["gender_counts"].keys()),
            list(self.results["gender_counts"].values())
        )
        ax1.set_title("Gender Distribution")
        ax1.set_xlabel("Gender")
        ax1.set_ylabel("Count")
        save_plot(fig1, f"{name}_gender")

        # Overall age histogram
        fig2, ax2 = plt.subplots()
        ax2.hist(self.results["age_list"], bins=DEFAULT_PLOT_BINS)
        ax2.set_title("Age Distribution")
        ax2.set_xlabel("Age")
        ax2.set_ylabel("Frequency")
        save_plot(fig2, f"{name}_age_hist")

        # Age boxplot by gender
        fig3, ax3 = plt.subplots()
        data = [stats["ages"] for stats in self.results["gender_age_stats"].values()]
        labels = list(self.results["gender_age_stats"].keys())
        ax3.boxplot(data, labels=labels)
        ax3.set_title("Age by Gender")
        ax3.set_xlabel("Gender")
        ax3.set_ylabel("Age")
        save_plot(fig3, f"{name}_age_boxplot")
