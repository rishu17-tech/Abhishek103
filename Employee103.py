import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title
st.title("📊 Hiring Growth Calculator")

st.write("Enter values and click calculate to see results")

# Inputs
st.subheader("🔹 Input Values")

E0 = st.number_input("Initial Employees (E0)", min_value=1, value=50)
r = st.number_input("Growth Rate (r)", min_value=0.01, value=0.3)
K = st.number_input("Maximum Capacity (K)", min_value=1, value=1000)

# Logistic Function
def logistic_growth(t, E0, r, K):
    return K / (1 + ((K - E0) / E0) * np.exp(-r * t))

# Button
if st.button("Calculate Growth"):

    # Time range
    t = np.linspace(0, 24, 100)

    # Output calculation
    employees = logistic_growth(t, E0, r, K)

    # Graph
    st.subheader("📈 Output Graph")
    fig, ax = plt.subplots()
    ax.plot(t, employees)
    ax.set_xlabel("Time (Months)")
    ax.set_ylabel("Employees")
    ax.set_title("Hiring Growth Curve")
    st.pyplot(fig)

    # Final Output
    st.subheader("📌 Final Result")
    st.write(f"Estimated Final Employees: {int(employees[-1])}")

    # Interpretation
    st.subheader("🧠 Interpretation")
    if r > 0.4:
        st.write("Fast hiring growth")
    elif r < 0.2:
        st.write("Slow hiring growth")
    else:
        st.write("Moderate hiring growth")

    if employees[-1] >= 0.9 * K:
        st.write("Company reaches near maximum capacity")
