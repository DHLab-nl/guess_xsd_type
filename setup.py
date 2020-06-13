import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="guess_xsd_type",
    version="0.1",
    author="Richard L. Zijdeman",
    author_email="richard.zijdeman@iisg.nl",
    description="XSD data type recommender",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DHLab-nl/guess_xsd_type",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
