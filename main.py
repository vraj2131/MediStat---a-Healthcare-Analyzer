from mediStat.data_loader import DataLoader

from mediStat.analysis.billing_analyzer import BillingAnalyzer
from mediStat.analysis.medication_analyzer import MedicationAnalyzer
from mediStat.analysis.insurance_analyzer import InsuranceAnalyzer
from mediStat.analysis.health_indicator_analyzer import HealthIndicatorAnalyzer
from mediStat.analysis.demographic_analyzer import DemographicAnalyzer
from mediStat.analysis.admission_analyzer import AdmissionAnalyzer


def main():

    loader = DataLoader()
    df = loader.load_dataframe()

    analyzers = [
        BillingAnalyzer(df),
        MedicationAnalyzer(df),
        InsuranceAnalyzer(df),
         HealthIndicatorAnalyzer(df),
        DemographicAnalyzer(df),
        AdmissionAnalyzer(df),
    ]

    for analyzer in analyzers:
        name = analyzer.__class__.__name__
        print(f"\n=== Running {name} ===")
        analyzer.analyze()
        analyzer.export()

    print("\nAll analyses complete. Check the results/ directory for outputs.")
    


if __name__ == "__main__":
    main()
