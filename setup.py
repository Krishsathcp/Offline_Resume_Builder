from setuptools import setup, find_packages

setup(
    name="resume-builder",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask",
        "pdfkit",
        "requests",
        "python-docx",
        "mammoth",
    ],
    entry_points={
        "console_scripts": [
            "resume-builder = offline_resume_builder.app:main"
        ]
    },
    author="Your Name",
    description="Offline AI-powered resume builder using Flask and Mistral/Ollama",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
