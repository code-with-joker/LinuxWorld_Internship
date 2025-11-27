import streamlit as st
from datetime import datetime
DATAFILE = "complaint.txt"

def save_complaint(txt,mood):
    with open(DATAFILE,"a") as f:
        f.write(f'{datetime.now()} | Mood: {mood} | Complaint: {txt}\n')

def load_complaints():
    try:
        with open(DATAFILE,"r") as f:
            return f.readlines()
    except:
        return ()

def search_word(txt):
    txt = txt.lower()
    angry_words = ["angry", "bad","slow","wrost","hate","issue","problem"]
    happy_words = ["happy","smile","nice","good","love","great"]

    for w in angry_words:
        if w in txt:
            return "Angry"

    for w in happy_words:
        if w in txt:
            return "Happy"

    return "Neutral..."

st.title("📢 Campus Complaint Analyzer") 
complaint = st.text_area("Write your complaint:") 
if st.button("Submit"): 
    if complaint.strip() == "": 
        st.warning("Please write something!") 
    else: 
        mood = search_word(complaint) 
        save_complaint(complaint, mood) 
        st.success(f"Complaint saved. Detected mood: {mood}") 
        st.subheader("Previous Complaints") 
        data = load_complaints() 
        if data: 
            for line in data[-10:]: 
                st.write(line) 
        else: st.info("No complaints yet.")
