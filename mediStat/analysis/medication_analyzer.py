import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame

from mediStat.base_analyzer import BaseAnalyzer
from mediStat.structures import Queue
from mediStat.utils import save_to_txt, save_plot
from mediStat.constants import (
    COL_MEDICATION,
    COL_CONDITION,
    COL_BILLING,
)

class MedicationAnalyzer(BaseAnalyzer):
    """
        Analyzing for medication data
    """

    def analyze(self) -> None:
        df: DataFrame = self.df.copy()

        meds = df[COL_MEDICATION]
        med_q = Queue()
        for med in meds:
            med_q.enqueue(med)
        med_list = list(med_q)

        med_counts = {med: med_list.count(med) for med in set(med_list)}

        billing_stats = {}
        if COL_BILLING in df.columns:
            grp = df.dropna(subset=[COL_BILLING]).groupby(COL_MEDICATION)[COL_BILLING]
            for med, vals in grp:
                arr = vals.astype(float).tolist()
                billing_stats[med] = {
                    "mean": float(np.mean(arr)) if arr else 0.0,
                    "median": float(np.median(arr)) if arr else 0.0
                }

        condition_med_counts = {}
        grouped = df.groupby(COL_CONDITION)[COL_MEDICATION]
        for condition, tmp in grouped:
            lst = tmp.tolist()
            c_q = Queue()
            for med in lst:
                c_q.enqueue(med)
            med_vals = list(c_q)
            counts = {med: med_vals.count(med) for med in set(med_vals)}
            condition_med_counts[condition] = counts

        self.results = {
            "med_counts": med_counts,
            "billing_stats": billing_stats,
            "condition_med_counts": condition_med_counts
        }

    def export(self) -> None:
        name = "medication"

        res = ["Medication Prescription Counts:"]
        for med, cnt in sorted(self.results["med_counts"].items(), key=lambda x: -x[1]):
            res.append(f"  {med}: {cnt}")

        res.append("\nBilling Stats by Medication:")
        for med, stats in self.results["billing_stats"].items():
            res.append(f"  {med}: mean=${stats['mean']:.2f}, median=${stats['median']:.2f}")

        res.append("\nMedication Counts by Medical Condition:")
        for condition, counts in self.results["condition_med_counts"].items():
            res.append(f"{condition}:")
            for med, cnt in sorted(counts.items(), key=lambda x: -x[1]):
                res.append(f"  {med}: {cnt}")
            res.append("")  

        text = "\n".join(res).strip()
        print(text)
        save_to_txt(name, text)

        # Medication frequency bar chart
        fig1, ax1 = plt.subplots()
        meds = list(self.results["med_counts"].keys())
        counts = [self.results["med_counts"][m] for m in meds]
        ax1.bar(meds, counts, edgecolor="black")
        ax1.set_title("Medication Prescription Frequency")
        ax1.set_xlabel("Medication")
        ax1.set_ylabel("Count")
        plt.xticks(rotation=45, ha="right")
        save_plot(fig1, f"{name}_frequency")

        # Mean billing by medication
        meds_b = list(self.results["billing_stats"].keys())
        means = [self.results["billing_stats"][m]["mean"] for m in meds_b]
        fig2, ax2 = plt.subplots()
        ax2.bar(meds_b, means, edgecolor="black")
        ax2.set_title("Mean Billing by Medication")
        ax2.set_xlabel("Medication")
        ax2.set_ylabel("Mean Billing ($)")
        plt.xticks(rotation=45, ha="right")
        save_plot(fig2, f"{name}_billing_by_medication")

        # Medication counts per condition
        for condition, counts in self.results["condition_med_counts"].items():
            fig, ax = plt.subplots()
            meds_c = list(counts.keys())
            vals = [counts[m] for m in meds_c]
            ax.bar(meds_c, vals, edgecolor="black")
            ax.set_title(f"Medication Counts — {condition}")
            ax.set_xlabel("Medication")
            ax.set_ylabel("Count")
            plt.xticks(rotation=45, ha="right")
            safe_condition = condition.lower().replace(" ", "_")
            save_plot(fig, f"{name}_{safe_condition}_counts")
