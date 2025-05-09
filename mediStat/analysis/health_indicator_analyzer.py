import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
from sklearn.preprocessing import LabelEncoder

from mediStat.base_analyzer import BaseAnalyzer
from mediStat.structures import Stack
from mediStat.utils import save_to_txt, save_plot
from mediStat.constants import (
    COL_TEST_RESULTS,
    COL_CONDITION,
)

class HealthIndicatorAnalyzer(BaseAnalyzer):
    """
    Analyzing Health Indicators and test results
    """

    def analyze(self) -> None:
        df: DataFrame = self.df.copy()

        target = df[COL_TEST_RESULTS]
        # Using Sklearn's Label Encoder
        le = LabelEncoder()
        codes = le.fit_transform(target)
        df["target"] = codes
        mapping = {cls: int(code) for cls, code in zip(le.classes_, le.transform(le.classes_))}
        categories = list(le.classes_)

        code_stk = Stack()
        for code in codes:
            code_stk.push(int(code))
        codes_list = list(code_stk)

        code_counts = {cls: codes_list.count(code) for cls, code in mapping.items()}

        condition_cat_counts = {}
        condition_means = {}
        grouped = df.dropna(subset=[COL_CONDITION]).groupby(COL_CONDITION)["target"]
        for condition, grp in grouped:
            condition_stk = Stack()
            for i in grp.astype(int):
                condition_stk.push(i)
            grp_list = list(condition_stk)

            counts = {cls: grp_list.count(code) for cls, code in mapping.items()}
            condition_cat_counts[condition] = counts

            condition_means[condition] = float(np.mean(grp_list)) if grp_list else 0.0


        self.results = {
            "mapping": mapping,
            "categories": categories,
            "codes_list": codes_list,
            "code_counts": code_counts,
            "condition_cat_counts": condition_cat_counts,
            "condition_means": condition_means,
        }

    def export(self) -> None:
        name = "health_indicator"

        res = ["LabelEncoder mapping:"]
        for cls, code in self.results["mapping"].items():
            res.append(f"  {cls}: {code}")
        res.append("\nOverall Counts:")
        for cls, cnt in self.results["code_counts"].items():
            res.append(f"  {cls}: {cnt}")
        res.append("\nCounts & Mean by Medical Condition:")
        for condition, counts in self.results["condition_cat_counts"].items():
            res.append(f"{condition}:")
            for cls, cnt in counts.items():
                res.append(f"  {cls}: {cnt}")
            res.append(f"  Mean encoded value: {self.results['condition_means'][condition]:.2f}")
            res.append("")
        text = "\n".join(res).strip()

        print(text)
        save_to_txt(name, text)

        # Histogram of encoded test results
        fig1, ax1 = plt.subplots()
        ax1.hist(self.results["codes_list"], bins=range(len(self.results["categories"]) + 1), edgecolor="black")
        ax1.set_xticks(range(len(self.results["categories"])))
        ax1.set_xticklabels(self.results["categories"], rotation=45, ha="right")
        ax1.set_title("Encoded Test Results Distribution")
        ax1.set_xlabel("Category")
        ax1.set_ylabel("Frequency")
        save_plot(fig1, f"{name}_hist")

        # Bar chart of mean encoded by condition
        fig2, ax2 = plt.subplots()
        conditions = list(self.results["condition_means"].keys())
        means = [self.results["condition_means"][c] for c in conditions]
        ax2.bar(conditions, means, edgecolor="black")
        ax2.set_title("Mean Encoded Test Result by Condition")
        ax2.set_xlabel("Condition")
        ax2.set_ylabel("Mean Encoded Value")
        plt.xticks(rotation=45, ha="right")
        save_plot(fig2, f"{name}_by_condition")

