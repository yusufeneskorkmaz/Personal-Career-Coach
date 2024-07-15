import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

class ATSMatcher:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY is not set in the environment variables")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    def match(self, resume_text, job_description, github_project):
        prompt = f"""
        Act as an experienced ATS with deep understanding of the tech field. 
        Evaluate the resume based on the given job description and GitHub project. 

        Resume: {resume_text}
        Job Description: {job_description}
        GitHub Project: {github_project}

        Provide a response in the following JSON structure:
        {{
            "JD Match": "%",
            "MissingKeywords": [],
            "Profile Summary": "",
            "GitHub Project Recommendation": {{
                "Project Name": "",
                "Relevance to Job": "",
                "Suggested Description for CV": ""
            }}
        }}
        """
        try:
            response = self.model.generate_content(prompt)
            response_content = response.content  # Make sure to access the correct attribute
            return json.loads(response_content)
        except json.JSONDecodeError:
            print("Error: Unable to parse JSON response")
            return None
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None
