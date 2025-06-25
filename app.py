

import streamlit as st
from resume_parser import parse_resume
from matcher import compute_cosine_similarity

st.set_page_config(page_title="AI Resume Screener", layout="centered")

# Sidebar
with st.sidebar:
    st.title("ℹ️ About")
    st.markdown(
        """
        **AI Resume Screener** helps you compare your resume to a job description and get a match score.
        
        **Instructions:**
        1. Upload your resume (PDF, DOCX, or TXT).
        2. Paste the job description.
        3. Click **Match Resume** to see your score!
        ---
        **Developed by: Maida Shahzad**
        """
    )

st.title("📄 AI-Powered Resume Screener")
st.markdown("Upload your resume and compare it with a job description to see the match score.")

col1, col2 = st.columns(2)

with col1:
    resume_file = st.file_uploader("Upload Resume (.pdf, .docx, .txt)", type=["pdf", "docx", "txt"])
    if resume_file:
        st.success(f"Uploaded: {resume_file.name}")

with col2:
    job_description = st.text_area("Paste Job Description", height=200)
    if st.button("Use Example Job Description"):
        job_description = st.session_state['job_description'] = (
            "We are seeking a Data Analyst with experience in Python, SQL, and data visualization tools. "
            "Responsibilities include data cleaning, analysis, and reporting."
        )
    if 'job_description' in st.session_state:
        job_description = st.session_state['job_description']

if st.button("🔍 Match Resume"):
    if resume_file and job_description:
        with st.spinner("Extracting text and calculating similarity..."):
            try:
                resume_text = parse_resume(resume_file)
                with st.expander("🔎 View Extracted Resume Text"):
                    st.write(resume_text)
                score = compute_cosine_similarity(resume_text, job_description)
                st.success(f"✅ Match Score: **{score:.2%}**")
                st.progress(min(int(score * 100), 100))
            except Exception as e:
                st.error(f"❌ Error: {e}")
    else:
        st.warning("Please upload a resume and paste a job description.")
