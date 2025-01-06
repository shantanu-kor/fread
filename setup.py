from setuptools import setup, find_packages

setup(
    name="fread",
    version="0.1.0",
    description="Used exnd-curses to output file content.",
    author="Shantanu Kor",
    author_email="kor.shantanu1@gmail.com",
    url="https://github.com/shantanu-kor/fread.git",
    packages=find_packages(),
    install_requires=["exnd-curses"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)