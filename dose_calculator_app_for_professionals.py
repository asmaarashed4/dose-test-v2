import streamlit as st # to import libarary
import math

# ---------------- to creates the title -------------------
st.title("Dose Calculator for Vancomycin in Neonates")
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

time_of_infusion= 2 #fixed at 2 hours

# -------------------- The Dosing Freruency ----------------
dosing_freruency = 8.00

# -------------------- to calculate eq. ----------------
def calculate():
    volume_of_distribution = 0.81*(WT/0.93)
    drug_clearance = (0.09*((WT/0.93)**0.75)) * ((0.6/SC)**0.48) * ((PMA**4.42)/ ((PMA**4.42)+(26.3**4.42)))
    ke= drug_clearance/volume_of_distribution
    Recommended_total_daily_dose = 450 * drug_clearance  
    dose = Recommended_total_daily_dose * (dosing_freruency/24)
                                             
    prediction =(((Recommended_total_daily_dose/(time_of_infusion*drug_clearance)))*(1-math.exp(-ke*time_of_infusion))/(1-math.exp(-ke*dosing_freruency)))*math.exp(-ke*(dosing_freruency-time_of_infusion))
# -------------------- to print the results ----------------
    #st.write("Volume of Distribution = ",round(volume_of_distribution,2))
    #st.write("Drug Clearance = ",round(drug_clearance,2))
    #st.write("Ke = ",round(ke,2))
    st.write("Recommended total daily dose in milligrams = ",round(Recommended_total_daily_dose,2))
    #st.write("The Predicted Trough = ",round(prediction,2))

# -------------------- to perform Decision tree ---------------
    if dosing_freruency == 8.00 and prediction > 15:
     dosing_freruency == 12.00 
    elif dosing_freruency == 12 and prediction > 15:
     dosing_freruency == 18 
    elif dosing_freruency == 18 and prediction > 20:
     dosing_freruency == 24 
    elif dosing_freruency == 24 and prediction > 20:
      st.text('No Recommended dose for this patient')
    else:
      st.text('NA')
 
# -------------------- to run the button ----------------
if st.button("Calculate Dose"):
    calculate()