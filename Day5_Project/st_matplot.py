import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dynamic Marks Chart", layout="centered")

# --------------------- HEADER ---------------------
st.title("Dynamic Marks Comparison Chart")

# --------------------- DATA -----------------------
subjects = ["M1", "M2", "Chem", "Physics", "English", "Computer"]
kishan = [15, 19, 11, 16, 18, 20]
rahul  = [18, 17, 14, 12, 16, 19]

students = {
    "Kishan": kishan,
    "Rahul": rahul
}

# --------------------- SIDEBAR CONTROLS ---------------------
st.sidebar.title("⚙️ Customization Panel")

# Theme
theme = st.sidebar.radio("Select Theme", ["Light", "Dark"])



# Dropdown subjects
selected_subjects = st.sidebar.multiselect(
    "Select subjects to display", 
    subjects, 
    default=subjects
)

# Select students
selected_students = st.sidebar.multiselect(
    "Select Students", 
    list(students.keys()), 
    default=list(students.keys())
)

# Color and style options
colors = ["blue", "red", "green", "purple", "orange", "black"]
styles = ["-", "--", "-.", ":"]

line_color = st.sidebar.selectbox("Line Color", colors)
line_style = st.sidebar.selectbox("Line Style", styles)

# --------------------- FILTER DATA ---------------------
indices = [subjects.index(sub) for sub in selected_subjects]

# --------------------- PLOT GRAPH ---------------------
fig, ax = plt.subplots(figsize=(7, 4))

for student in selected_students:
    marks = [students[student][i] for i in indices]
    ax.plot(
        selected_subjects,
        marks,
        marker="o",
        label=student,
        color=line_color,
        linestyle=line_style
    )

ax.set_title("Marks Comparison Chart", fontsize=16)
ax.set_xlabel("Subjects")
ax.set_ylabel("Marks")
ax.grid()

ax.legend()

# Show graph in Streamlit
st.pyplot(fig)
