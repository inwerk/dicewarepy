from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

# Setting up
setup(
    name="dicewarepy",
    version="1.0.3",
    description="Minimalist Python library designed for the random selection of words from cryptographic wordlists, utilizing the Diceware method.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/inwerk/dicewarepy",
    author="inwerk",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Topic :: Security",
        "Topic :: Security :: Cryptography",
        "Topic :: Utilities"
    ],
    keywords=[
        "dicewarepy", "diceware", "dice", "die", "passphrase", "passphrases", "password", "passwords"
    ],
    packages=find_packages(),
    package_data={
        "dicewarepy.wordlists": ["*.txt"],
    },
    install_requires=[]
)
