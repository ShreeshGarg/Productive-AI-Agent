from setuptools import setup, find_packages

setup(
    name="productivity-agent",
    version="1.0.0",
    description="Autonomous AI Agent for task management",
    author="Your Name",
    python_requires=">=3.10",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "google-generativeai>=0.6.0",
        "flask>=2.3.0",
        "python-dotenv>=1.0.0",
        "requests>=2.31.0",
    ],
)
