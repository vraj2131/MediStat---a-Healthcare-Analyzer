import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame

from mediStat.base_analyzer import BaseAnalyzer
from mediStat.structures import Stack
from mediStat.utils import save_to_txt, save_plot
from mediStat.constants import COL_BILLING, COL_CONDITION, BILLING_THRESHOLD

class BillingAnalyzer(BaseAnalyzer):
    """
        Analyzing billing data for the patients in different ways.
    """

    def analyze(self) -> None:
        df: DataFrame = self.df.copy()

        bill_stk: Stack = Stack()
        for amnt in df[COL_BILLING].astype(float):
            bill_stk.push(amnt)
        bill_list = list(bill_stk)

        count = len(bill_list)
        total = float(np.sum(bill_list)) if count else 0.0
        mean = float(np.mean(bill_list)) if count else 0.0
        median = float(np.median(bill_list)) if count else 0.0
        high_cost_count = sum(1 for amnt in bill_list if amnt > BILLING_THRESHOLD)

        condition_grp = df.dropna(subset=[COL_BILLING, COL_CONDITION]).groupby(COL_CONDITION)[COL_BILLING]
        condition_stats = {}
        for condition, res in condition_grp:
            tmp = res.astype(float).tolist()
            condition_stats[condition] = {
                "count": len(tmp),
                "mean": float(np.mean(tmp)),
                "median": float(np.median(tmp))
            }

        self.results = {
            "billing_list": bill_list,
            "count": count,
            "total": total,
            "mean": mean,
            "median": median,
            "high_cost_count": high_cost_count,
            "condition_stats": condition_stats
        }

    def export(self) -> None:
        name = "billing"

        res = [
            f"Total records         : {self.results['count']}",
            f"Total billing amount  : ${self.results['total']:.2f}",
            f"Mean billing amount   : ${self.results['mean']:.2f}",
            f"Median billing amount : ${self.results['median']:.2f}",
            f"Cases above ${BILLING_THRESHOLD:.2f}: {self.results['high_cost_count']}",
            "",
            "Billing by Condition:"
        ]
        for condition, stats in self.results["condition_stats"].items():
            res.append(
                f"  {condition} -> count: {stats['count']}, "
                f"mean: ${stats['mean']:.2f}, median: ${stats['median']:.2f}"
            )
        text = "\n".join(res)

        save_to_txt(name, text)
        print(text)

        # Histogram of billing amounts
        fig1, ax1 = plt.subplots()
        ax1.hist(self.results["billing_list"], bins=20)
        ax1.set_title("Billing Amount Distribution")
        ax1.set_xlabel("Amount ($)")
        ax1.set_ylabel("Frequency")
        save_plot(fig1, name + "_hist")

        # Mean billing by each condition
        conditions = list(self.results["condition_stats"].keys())
        means = [self.results["condition_stats"][c]["mean"] for c in conditions]

        fig2, ax2 = plt.subplots()
        ax2.bar(conditions, means)
        ax2.set_title("Mean Billing by Condition")
        ax2.set_xlabel("Condition")
        ax2.set_ylabel("Mean Amount ($)")
        plt.xticks(rotation=45, ha="right")
        save_plot(fig2, name + "_by_condition")
