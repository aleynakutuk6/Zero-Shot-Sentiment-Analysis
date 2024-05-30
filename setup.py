from setuptools import find_packages
from setuptools import setup

setup(
    name="zero-shot-sentiment-analysis",
    version="0.1.0",
    author="Aleyna Kutuk",
    author_email="akutuk21@ku.edu.tr",
    description="Sentiment and Intention Analysis",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/aleynakutuk6/ZeroShotChatAnalysis",
    packages=find_packages(),
    install_requires=["tqdm", "torch>=2.0.0", "transformers>=4.33.0", "datasets"],
    python_requires=">=3.9",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
