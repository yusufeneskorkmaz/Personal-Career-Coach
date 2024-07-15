import streamlit as st
import requests
from io import BytesIO


def main():
    st.set_page_config(page_title="Personal Career Coach", layout="wide")
    st.title("Personal Career Coach")

    # Sidebar for user inputs
    with st.sidebar:
        st.header("User Input")
        uploaded_file = st.file_uploader("Upload your Resume (PDF)", type="pdf")
        job_description = st.text_area("Paste Job Description")
        github_username = st.text_input("Enter your GitHub Username")
        analyze_button = st.button("Analyze")

    # Main content area
    if analyze_button and uploaded_file and job_description and github_username:
        with st.spinner("Analyzing your career profile..."):
            try:
                # Prepare the data for the API request
                files = {"resume": ("resume.pdf", uploaded_file.getvalue(), "application/pdf")}
                data = {
                    "job_description": job_description,
                    "github_username": github_username
                }

                # Make the API request
                response = requests.post("http://localhost:8000/analyze", files=files, data=data)
                response.raise_for_status()  # Raise an exception for HTTP errors

                # Print the raw response for debugging
                st.write("Raw API Response:", response.text)

                try:
                    result = response.json()
                except ValueError:
                    st.error("Invalid JSON response from the API.")
                    return

                # Print the result for debugging
                st.write("Parsed API Response:", result)

                # Check if the result is not None and contains the expected keys
                if result and "JD Match" in result and "MissingKeywords" in result and "Profile Summary" in result and "GitHub Project Recommendation" in result:
                    # Display results
                    col1, col2 = st.columns(2)

                    with col1:
                        st.subheader("ATS Match")
                        st.metric("Match Percentage", result["JD Match"])

                        st.subheader("Missing Keywords")
                        st.write(", ".join(result["MissingKeywords"]))

                    with col2:
                        st.subheader("Profile Summary")
                        st.write(result["Profile Summary"])

                    st.subheader("GitHub Project Recommendation")
                    project_rec = result["GitHub Project Recommendation"]
                    st.write(f"**Project Name:** {project_rec['Project Name']}")
                    st.write(f"**Relevance to Job:** {project_rec['Relevance to Job']}")
                    st.write("**Suggested Description for CV:**")
                    st.text(project_rec['Suggested Description for CV'])
                else:
                    st.error("Unexpected API response format. Please check the API and try again.")

            except requests.exceptions.RequestException as e:
                st.error(f"An error occurred during the API request: {e}")
            except ValueError:
                st.error("Invalid JSON response from the API.")
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")

    else:
        st.info(
            "Please upload your resume, enter the job description, and provide your GitHub username to start the analysis.")


if __name__ == "__main__":
    main()
