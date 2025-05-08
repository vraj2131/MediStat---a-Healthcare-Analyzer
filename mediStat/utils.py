from pathlib import Path
import matplotlib.pyplot as plt
from mediStat.constants import RESULTS_DIR, STATS_FILE_TEMPLATE, PLOT_FILE_TEMPLATE

def ensure_results_dir() -> None:
    """
    Ensure that the results directory exists.
    """
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

def save_to_txt(name: str, text: str) -> Path:
    """
    Save a string of text to a stats file in the results directory.

    :param name: Logical name used to format the filename (e.g., "billing" → "billing_stats.txt")
    :param text: The content to write into the file.
    :return: Path to the written file.
    """
    ensure_results_dir()
    filename = STATS_FILE_TEMPLATE.format(name=name)
    filepath = RESULTS_DIR / filename
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    return filepath

def save_plot(fig: plt.Figure, name: str) -> Path:
    """
    Save a matplotlib figure to a PNG in the results directory.

    :param fig: A matplotlib Figure object.
    :param name: Logical name used to format the filename (e.g., "billing" → "billing_plot.png")
    :return: Path to the saved image.
    """
    ensure_results_dir()
    filename = PLOT_FILE_TEMPLATE.format(name=name)
    filepath = RESULTS_DIR / filename
    fig.savefig(filepath, bbox_inches="tight")
    plt.close(fig)
    return filepath
