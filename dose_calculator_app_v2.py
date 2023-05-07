import streamlit as st # to import libarary
import math

# ---------------- to creates the title -------------------
st.title("Dose calculator for vancomycin in VLBW neonates, Alsultan model")
# ---------------- to creates a horizontal line -------------------
st.write("---")
 
# ---------------- to enter the Patient Parameters -------------------
st.header("Patient Parameters") # header 
# input 1
PMA = st.number_input(label="Post menstural age (PMA), units = weeks")
# input 2
WT = st.number_input(label="Weight (WT), units = kilograms")
# input 3
SC = st.number_input(label="Serum Creatinine, units = milligram/deciliter")
# input 4
dose = st.number_input(label="Dose in milligram")

# -------------------- to choose the Dosing Freruency ----------------
#input 5
frequency = st.selectbox(
    'Select the frequency to perform:',
    ('8', '12', '18', '24'))
dosing_freruency = float(frequency)

# -------------------- Time of infusion = fixed at 2 hours ----------------
#input 6
time_of_infusion= 2
st.write("Time of infusion = fixed at 2 hours")

# -------------------- to calculate eq. ----------------
def calculate():
    volume_of_distribution = 0.81*(WT/0.93)
    drug_clearance = (0.09*((WT/0.93)**0.75)) * ((0.6/SC)**0.48) * ((PMA**4.42)/ ((PMA**4.42)+(26.3**4.42)))
    ke= drug_clearance/volume_of_distribution
    Recommended_total_daily_dose = 450 * drug_clearance  
                                             
    prediction =(((dose/(time_of_infusion*drug_clearance)))*(1-math.exp(-ke*time_of_infusion))/(1-math.exp(-ke*dosing_freruency)))*math.exp(-ke*(dosing_freruency-time_of_infusion))

# -------------------- to print the results ----------------
    st.write("Volume of Distribution = ",round(volume_of_distribution,2))
    st.write("Drug Clearance = ",round(drug_clearance,2))
    st.write("Ke = ",round(ke,2))
    st.write("Recommended total daily dose in milligrams = ",round(Recommended_total_daily_dose,2))
    st.write("The Predicted Trough = ",round(prediction,2))

# -------------------- to run the button ----------------
if st.button("Calculate Dose"):
    calculate()
