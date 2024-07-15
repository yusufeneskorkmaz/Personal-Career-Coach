from src.PersonalCareerCoach.components.resume_parser import ResumeParser
from src.PersonalCareerCoach.components.github_analyzer import GitHubAnalyzer
from src.PersonalCareerCoach.components.ats_matcher import ATSMatcher
from io import BytesIO


class CareerAnalysisPipeline:
    def __init__(self):
        self.resume_parser = ResumeParser()
        self.github_analyzer = GitHubAnalyzer()
        self.ats_matcher = ATSMatcher()

    def run(self, resume_content, job_description, github_username):
        resume_file = BytesIO(resume_content)
        resume_text = self.resume_parser.parse_pdf(resume_file)
        github_projects = self.github_analyzer.get_user_repos(github_username)
        most_relevant_project = self.github_analyzer.get_most_relevant_project(github_username, job_description)

        result = self.ats_matcher.match(resume_text, job_description, most_relevant_project)
        return result