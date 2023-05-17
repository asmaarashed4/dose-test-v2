import streamlit as st # to import libarary
import math

# ---------------- to creates the title -------------------
st.title("Dose calculator for vancomycin in neonates, Frymoyer model")
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
time_of_infusion= 2
st.write("Time of infusion = fixed at 2 hours")

# -------------------- to calculate eq. ----------------
def calculate():
#input 5
 dosing_freruency = 8.00

 if dosing_freruency == 8.00:
    volume_of_distribution = 1.75*(WT/2.9)
    drug_clearance = (0.34*((WT/2.9)**0.75)) * ((1/SC)**0.267) * (1/(1+((PMA/34.8))**(-4.52) ))
    ke= drug_clearance/volume_of_distribution
    Recommended_total_daily_dose = 450 * drug_clearance  
    dose = Recommended_total_daily_dose /3            #given every 8 hours                            
    prediction =(((dose/(time_of_infusion*drug_clearance)))*(1-math.exp(-ke*time_of_infusion))/(1-math.exp(-ke*dosing_freruency)))*math.exp(-ke*(dosing_freruency-time_of_infusion))
    if prediction > 15:
      dosing_freruency = 12.00
    else:
     st.write("Recommended dose = ",round(dose,2))
     st.write("Dosing freruency= ",round(dosing_freruency,2))
     st.write("prediction= ",round(prediction,2))
     
 if dosing_freruency == 12.00:
    volume_of_distribution = 1.75*(WT/2.9)
    drug_clearance = (0.34*((WT/2.9)**0.75)) * ((1/SC)**0.267) * (1/(1+((PMA/34.8))**(-4.52) ))
    ke= drug_clearance/volume_of_distribution
    Recommended_total_daily_dose = 450 * drug_clearance  
    dose = Recommended_total_daily_dose /2     #given every 12 hours                                    
    prediction =(((dose/(time_of_infusion*drug_clearance)))*(1-math.exp(-ke*time_of_infusion))/(1-math.exp(-ke*dosing_freruency)))*math.exp(-ke*(dosing_freruency-time_of_infusion))
    if prediction > 15:
      dosing_freruency = 18.00
    else:
     st.write("Recommended dose = ",round(dose,2))
     st.write("Dosing freruency= ",round(dosing_freruency,2))
     st.write("prediction= ",round(prediction,2))

 if dosing_freruency == 18.00:
    volume_of_distribution = 1.75*(WT/2.9)
    drug_clearance = (0.34*((WT/2.9)**0.75)) * ((1/SC)**0.267) * (1/(1+((PMA/34.8))**(-4.52) ))
    ke= drug_clearance/volume_of_distribution
    Recommended_total_daily_dose = 450 * drug_clearance  
    dose = Recommended_total_daily_dose/1.33          #given every 18 hours                             
    prediction =(((dose/(time_of_infusion*drug_clearance)))*(1-math.exp(-ke*time_of_infusion))/(1-math.exp(-ke*dosing_freruency)))*math.exp(-ke*(dosing_freruency-time_of_infusion))
    if prediction > 15:
      dosing_freruency = 24.00
    else:
     st.write("Recommended dose = ",round(dose,2))
     st.write("Dosing freruency= ",round(dosing_freruency,2))
     st.write("prediction= ",round(prediction,2))

 if dosing_freruency == 24.00:
    volume_of_distribution = 1.75*(WT/2.9)
    drug_clearance = (0.34*((WT/2.9)**0.75)) * ((1/SC)**0.267) * (1/(1+((PMA/34.8))**(-4.52) ))
    ke= drug_clearance/volume_of_distribution
    Recommended_total_daily_dose = 450 * drug_clearance  
    dose = Recommended_total_daily_dose /1    #given every 24 hours                                  
    prediction =(((dose/(time_of_infusion*drug_clearance)))*(1-math.exp(-ke*time_of_infusion))/(1-math.exp(-ke*dosing_freruency)))*math.exp(-ke*(dosing_freruency-time_of_infusion))
    if prediction > 20:
      st.text('No Recommended dose for this patient')
    else:
     st.write("Recommended dose = ",round(dose,2))
     st.write("Dosing freruency= ",round(dosing_freruency,2))
     st.write("prediction= ",round(prediction,2))
# -------------------- to run the button ----------------
if st.button("Calculate Dose"):
 calculate()
