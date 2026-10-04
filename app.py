import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="LabSync AI",
    page_icon="💻",
    layout="wide"
)

# Load CSS
def load_css():
    css_file = Path("static/style.css")
    if css_file.exists():
        with open(css_file, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Header
st.markdown("""
<div class="header">
    <h1>💻 LabSync AI</h1>
    <p>Smart Lab Seat & PC Reservation System</p>
</div>
""", unsafe_allow_html=True)

# Navigation
menu = st.radio(
    "Navigation",
    ["Home", "Reserve Seat", "Lab Status", "About"],
    horizontal=True
)

if menu == "Home":

    st.markdown("""
    <div class="hero">
        <h2>Welcome to LabSync AI</h2>
        <p>
        Find available computers and seats, reserve them online,
        and avoid waiting in the computer lab.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
            <h3>💻 Available PCs</h3>
            <h2>25</h2>
            <p>Computers ready to use</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h3>🪑 Available Seats</h3>
            <h2>18</h2>
            <p>Seats available now</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <h3>📊 Lab Occupancy</h3>
            <h2>55%</h2>
            <p>Current lab usage</p>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("✨ Main Features")

    col1, col2 = st.columns(2)

    with col1:
        st.info("📅 Online Seat & PC Reservation")
        st.info("📱 QR Code Check-in")
        st.info("⏱️ Automatic Reservation Cancellation")

    with col2:
        st.success("🤖 AI Crowd Prediction")
        st.success("🔔 Waitlist Notifications")
        st.success("🖥️ PC Health Monitoring")


elif menu == "Reserve Seat":

    st.header("📅 Reserve Your Seat")

    name = st.text_input("Enter Your Name")
    roll = st.text_input("Enter Roll Number")

    col1, col2 = st.columns(2)

    with col1:
        seat = st.selectbox(
            "Select Seat",
            ["Seat A1", "Seat A2", "Seat A3", "Seat B1"]
        )

    with col2:
        pc = st.selectbox(
            "Select Computer",
            ["PC 01", "PC 02", "PC 03", "PC 04"]
        )

    time = st.selectbox(
        "Select Time",
        ["9:00 AM - 10:00 AM",
         "10:00 AM - 11:00 AM",
         "11:00 AM - 12:00 PM",
         "1:00 PM - 2:00 PM"]
    )

    if st.button("Reserve Now", use_container_width=True):

        if name and roll:
            st.success(
                f"Reservation Successful! 🎉\n\n"
                f"Student: {name}\n\n"
                f"Seat: {seat}\n\n"
                f"Computer: {pc}\n\n"
                f"Time: {time}"
            )
        else:
            st.warning("Please enter your Name and Roll Number.")


elif menu == "Lab Status":

    st.header("📊 Live Lab Status")

    st.progress(55)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total PCs", "50")

    with col2:
        st.metric("Available PCs", "25")

    st.subheader("Computer Status")

    status = {
        "PC 01": "🟢 Available",
        "PC 02": "🔴 Occupied",
        "PC 03": "🟢 Available",
        "PC 04": "🔴 Occupied",
        "PC 05": "🟢 Available",
        "PC 06": "🟢 Available"
    }

    for computer, condition in status.items():
        st.write(f"**{computer}:** {condition}")

    st.subheader("🤖 AI Crowd Prediction")

    st.info("""
    9:00 AM - 11:00 AM → High Crowd (95%)

    11:00 AM - 1:00 PM → Medium Crowd (60%)

    1:00 PM - 2:00 PM → Best Time (35%)
    """)


elif menu == "About":

    st.header("About LabSync AI")

    st.write("""
    LabSync AI is a Smart Lab Seat and Computer Reservation System.

    It helps students find available computers and seats before
    entering the computer laboratory.
    """)

    st.subheader("Project Benefits")

    st.write("""
    ✅ Saves students' time

    ✅ Reduces lab crowd

    ✅ Easy online reservation

    ✅ Better computer management

    ✅ AI-based crowd prediction
    """)

    st.subheader("Technology Used")

    st.write("""
    🐍 Python

    🌐 Streamlit

    🎨 HTML & CSS

    📊 Data Analysis
    """)

st.markdown("---")
st.markdown(
    "<center>© 2026 LabSync AI | Smart Laboratory Management System</center>",
    unsafe_allow_html=True
)