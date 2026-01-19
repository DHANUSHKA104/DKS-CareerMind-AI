import streamlit as st
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="DKS CareerMind AI",
    layout="wide"
)

# ---------------- SESSION STATE ----------------
if "users" not in st.session_state:
    st.session_state.users = {}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "current_user" not in st.session_state:
    st.session_state.current_user = ""

if "page" not in st.session_state:
    st.session_state.page = "login"

# ---------------- IMAGE PATHS ----------------
LOGO = "assets/logo.png"
LOGIN_IMG = "assets/login.png"
DASHBOARD_IMG = "assets/dashboard.png"

def safe_image(path, width=None):
    if os.path.exists(path):
        st.image(path, width=width)

# ---------------- SIDEBAR ----------------
if st.session_state.logged_in:
    with st.sidebar:
        safe_image(LOGO, width=120)
        st.markdown("## 🤖 DKS CareerMind AI")
        st.caption("Career Intelligence Agent")
        st.divider()

        menu = st.radio(
            "Navigation",
            [
                "Dashboard",
                "Resume Improvement",
                "Internship Recommendation",
                "Logout"
            ]
        )
else:
    menu = None

# ---------------- LOGIN PAGE ----------------
if st.session_state.page == "login" and not st.session_state.logged_in:
    safe_image(LOGIN_IMG, width=350)
    st.title("🔐 Login")

    with st.form("login_form", clear_on_submit=False):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        login_btn = st.form_submit_button("Login")

        if login_btn:
            if email in st.session_state.users and st.session_state.users[email]["password"] == password:
                st.session_state.logged_in = True
                st.session_state.current_user = st.session_state.users[email]["name"]
                st.success("Login successful")
                st.rerun()
            else:
                st.error("Invalid email or password")

    st.markdown("### New user?")
    if st.button("Go to Register"):
        st.session_state.page = "register"
        st.rerun()

# ---------------- REGISTER PAGE (FIXED) ----------------
elif st.session_state.page == "register":
    safe_image(LOGIN_IMG, width=350)
    st.title("📝 Register")

    with st.form("register_form", clear_on_submit=False):
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm = st.text_input("Confirm Password", type="password")

        register_btn = st.form_submit_button("Create Account")

        if register_btn:
            if not name or not email or not password or not confirm:
                st.error("Please fill all details")
            elif password != confirm:
                st.error("Passwords do not match")
            elif email in st.session_state.users:
                st.error("Account already exists. Please login.")
            else:
                st.session_state.users[email] = {
                    "name": name,
                    "password": password
                }
                st.success("Registration successful. Please login.")
                st.session_state.page = "login"
                st.rerun()

    if st.button("Back to Login"):
        st.session_state.page = "login"
        st.rerun()

# ---------------- DASHBOARD ----------------
elif st.session_state.logged_in:
    safe_image(DASHBOARD_IMG, width=600)
    st.title("🤖 DKS CareerMind AI")
    st.subheader(f"Welcome, {st.session_state.current_user}")
    st.write("Career guidance powered by intelligent logic")

    # -------- DASHBOARD --------
    if menu == "Dashboard":
        st.info("""
        ✔ Resume Improvement  
        ✔ Internship Recommendation  
        ✔ Skill Gap Analysis  
        ✔ Learning Roadmap  
        ✔ For 1st year to Graduates  
        """)

    # -------- RESUME IMPROVEMENT --------
    elif menu == "Resume Improvement":
        st.header("📄 Resume Improvement")

        year = st.selectbox(
            "Academic Status",
            ["1st Year", "2nd Year", "3rd Year", "Final Year", "Graduate"]
        )

        department = st.selectbox(
            "Department",
            ["CSE", "ECE", "EEE", "MECH", "CIVIL", "IT", "OTHER"]
        )

        tech_skills = st.text_area("Technical Skills")
        soft_skills = st.text_area("Soft Skills")
        projects = st.text_area("Projects / Internships")
        certifications = st.text_area("Certifications")
        experience = st.text_input("Work Experience (if any)")

        if st.button("Analyze Resume"):
            st.success("Resume analysis completed")

            if year in ["1st Year", "2nd Year"]:
                st.warning("Focus on fundamentals and mini-projects")

            if len(projects.strip()) < 20:
                st.warning("Add more detailed project descriptions")

            if "communication" not in soft_skills.lower():
                st.warning("Improve communication skills")

            if certifications.strip() == "":
                st.info("Add certifications (NPTEL, Coursera, Udemy)")

    # -------- INTERNSHIP --------
    elif menu == "Internship Recommendation":
        st.header("🎯 Internship Recommendation")

        year = st.selectbox(
            "Academic Status",
            ["1st Year", "2nd Year", "3rd Year", "Final Year", "Graduate"]
        )

        skills = st.text_area("Your Skills")

        if st.button("Get Internship Suggestions"):
            st.success("Recommendations generated")

            if year in ["1st Year", "2nd Year"]:
                st.info("Recommended beginner & learning internships")

            if "python" in skills.lower():
                st.write("- Python Internship")
            if "web" in skills.lower():
                st.write("- Web Development Internship")
            if "ml" in skills.lower():
                st.write("- Machine Learning Internship")

            st.markdown("""
            **Platforms:** Internshala, LinkedIn, Indeed
            """)

    # -------- LOGOUT --------
    elif menu == "Logout":
        st.session_state.logged_in = False
        st.session_state.page = "login"
        st.rerun()

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("© DKS CareerMind AI | Second year Academic Project")
