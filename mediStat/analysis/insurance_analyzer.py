# mediStat/analysis/insurance_analyzer.py

import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame

from mediStat.base_analyzer import BaseAnalyzer
from mediStat.structures import Queue
from mediStat.utils import save_to_txt, save_plot
from mediStat.constants import (
    COL_INSURANCE, 
    COL_BILLING,
)


class InsuranceAnalyzer(BaseAnalyzer):
    """
        Analyzing for insurance data
    """

    def analyze(self) -> None:
        df: DataFrame = self.df.copy()

        tmp = df[COL_INSURANCE]
        providers_q = Queue()
        for i in tmp:
            providers_q.enqueue(i)
        providers_list = list(providers_q)

        provider_counts = {
            provider: providers_list.count(provider)
            for provider in set(providers_list)
        }

        billing_stats = {}
        if COL_BILLING in df.columns:
            grp = df.dropna(subset=[COL_BILLING]).groupby(COL_INSURANCE)[COL_BILLING]
            for provider, vals in grp:
                arr = vals.astype(float).tolist()
                billing_stats[provider] = {
                    "mean": float(np.mean(arr)) if arr else 0.0,
                    "median": float(np.median(arr)) if arr else 0.0
                }

        self.results = {
            "provider_counts": provider_counts,
            "billing_stats": billing_stats
        }

    def export(self) -> None:
        name = "insurance"

        res = ["Insurance Provider Counts:"]
        for provider, cnt in sorted(self.results["provider_counts"].items(), key=lambda x: -x[1]):
            res.append(f"  {provider}: {cnt}")
        res.append("\nBilling Stats by each Provider:")
        for provider, stats in self.results["billing_stats"].items():
            res.append(f"{provider}: mean=${stats['mean']:.2f}, median=${stats['median']:.2f}")

        text = "\n".join(res)
        print(text)
        save_to_txt(name, text)

        # Pie chart for market share
        fig1, ax1 = plt.subplots()
        ax1.pie(self.results["provider_counts"].values(), labels=self.results["provider_counts"].keys(), autopct='%1.1f%%', startangle=90)
        ax1.set_title("Insurance Provider Market Share")
        save_plot(fig1, f"{name}_pie")

        # Bar chart for mean billing by provider
        providers = list(self.results["billing_stats"].keys())
        means = [self.results["billing_stats"][p]["mean"] for p in providers]
        fig2, ax2 = plt.subplots()
        ax2.bar(providers, means, edgecolor="black")
        ax2.set_title("Mean Billing by Insurance Provider")
        ax2.set_xlabel("Insurance Provider")
        ax2.set_ylabel("Mean Billing ($)")
        plt.xticks(rotation=45, ha="right")
        save_plot(fig2, f"{name}_billing_by_provider")
