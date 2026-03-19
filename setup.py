from setuptools import setup, find_packages

setup(
    name="sequence",
    version="1.0.0",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "termplotlib",
        "numpy<2.0.0,>=1.21.2"
    ],
    entry_points={
        "console_scripts": [
            "sequence=sequence:main",
        ],
    },
)