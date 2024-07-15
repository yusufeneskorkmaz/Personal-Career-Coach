from setuptools import find_packages, setup

setup(
    name='PersonalCareerCoach',
    version='0.0.1',
    author='yusufeneskorkmaz',
    author_email='yusufeneskorkmaz@outlook.com',
    description='A Personal Career Coach with ATS analysis and GitHub project recommendations',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)