from abc import ABC, abstractmethod
from pandas import DataFrame

class BaseAnalyzer(ABC):
    """
        Abstract base class for all analyzers.
        It have two methods analyze and export to results.
    """

    def __init__(self, df: DataFrame):
        self.df = df
        self.results = None

    @abstractmethod
    def analyze(self) -> None:
        pass

    @abstractmethod
    def export(self) -> None:
        pass
