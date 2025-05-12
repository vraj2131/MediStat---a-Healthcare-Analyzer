import streamlit as st
import pandas as pd

from mediStat.data_loader     import DataLoader
from mediStat.analysis.billing_analyzer import BillingAnalyzer
from mediStat.analysis.insurance_analyzer import InsuranceAnalyzer
from mediStat.analysis.medication_analyzer import MedicationAnalyzer
from mediStat.analysis.demographic_analyzer import DemographicAnalyzer
from mediStat.analysis.admission_analyzer  import AdmissionAnalyzer

@st.cache_data
def load_data():
    return DataLoader().load_dataframe()

df = load_data()

st.title("🏥 Healthcare Data Dashboard")

# --- Billing section ---
st.header("💳 Billing Overview")
bill = BillingAnalyzer(df)
bill.analyze()
# show key stats
st.metric("Total Encounters", bill.results["count"])
st.metric("High-Cost Cases",    bill.results["high_cost_count"])
# render plot
hist1 = bill.results["billing_list"]
st.bar_chart(pd.DataFrame(hist1, columns=["Amount"]))

# --- Insurance section ---
st.header("🛡️ Insurance Market Share")
ins = InsuranceAnalyzer(df)
ins.analyze()
counts = ins.results["provider_counts"]
st.bar_chart(pd.DataFrame.from_dict(counts, orient="index", columns=["Patients"]))

# --- Medication section ---
st.header("💊 Medication Usage")
med = MedicationAnalyzer(df)
med.analyze()
st.bar_chart(pd.DataFrame.from_dict(med.results["med_counts"], orient="index", columns=["Count"]))

# --- Demographics section ---
st.header("👥 Demographics")
demo = DemographicAnalyzer(df)
demo.analyze()
st.bar_chart(pd.DataFrame.from_dict(demo.results["gender_counts"], orient="index", columns=["Count"]))

# --- Admissions section ---
st.header("🏨 Admissions & Length-of-Stay")
adm = AdmissionAnalyzer(df)
adm.analyze()
st.bar_chart(pd.DataFrame.from_dict(adm.results["type_counts"], orient="index", columns=["Count"]))

