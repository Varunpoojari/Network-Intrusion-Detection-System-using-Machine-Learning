# setup.py
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="network-ids",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A machine learning-based Network Intrusion Detection System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/network-ids",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=[
        "pandas>=1.3.0",
        "numpy>=1.21.0",
        "scikit-learn>=0.24.0",
        "scapy>=2.4.5"
    ],
    entry_points={
        "console_scripts": [
            "network-ids=network_ids:main",
            "live-network-ids=live_network_ids:main"
        ],
    },
)
