import streamlit as st
from scipy.stats import norm

def ab_test(control_visitors, control_conversions, treatment_visitors, treatment_conversions, confidence_level):
    # Calculate conversion rates
    control_conversion_rate = control_conversions / control_visitors
    treatment_conversion_rate = treatment_conversions / treatment_visitors
    
    # Calculate pooled probability
    pooled_probability = (control_conversions + treatment_conversions) / (control_visitors + treatment_visitors)
    
    # Calculate standard error
    standard_error = ((pooled_probability * (1 - pooled_probability)) * ((1 / control_visitors) + (1 / treatment_visitors))) ** 0.5
    
    # Calculate z-score
    z_score = (treatment_conversion_rate - control_conversion_rate) / standard_error
    
    # Determine critical value based on confidence level
    if confidence_level == 90:
        critical_value = norm.ppf(0.95)
    elif confidence_level == 95:
        critical_value = norm.ppf(0.975)
    elif confidence_level == 99:
        critical_value = norm.ppf(0.995)
    else:
        raise ValueError("Confidence level must be 90, 95, or 99")
    
    # Perform hypothesis test
    if z_score > critical_value:
        return "Experiment Group is Better"
    elif z_score < -critical_value:
        return "Control Group is Better"
    else:
        return "Indeterminate"

def main():
    st.title("📈 Hypothesis Testing App 📈")
    
    # Sidebar for customization
    st.sidebar.title("Results 💯")
    confidence_level = st.sidebar.selectbox("Confidence Level", [90, 95, 99], index=1)
    
    # Input fields for control and treatment group data
    control_visitors = st.number_input("Control Group Visitors", min_value=0, step=1)
    control_conversions = st.number_input("Control Group Conversions", min_value=0, step=1)
    treatment_visitors = st.number_input("Treatment Group Visitors", min_value=0, step=1)
    treatment_conversions = st.number_input("Treatment Group Conversions", min_value=0, step=1)
    
    # Perform hypothesis test
    if st.button("Run Hypothesis Test 🔎"):
        result = ab_test(control_visitors, control_conversions, treatment_visitors, treatment_conversions, confidence_level)
        st.sidebar.subheader("Result:")
        st.sidebar.write(result)

if __name__ == "__main__":
    main()
