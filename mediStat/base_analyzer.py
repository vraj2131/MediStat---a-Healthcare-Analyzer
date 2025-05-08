# mediStat/base_analyzer.py

from abc import ABC, abstractmethod
from pandas import DataFrame

class BaseAnalyzer(ABC):
    """
    Abstract base class for all analyzers.
    Analyzers must implement analyze() to compute results
    and export() to save stats and plots.
    """

    def __init__(self, df: DataFrame):
        """
        :param df: pandas DataFrame containing the full dataset.
        """
        self.df = df
        self.results = None

    @abstractmethod
    def analyze(self) -> None:
        """
        Perform the analysis on self.df and store any computed
        statistics, summaries, or intermediate data in self.results.
        """
        pass

    @abstractmethod
    def export(self) -> None:
        """
        Export the results of analyze():
          - write textual summaries (e.g., via utils.save_to_txt)
          - save plots (e.g., via utils.save_plot)
        """
        pass
