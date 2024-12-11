from platform import python_revision

from setuptools import setup

with open("README.md", "r", encoding = "utf-8") as f:
    long_description = f.read()

#personal info
REPO_NAME = "Book-Recommender"
AUTHOR_USER_NAME = "saamm"
LIST_OF_REQUIREMENTS = ['streamlit', 'numpy']

setup (
    version = "0.0.1",
    author = AUTHOR_USER_NAME,
    description = "A small package for Book Recommendation System",
    long_description= long_description,
    long_description_content_type= "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email="soumyasinha161093@gmail.com",
    license="Apache License 2.0",
    python_requires = ">=3.11",
    install_requires = LIST_OF_REQUIREMENTS


)