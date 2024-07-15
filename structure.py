import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "PersonalCareerCoach"

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/resume_parser.py",
    f"src/{project_name}/components/github_analyzer.py",
    f"src/{project_name}/components/ats_matcher.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/career_analysis_pipeline.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/api/__init__.py",
    f"src/{project_name}/api/routes.py",
    f"src/{project_name}/dashboard/__init__.py",
    f"src/{project_name}/dashboard/app.py",
    "main.py",
    "setup.py",
    ".gitignore",
    "README.md",
    ".env",
    "requirements.txt"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")

# Create directories
for dir in ["logs", "data", "models"]:
    os.makedirs(dir, exist_ok=True)
    logging.info(f"Created '{dir}' directory")

print("Project structure created successfully!")