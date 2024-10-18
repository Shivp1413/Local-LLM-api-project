from setuptools import setup, find_packages

setup(
    name="llama-api-project",
    version="0.1.0",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "fastapi==0.68.0",
        "uvicorn==0.15.0",
        "ollama==0.1.1",
    ],
    extras_require={
        "dev": [
            "pytest==6.2.5",
            "pytest-mock==3.6.1",
        ],
    },
    author="Shivp1413",
    description="A FastAPI project for running LLAMA 3.1 model using Ollama",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/llama-api-project",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
