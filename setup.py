from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setup(
    name = "testpackagedkpb",
    version = "1.0.1",
    description = "This is a test package.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/pythoslabs/littleIndian",
    author = "Dianne Kim Bienes",
    author_email = "kimbienes@gmail.com",
    license = "MIT",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["littleIndian"],
    include_package_data=True,
)