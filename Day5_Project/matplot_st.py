import streamlit as st
import matplotlib.pyplot as plt

st.title("Marks Comparison Chart")

# Data
subjects = ["M1", "M2", "Chem", "Physics"]
kishan = [15, 19, 11, 16]
rahul  = [18, 17, 14, 12]

# Create Figure
fig, ax = plt.subplots()

ax.plot(subjects, kishan, marker='D', label="Kishan")
ax.plot(subjects, rahul, marker='o', label="Rahul")

ax.set_title("Comparison of Marks")
ax.set_xlabel("Subjects")
ax.set_ylabel("Marks")
ax.legend()
ax.grid()

# Show graph in Streamlit
st.pyplot(fig)
