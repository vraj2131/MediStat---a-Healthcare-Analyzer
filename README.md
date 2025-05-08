# Healthcare Data Science Project

This project applies Data Science techniques to a real-world healthcare dataset, turning raw patient records into detailed insights. Following our proposal, we load and clean data about admissions, billing, medications, insurance, demographic profiles, and clinical test results. By building modular analyzer components, we compute key statistics and generate visualizations that reveal cost drivers, treatment patterns, coverage distributions, and population health indicators.

## Key Features

* **Custom Analysis Library**: Reusable `mediStat` package with data loading, structure utilities, and abstract analyzer base class.
* **Modular Analyzers**: Separate modules for billing, medication, insurance, health indicators, demographics, admissions, and test results—each producing summary metrics and plots.
* **End-to-End Pipeline**: A single `main.py` script orchestrates data ingestion, analysis execution, and result export.
* **Insight Generation**: Automated computation of means, medians, frequency distributions, and correlations, enabling data-driven decision making.

## Real-Time Applications

This data science pipeline can drive real-time decision support and operational monitoring in healthcare settings:

* **Dynamic Resource Allocation**: Hospitals can monitor admission trends and length-of-stay in near real-time to optimize bed management and staffing levels.
* **Cost Control Alerts**: Billing analytics can flag unusually high charges as they occur, enabling finance teams to investigate and mitigate unexpected expenses quickly.
* **Medication Adherence Monitoring**: By analyzing prescription and medication dispensation patterns, pharmacy departments can identify potential noncompliance or stock shortages in time to intervene.
* **Risk Stratification Dashboards**: Automated health indicator scores (e.g., glucose or cholesterol levels) can feed into clinical dashboards that alert providers about high-risk patients.

## Dependencies

All third-party libraries are listed in `requirements.txt`:

* `pandas>=1.5.0`
* `numpy>=1.23.0`
* `matplotlib>=3.5.0`

## Setup & Installation

1. **Clone the repository**:

   ```bash
   git clone <repo-url>
   cd ProjectRoot
   ```

2. **Create and activate a Python virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Windows PowerShell: .\venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Analysis

Execute the full pipeline with:

```bash
python main.py
```

This will:

1. Load and preprocess `data/healthcare_dataset.csv`.
2. Run each analyzer to compute statistics and create plots.
3. Print summaries in the terminal.
4. Save text reports (`*_stats.txt`) and images (`*_plot.png`) in the `results/` folder.

## Extending the Project

* **New Analyzer**: Add a Python module under `mediStat/analysis/`, subclass `BaseAnalyzer`, implement `analyze()` and `export()`.
* **Adjust Constants**: Update `mediStat/constants.py` for new columns or thresholds.
* **CLI Options**: Enhance `main.py` to accept command-line arguments for selective execution.
* **Dashboard Integration**: Use a dashboard framework (e.g., Dash or Streamlit) to present analytics and plots interactively through a web interface.

## License

This project is released under the MIT License—feel free to use and modify.
