from pathlib import Path
import matplotlib.pyplot as plt
from mediStat.constants import RESULTS_DIR, STATS_FILE_TEMPLATE, PLOT_FILE_TEMPLATE

def ensure_results_dir() -> None:
    """
        Will check if results directory is present
    """
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

def save_to_txt(name: str, text: str) -> Path:
    """
        Will save the given text to a file in the results directory
    """
    ensure_results_dir()
    filename = STATS_FILE_TEMPLATE.format(name=name)
    filepath = RESULTS_DIR / filename
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    return filepath

def save_plot(fig: plt.Figure, name: str) -> Path:
    """
        Will save the given plot to a file in the results directory
    """
    ensure_results_dir()
    filename = PLOT_FILE_TEMPLATE.format(name=name)
    filepath = RESULTS_DIR / filename
    fig.savefig(filepath, bbox_inches="tight")
    plt.close(fig)
    return filepath
