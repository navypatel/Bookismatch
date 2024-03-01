from setuptools import setup

with open("README>md", encoding="utf-8") as f:
    long_description = f.read()


REPO_NAME = "Books-Recommender-System-Using-Machine-Learning"
AUTHOR_USER_NAME = "ShinChan"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS =  ['streamlit', 'numpy']

setup(
    name=SRC_REPO,
    version="0.0.1"
    author=AUTHOR_USER_NAME,
    description="A small package for Book Recommender System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email="navypatel3234@gmail.com",
    packages=[SRC_REPO],
    python_requires=">=3.11.4",
    install_requires=LIST_OF_REQUIREMENTS
)